# Task 3: Secure Coding Review

## Objective
Review a small Python example for common secure-coding issues and document safer alternatives.

## Files
- `secure_example.py`: improved example using allow-list validation and mock data
- `test_secure_example.py`: unit tests for normal and invalid inputs
- `review_report.md`: findings, recommendations, and scope/limitations

## Run
```bash
python secure_example.py
python -m unittest -v
```

## Optional static analysis
Install Bandit and scan this folder:
```bash
python -m pip install bandit
bandit -r .
```
A scanner can produce false positives or miss issues. Review findings manually.

## Important
This is a learning example, not a complete production authentication system or a substitute for a professional audit.
