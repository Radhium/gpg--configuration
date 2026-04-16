# check2_key_expiry.py
# Checks whether the GPG key has an expiry date and if it is still valid

import subprocess
from datetime import datetime

def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result.stdout.strip(), result.stderr.strip()

print("=" * 50)
print("Check 2 — GPG Key Expiry")
print("=" * 50)

out, _ = run(r'"C:\Program Files\GnuPG\bin\gpg.exe" --list-secret-keys --keyid-format=long')

expires = None
for line in out.splitlines():
    if "sec" in line:
        if "expires" in line:
            part = line.split("expires")[-1].strip().rstrip("]")
            try:
                expires = datetime.strptime(part, "%Y-%m-%d")
            except ValueError:
                pass
        break

if expires is None:
    print("\nExpiry    : No expiry date set")
    print("\nRESULT: PASS — key never expires")
else:
    today = datetime.today()
    print(f"\nExpiry    : {expires.strftime('%Y-%m-%d')}")
    if expires > today:
        days_left = (expires - today).days
        print(f"Days left : {days_left}")
        print("\nRESULT: PASS — key is still valid")
    else:
        print("\nRESULT: FAIL — key has expired")

print("=" * 50)