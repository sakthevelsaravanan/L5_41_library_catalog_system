# Static Code Analysis – Issues Identified

The table below is based on the original `pylint_report.txt`, `bandit_report.txt`, and `flake8_report.txt`. High- and medium-severity security issues are listed first. Line numbers refer to the original `library_catalog_system.py` file, before cleanup.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| MD5 used for patron hash | Security – High | 47 | MD5 is a weak hashing algorithm and should not be used where collision resistance matters. | Replaced `hashlib.md5()` with SHA-256. |
| Shell command built using filename | Security – High | 58 | `os.system()` runs a shell command containing the filename, which can create command-injection risk. | Removed shell execution and used a normal Python `print()` message. |
| Use of `eval()` | Security – Medium | 42 | `eval()` can execute arbitrary Python expressions instead of only calculating a fine. | Replaced the expression string with a numeric daily rate and direct multiplication. |
| Bare `except` followed by `pass` | Code quality / Security – Low | 24–27 | All exceptions are silently ignored, hiding errors such as invalid book IDs. | Removed exception handling and explicitly checked whether the book ID exists. |
| Non-cryptographic random PIN | Security – Low | 50–51 | `random.randint()` is not intended for security-sensitive PIN generation. | Used `secrets.randbelow()` to generate a secure four-digit PIN. |
| Mutable default list | Code quality | 15 | The default `active_issues=[]` is shared between function calls. | Changed the default to `None` and create a new list inside the function. |
| Unused import and variables | Code quality | 6, 31, 41 | `csv`, `late_fee`, and `days` are unused. | Removed unused items. |
| Function naming and missing docstrings | Maintainability | 15, 23, 30, 40, 46, 50, 54, 61 | The function `issueBook` does not follow snake_case and functions lack documentation. | Renamed it to `issue_book` and added docstrings. |
| Comparison with `None` | Style | 32 | `== None` is not the recommended Python comparison. | Used `is not None` in the availability check. |
| File handling without context manager or encoding | Reliability / Style | 55–57 | The file is manually opened and closed without specifying an encoding. | Used `Path.open()` with UTF-8 encoding and a `with` statement. |
| Missing final newline | Formatting | 73 | The original source file does not end with a newline. | Added a final newline. |

## Summary

The original analysis reported a Pylint score of **5.32/10** and identified **5 Bandit findings**: 2 high, 1 medium, and 2 low severity. The cleaned program addresses the reported security and code-quality problems while retaining the library catalog's main operations.
