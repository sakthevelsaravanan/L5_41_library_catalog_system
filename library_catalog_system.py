"""Library catalog management module.

Provides basic book circulation, fine calculation, patron utilities,
and catalog export functionality.
"""

import hashlib
import json
import secrets
from pathlib import Path
from typing import Optional

CATALOG = {
    "B01": {"title": "Clean Code", "copies": 3},
    "B02": {"title": "The Pragmatic Programmer", "copies": 1},
    "B03": {"title": "Design Patterns", "copies": 2},
}


def issue_book(book_id: str, patron: str,
               active_issues: Optional[list[str]] = None) -> bool:
    """Issue a copy of a book when it is available."""
    if book_id not in CATALOG or CATALOG[book_id]["copies"] <= 0:
        return False

    if active_issues is None:
        active_issues = []

    CATALOG[book_id]["copies"] -= 1
    active_issues.append(f"Issued book {book_id} to patron {patron}")
    return True


def return_book(book_id: str) -> bool:
    """Return a book copy; return False when the book ID is unknown."""
    if book_id not in CATALOG:
        return False

    CATALOG[book_id]["copies"] += 1
    return True


def check_availability(book_id: str) -> bool:
    """Check whether a known book has at least one available copy."""
    book = CATALOG.get(book_id)
    return book is not None and book["copies"] > 0


def calculate_fine(days_overdue: int, daily_rate: float = 2.0) -> float:
    """Calculate an overdue fine without evaluating user-supplied code."""
    if days_overdue < 0 or daily_rate < 0:
        raise ValueError("Days overdue and daily rate must be non-negative.")
    return days_overdue * daily_rate


def generate_patron_hash(patron_id: str) -> str:
    """Return a SHA-256 digest for a patron identifier."""
    return hashlib.sha256(patron_id.encode("utf-8")).hexdigest()


def generate_temp_patron_pin() -> str:
    """Generate a cryptographically secure four-digit temporary PIN."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def export_catalog(filename: str = "catalog_export.txt") -> None:
    """Export the catalog as JSON text."""
    output_path = Path(filename)
    with output_path.open("w", encoding="utf-8") as output_file:
        json.dump(CATALOG, output_file, indent=4)
        output_file.write("\n")
    print(f"Catalog backup exported to: {output_path}")


def main() -> None:
    """Run a short demonstration of the library catalog functions."""
    issue_book("B01", "P101")
    return_book("B02")
    print("Is B01 available:", check_availability("B01"))
    print("Fine accrued:", calculate_fine(4))
    print("Patron Hash:", generate_patron_hash("P101"))
    print("Temp PIN:", generate_temp_patron_pin())
    export_catalog()


if __name__ == "__main__":
    main()
