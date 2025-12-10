# Library Management System

A simple command-line library management system built with Python and PostgreSQL.

## Features

- Add and remove books from the library
- Search books by title or author
- Borrow and return books
- View all books or only available books
- Track borrowed books count

## Project Structure

```
LMS/
├── src/
│   ├── cli.py          # Command-line interface
│   ├── db.py           # Database connection handler
│   └── library.py      # Library and Book classes
├── .env.example        # Environment variables template
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── schema.sql          # Database schema
```

## Prerequisites

- Python 3.7 or higher
- PostgreSQL database
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd LMS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your database:
```bash
psql -U your_username -d your_database -f schema.sql
```

4. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your database credentials:
```
PGHOST=your_host
PGDATABASE=your_database
PGUSER=your_username
PGPASSWORD=your_password
```

## Usage

Run the application:
```bash
python src/cli.py
```

### Available Commands

- **Add new book** - Add a book with ISBN, title, and author
- **Remove book** - Remove a book using its ISBN
- **Search by title** - Find books by their title
- **Search by author** - Find books by author name
- **Borrow a book** - Mark a book as borrowed
- **Return a book** - Mark a book as available
- **Show all books** - Display the complete library inventory
- **Show available books** - Display only available books
- **Count all books** - Show total number of books
- **Count borrowed books** - Show number of borrowed books

## Database Schema

The system uses a single `books` table with the following structure:

- `isbn` (VARCHAR, PRIMARY KEY) - Unique book identifier
- `title` (VARCHAR) - Book title
- `author` (VARCHAR) - Book author
- `available` (BOOLEAN) - Availability status

## Dependencies

- psycopg2 - PostgreSQL adapter for Python
- python-dotenv - Environment variable management

## Notes

- ISBN values are immutable once set
- Books are marked as available by default when added
- The system prevents duplicate ISBNs

## What I Learned
- Working with PostgreSQL databases
- Implementing CRUD operations
- Object-oriented programming in Python
- Database connection management
- Environment variable configuration

## License

This project is open source and available for educational purposes.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-13+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
