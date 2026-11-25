#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes a single Wi-Fi network name (at most 32 characters) to
/output/entry.txt. The name is a joke that implies a whole story:
a kid changed the Wi-Fi password, and only mum knows the new one.
"""

import os

ENTRY = "I changed it, ask your mother"


def main() -> None:
    assert 1 <= len(ENTRY) <= 32, f"entry is {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
