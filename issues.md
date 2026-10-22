

\# Lab 5: Static Code Analysis — Issue Log



| Issue | Type | Line(s) | Description | Fix Approach |

|---|---|---|---|---|

| Route accessed after deletion | Runtime bug | 55, 58 | R3 is deleted before its average is calculated, causing a KeyError and terminating the program. | Correct the order of operations or handle the route's absence appropriately. |

| Invalid passenger counts | Data validation | 49–50 | A negative count and a string are recorded as passenger counts. These values can produce incorrect results or type errors. | Validate passenger counts and ensure that trip data uses a consistent numeric type. |

| Mutable default argument | Bug / Code quality | 11–13 | The default logs list is shared across calls, so entries can accumulate unexpectedly. Pylint W0102. | Use a None default and initialize a fresh list when needed. |


| Bare exception and ignored errors | Reliability / Error handling | 26–30 | A bare except catches every exception and pass silently discards it. Pylint W0702, Flake8 E722 and Bandit B110. | Replaced the bare exception handler with explicit handling for TypeError and ZeroDivisionError. The program now prints an explanatory message rather than silently ignoring the error. |
| Pseudorandom generator warning | Security analysis | 33–35 | Bandit B311 flags random.choice because the standard pseudorandom generator is unsuitable for cryptographic purposes. The original driver-selection operation does not itself require cryptographic randomness. | Replaced random.choice with secrets.choice. This removes Bandit's B311 finding, although cryptographic randomness is not necessary for this particular application. |


| Pseudorandom generator warning | Security analysis | 33–35 | Bandit B311 flags random.choice because the standard pseudorandom generator is unsuitable for cryptographic purposes. The current driver-selection use is not inherently a cryptographic operation. | Assess the context and use an appropriate alternative or document a justified exception. |

| File handling without encoding or context managers | Resource management | 37–43 | Files are opened without explicit encoding, and the file objects are not consistently closed through context management. Pylint W1514 and R1732. | Use context managers and specify an appropriate encoding. |

| Average of an empty route | Runtime edge case | 19–21 | Calculating the average of a route with no trips results in division by zero. | Handle empty trip lists according to the intended behaviour. |

| Invalid function name and unused argument | Style / Code quality | 33–35 | assignDriver violates snake\_case naming conventions, and route\_id is unused. Pylint C0103 and W0613. | Rename the function and either use the argument meaningfully or remove it and update its callers. |

| Missing docstrings | Code quality | 1, 11, 16, 19, 23, 33, 37, 45 | The module and functions lack explanatory docstrings. Pylint C0114 and C0116. | Add a module docstring and concise docstrings for functions. |

| String formatting and line length | Style | 13 | The log message uses an old-style formatting pattern that Pylint recommends replacing, and the line exceeds the Flake8 limit. Pylint C0209 and Flake8 E501. | Use an f-string and format the expression across appropriately sized lines. |

| Blank-line formatting | Style | 11, 16, 19, 23, 33, 37, 45, 60 | Top-level functions and the final function call do not have the required spacing. Flake8 E302 and E305. | Apply the required blank-line spacing between functions and after the final function definition. |



## Bandit Verification

- Original report: `bandit_before.txt`
- Updated report: `bandit_after_1.txt`
- Result: No issues identified.
- Findings resolved: B110 and B311.
- Verification date: 22 October 2026.

