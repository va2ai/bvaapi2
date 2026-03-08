#!/usr/bin/env python3
"""Keep gcloud auth alive and exchange code via temp file."""
import subprocess, threading, time, os, sys

GCLOUD = r'C:\Users\ccdmn\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd'
CODE_FILE = r'C:\Users\ccdmn\code\bvaapi\gauth_code.txt'
URL_FILE  = r'C:\Users\ccdmn\code\bvaapi\gauth_url.txt'

for f in [CODE_FILE, URL_FILE]:
    if os.path.exists(f):
        os.remove(f)

proc = subprocess.Popen(
    [GCLOUD, 'auth', 'login', 'denvercombs@vaclaims.net', '--no-launch-browser'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True, bufsize=1
)

url_found = threading.Event()

def read_output():
    for line in proc.stdout:
        sys.stdout.write(line)
        sys.stdout.flush()
        if 'accounts.google.com' in line:
            with open(URL_FILE, 'w') as f:
                f.write(line.strip())
            url_found.set()

t = threading.Thread(target=read_output, daemon=True)
t.start()

url_found.wait(timeout=15)
print("=== URL captured — polling for code file ===", flush=True)

code = None
for _ in range(120):
    if os.path.exists(CODE_FILE):
        with open(CODE_FILE) as f:
            code = f.read().strip()
        if code:
            break
    time.sleep(1)

if not code:
    print("Timed out.", flush=True)
    proc.kill()
    sys.exit(1)

print("Sending code to gcloud...", flush=True)
proc.stdin.write(code + '\n')
proc.stdin.flush()

t.join(timeout=15)
proc.wait()
print(f"Done. Exit: {proc.returncode}", flush=True)
