# hello.py

# 1. The classic way
print("Hello Python 🐍 from an experienced dev")

# 2. Using logging for better control in larger projects
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Hello from logging")

# 3. Debug print with f-strings
name = "Python"
version = 3.12
print(f"Debug: We're using {name} version {version}")

# 4. Use warnings if the message is about potential issues
import warnings
warnings.warn("This is a warning message")

# 5. pprint for structured data (e.g. dicts, lists)
from pprint import pprint
sample_data = {'name': 'Alice', 'skills': ['Python', 'Rust', 'C++']}
pprint(sample_data)

# Notes for experienced devs:
# - `print()` is fine for quick scripts and debugging.
# - `logging` is preferred for real applications and production code.
# - You can control log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
# - `pprint` helps with visualizing nested structures during development.
