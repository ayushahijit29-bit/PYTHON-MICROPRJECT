# Library Management System

A simple Python-based library management system for tracking books, handling issuing and returning, and maintaining availability status.

## Features

- Add books with title, author, and ISBN
- Issue books to users with due dates
- Return books
- Search books by title or author
- List available and issued books
- Check for overdue books
- Calculate fines for overdue books (unique feature: automated fine calculation based on days overdue)

## Unique Features

- Automatic due date tracking and overdue detection
- Fine calculation with customizable rate
- ISBN uniqueness validation
- User-friendly console interface

## Requirements

- Python 3.x

## Installation

1. Clone or download the project.
2. Ensure Python 3.x is installed.

## Usage

Run the main script:

```bash
python main.py
```

Follow the menu prompts to manage the library.

## Integration

This code is modular and can be easily integrated into larger applications. Import the `Library` class from `library.py` and use its methods.

Example:

```python
from library import Library

lib = Library()
lib.add_book("Book Title", "Author", "ISBN")
lib.issue_book("ISBN", "User Name")
```

## Troubleshooting

- Ensure ISBNs are unique when adding books.
- Dates are handled using Python's datetime module.
- No external dependencies required.