# Library Book Management System  
Agile Development with Git and Unit Testing

## Course
CS2042 – Software Engineering
Name: Aviral
Roll No: 240101017

## Assignment Overview
This project implements a **Library Book Management System** using Python by following a **three-sprint Agile development process**. The system is developed incrementally using Git feature branches, unit testing, and version tagging. All data is managed using **in-memory data structures** (no database).

The focus of this assignment is **software engineering process adherence**, not just functional correctness.

---

## Technology Stack
- Programming Language: Python
- Testing Framework: unittest
- Version Control: Git
- Database: Not used (in-memory only)

---

## Features (Sprint-wise)

### Sprint 1 – Book Registration (v0.1)
- Add books with Book ID, Title, and Author
- Prevent duplicate Book IDs
- Unit tests for book addition and validation

### Sprint 2 – Borrow and Return Book (v0.2)
- Borrow an available book
- Return a borrowed book
- Prevent borrowing an already borrowed book
- Unit tests for borrow and return scenarios

### Sprint 3 – Library Report (v0.3)
- Generate a library status report
- Report includes Book ID, Title, Author, and Status
- Unit tests to validate report content

---

## Project Structure
library-se/
│
├── src/
│ └── library.py
│
├── tests/
│ └── test_library.py
│
├── docs/
│ ├── USER_STORIES.md
│ └── TRACEABILITY.md
│
├── README.md


---

## Agile & Git Workflow
- No direct commits to `main`
- Each sprint developed in its own branch:
  - `feature/sprint-1`
  - `feature/sprint-2`
  - `feature/sprint-3`
- Each sprint merged into `main` only after tests passed
- Tags created after each sprint merge:
  - `v0.1`, `v0.2`, `v0.3`

---

## Running Unit Tests
All unit tests can be executed using the following command:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
