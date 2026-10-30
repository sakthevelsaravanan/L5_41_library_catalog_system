# Reflection – Static Code Analysis

**Note:** The uploaded repository README says to answer four reflection questions from the lab handout, but the handout and the exact questions were not included in the uploaded files. The following are four draft reflections based on the work performed. Please compare them with the handout and adjust the wording or headings if its questions are different.

## 1. What is the purpose of static code analysis?

Static code analysis checks source code without running the program. Tools such as Pylint and Flake8 identify style problems, unused variables, naming issues, and other code-quality concerns. Bandit focuses on common security risks. These tools help find problems early and make code easier to maintain.

## 2. What issues were found in the original program?

The original program contained both code-quality and security issues. Examples included the use of `eval()`, MD5 hashing, shell command execution with `os.system()`, a bare `except`, and a mutable default list. Pylint and Flake8 also reported unused imports and variables, missing docstrings, naming issues, and formatting problems.

## 3. Which fixes were made, and why?

The program was updated to use SHA-256 instead of MD5 and the `secrets` module instead of `random` for temporary PIN generation. The `eval()` call was replaced with direct fine calculation using a daily rate. Shell execution was removed. Book returns now check the book ID explicitly, and the issue function uses `None` instead of a shared mutable list as its default. File export now uses a context manager and UTF-8 encoding. These changes improve security, reliability, and readability.

## 4. What did you learn from this lab?

I learned that a program can run and produce output while still containing security vulnerabilities and poor coding practices. Different analysis tools identify different categories of problems, so using more than one tool gives better coverage. I also learned that fixing warnings should not be done blindly: the changes must preserve the program's intended functionality and should be checked by running the program and repeating the analysis.
