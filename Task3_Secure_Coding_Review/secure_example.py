"""Safer input-handling example for a simple account lookup.

This is a self-contained teaching example. It does not connect to a real database.
"""
import re
from dataclasses import dataclass

USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_]{3,20}$")


@dataclass(frozen=True)
class Account:
    username: str
    display_name: str


# Mock data for demonstration only.
ACCOUNTS = {
    "momina_01": Account("momina_01", "Demo User"),
    "student_02": Account("student_02", "Sample Student"),
}


def normalize_username(value: str) -> str:
    """Validate a username against a narrow allow-list."""
    if not isinstance(value, str):
        raise ValueError("Username must be text.")
    candidate = value.strip()
    if not USERNAME_PATTERN.fullmatch(candidate):
        raise ValueError("Username must be 3–20 characters: letters, numbers, underscore.")
    return candidate


def find_account(username: str):
    """Return a mock account or None; do not expose internal errors."""
    safe_username = normalize_username(username)
    return ACCOUNTS.get(safe_username)


def main():
    try:
        username = input("Enter demo username (or press Enter to exit): ")
        if not username:
            print("No username entered. Exiting.")
            return
        account = find_account(username)
        if account is None:
            print("No matching account.")
        else:
            print(f"Account found: {account.display_name}")
    except ValueError as exc:
        print(f"Invalid input: {exc}")


if __name__ == "__main__":
    main()
