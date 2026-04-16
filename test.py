# test.py
# GPG configuration test — verifies Git signing setup is correct

import subprocess

def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result.stdout.strip(), result.stderr.strip()

print("=" * 50)
print("GPG + Git Configuration Check")
print("=" * 50)

# GPG version
out, _ = run(r'"C:\Program Files\GnuPG\bin\gpg.exe" --version')
print(f"\n[1] GPG version:\n    {out.splitlines()[0]}")

# Git signing key
out, _ = run("git config --global user.signingkey")
print(f"\n[2] Signing key:  {out or 'NOT SET'}")

# GPG sign enabled
out, _ = run("git config --global commit.gpgsign")
print(f"[3] Auto-sign:    {out or 'NOT SET'}")

# GPG program path
out, _ = run("git config --global gpg.program")
print(f"[4] GPG program:  {out or 'NOT SET'}")

# Git user name and email
name, _ = run("git config --global user.name")
email, _ = run("git config --global user.email")
print(f"[5] Git user:     {name} <{email}>")

# Check if key exists in keyring
out, err = run(r'"C:\Program Files\GnuPG\bin\gpg.exe" --list-secret-keys --keyid-format=long')
if "sec" in out:
    print(f"\n[6] GPG key found in keyring: OK")
else:
    print(f"\n[6] GPG key found in keyring: NOT FOUND")

print("\n" + "=" * 50)
print("All checks done. If everything shows OK, you're good to go!")
print("=" * 50)