# LazyLib

![Logo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2hqNW13aWJjd2txZmR3bGp5d3N5ZHZqa2kxNTg3bWk5OHMwaDFvZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/pVkmGyqYRt4qY/giphy.gif)

A Python automation tool that dynamically handles library dependencies and virtual environments. No more manual `pip install` errors!

'-------------'![Static Badge](https://img.shields.io/badge/Made_in-KSA-white)'-------------'

## What This Tool Does

LazyLib is designed to make running Python scripts seamless by automating the boring setup parts:

* **Auto-Detection:** Reads your target script and identifies all required libraries via `ast` parsing.
* **Virtual Environment Management:** Automatically creates a `venv` if it doesn't exist (on Linux/Mac).
* **Environment Rebooting:** Restarts itself inside the virtual environment to ensure isolated execution.
* **Dynamic Installation:** Checks and installs missing libraries using `pip` on the fly.
* **Zero Configuration:** Runs your target script immediately after the environment is ready.

### Why LazyLib?

* **Portability:** Share a script with someone and let LazyLib handle the setup for them.
* **Clean Systems:** Keeps your global Python installation clean by forcing usage of Virtual Environments.
* **Cross-Platform:** Includes logic for both Windows and Unix-based systems.

---

# Quick Usage

Easy as hell I ain’t lying about the name
```bash
python lazylib.py your_script.py
