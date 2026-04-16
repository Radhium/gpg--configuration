# check3_gpg_path.py
# Confirms that the GPG program path configured in Git actually exists on disk

import subprocess
import os

def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result.stdout.strip(), result.stderr.strip()

print("=" * 50)
print("Check 3 — GPG Program Path on Disk")
print("=" * 50)

configured_path, _ = run("git config --global gpg.program")
print(f"\nConfigured path : {configured_path or 'NOT SET'}")

if not configured_path:
    print("\nRESULT: FAIL — gpg.program is not set in Git config")
elif os.path.exists(configured_path):
    print(f"File exists     : YES")
    print("\nRESULT: PASS — GPG program found at configured path")
else:
    print(f"File exists     : NO")
    print("\nRESULT: FAIL — GPG program not found at configured path")

print("=" * 50)