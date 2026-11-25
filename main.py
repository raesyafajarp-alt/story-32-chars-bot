#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes a single Wi-Fi network name (at most 32 characters) to
/output/entry.txt. The name is a joke that implies a whole story:
mum keeps changing the Wi-Fi password, and only she knows the new
one — "again" turns one password change into a recurring saga.
"""

import os

ENTRY = "Ask mom, she changed it again"


def main() -> None:
    assert 1 <= len(ENTRY) <= 32, f"entry is {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
