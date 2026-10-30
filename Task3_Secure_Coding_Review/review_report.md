# Secure Coding Review Report

## Project
**Target:** A small Python account-lookup example  
**Review type:** Educational static/manual review  
**Scope:** Input validation, data access patterns, error handling, and information exposure  
**Limitations:** This is a teaching example, not a full production audit. No real database, authentication system, or external service is connected.

## Security risks to look for in an unsafe implementation
1. **Unvalidated input:** Arbitrary input can cause unexpected behavior and may become dangerous when passed into shell commands, SQL queries, file paths, or other interpreters.
2. **String-built database queries:** Concatenating user input into SQL can create SQL injection. Use parameterized queries instead.
3. **Excessive error details:** Returning stack traces or database errors to end users can reveal implementation details.
4. **Overly broad permissions:** An application account should receive only the database and operating-system permissions it needs.
5. **Sensitive data in logs:** Passwords, tokens, one-time codes, and private packet contents should not be logged.
6. **Missing tests:** Security assumptions should be verified with positive, negative, boundary, and malformed-input tests.

## Improvements demonstrated in `secure_example.py`
- Uses a strict allow-list for the demo username.
- Trims leading/trailing whitespace.
- Rejects invalid characters and out-of-range lengths.
- Uses a dictionary lookup for mock data; it does not build a SQL query.
- Shows a simple, user-safe error message for invalid input.
- Includes unit tests for expected and rejected input.

## Recommendations for a production application
- If a database is introduced, use parameterized queries or a well-maintained ORM; never concatenate input into SQL.
- Apply authentication and authorization checks on every protected operation.
- Store passwords only with a modern password-hashing function such as Argon2id, scrypt, or bcrypt; never store plaintext passwords.
- Keep secrets in environment variables or a secrets manager, not source code.
- Log security-relevant events without logging credentials or tokens.
- Keep dependencies updated and run a static analyzer such as Bandit (`python -m pip install bandit`, then `bandit -r .`) in a controlled project directory.
- Add rate limiting, monitoring, and a documented vulnerability-response process where relevant.

## Test results
Run from this folder:
```bash
python -m unittest -v
```
Expected result: six tests pass. Tests cover valid, unknown, whitespace-padded, malformed, too-short, and non-text inputs.

## Conclusion
The reviewed example applies basic input validation and predictable error handling. These measures reduce common input-handling risks, but do not replace a complete security assessment of a real application.
