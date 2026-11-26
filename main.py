import os

TEXT = "My mother told me to always keep bus fare home in a separate pocket, so I'd never have to stay anywhere I didn't want to be."

assert 1 <= len(TEXT) <= 200, f"length {len(TEXT)} out of range"
assert "\n" not in TEXT and "\r" not in TEXT, "must be single line"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)

with open(path, encoding="utf-8") as f:
    data = f.read()

assert data == TEXT, "read-back mismatch"
assert 1 <= len(data) <= 200, f"read-back length {len(data)} out of range"
assert "\n" not in data and "\r" not in data, "read-back must be single line"

print(f"OK {len(data)} chars")
