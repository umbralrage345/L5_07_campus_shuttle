# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing the program. It helps identify potential bugs, insecure coding patterns, maintainability problems, and style violations early in development. It improves code quality and helps developers detect problems before deployment. However, it does not replace runtime testing because some logical errors only become apparent when the program executes.

## 2. What are the differences between Pylint, Bandit, and Flake8?

Pylint evaluates Python code quality, including naming conventions, missing docstrings, unused arguments, and potentially problematic coding practices. Bandit identifies potentially insecure coding patterns. Flake8 checks Python style and formatting, including whitespace, blank-line spacing, and line length. Using these tools together provides complementary perspectives on code quality, security, and consistency.

## 3. What issues were identified and how were they resolved?

The analysis identified a mutable default argument, missing docstrings, inconsistent naming, an unused function argument, broad exception handling, file operations without context managers, and formatting violations. Bandit also flagged the exception-handling pattern and the use of the standard pseudorandom generator. The changes included initializing default lists safely, adding docstrings, using consistent naming, handling expected exceptions explicitly, specifying file encodings, using context managers, and correcting formatting. Additional runtime problems were addressed, including invalid passenger counts, empty trip lists, and accessing a route after deletion.

## 4. What are the limitations of static analysis?

Static analysis does not guarantee that a program is free from defects. A tool may not detect every logical error or determine whether a warning is relevant to the application's particular use case. For example, a pseudorandom generator warning must be evaluated in context; ordinary driver selection does not inherently require cryptographic randomness. Running the program and testing normal inputs, invalid inputs, and edge cases remain necessary to verify correct behaviour.
