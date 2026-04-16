# check1_email_match.py
# Verifies that the GPG key email matches the Git global email

import subprocess

def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result.stdout.strip(), result.stderr.strip()

print("=" * 50)
print("Check 1 — GPG Email vs Git Email")
print("=" * 50)

git_email, _ = run("git config --global user.email")

out, _ = run(r'"C:\Program Files\GnuPG\bin\gpg.exe" --list-secret-keys --keyid-format=long')

gpg_email = ""
for line in out.splitlines():
    if "@" in line and "<" in line:
        gpg_email = line.strip().split("<")[-1].replace(">", "").strip()
        break

print(f"\nGit email : {git_email}")
print(f"GPG email : {gpg_email}")

if git_email and gpg_email and git_email == gpg_email:
    print("\nRESULT: PASS — emails match")
else:
    print("\nRESULT: FAIL — emails do not match")

print("=" * 50)