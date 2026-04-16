# check4_pretty.py
# Full GPG + Git configuration check with PASS / FAIL output

import subprocess
import os

def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result.stdout.strip(), result.stderr.strip()

def status(label, condition):
    result = "PASS" if condition else "FAIL"
    print(f"  [{result}] {label}")
    return condition

print("=" * 50)
print("Full GPG Configuration Check")
print("=" * 50)
print()

# 1. GPG version
out, _ = run(r'"C:\Program Files\GnuPG\bin\gpg.exe" --version')
version_line = out.splitlines()[0] if out else ""
print(f"  GPG : {version_line or 'not found'}")
print()

# 2. Signing key set
signing_key, _ = run("git config --global user.signingkey")
status("Signing key configured", bool(signing_key))

# 3. Auto-sign enabled
auto_sign, _ = run("git config --global commit.gpgsign")
status("Auto-sign enabled", auto_sign == "true")

# 4. GPG program path exists
gpg_path, _ = run("git config --global gpg.program")
status("GPG program path exists on disk", os.path.exists(gpg_path) if gpg_path else False)

# 5. Key exists in keyring
keyring, _ = run(r'"C:\Program Files\GnuPG\bin\gpg.exe" --list-secret-keys --keyid-format=long')
status("GPG key found in keyring", "sec" in keyring)

# 6. Email match
git_email, _ = run("git config --global user.email")
gpg_email = ""
for line in keyring.splitlines():
    if "@" in line and "<" in line:
        gpg_email = line.strip().split("<")[-1].replace(">", "").strip()
        break
status("GPG email matches Git email", git_email == gpg_email)

# 7. Key name check
git_name, _ = run("git config --global user.name")
gpg_name = ""
for line in keyring.splitlines():
    if "uid" in line:
        gpg_name = line.strip().split("]")[-1].strip().split("(")[0].strip()
        break
status("GPG name matches Git username", git_name.lower() in gpg_name.lower())

print()
print("=" * 50)