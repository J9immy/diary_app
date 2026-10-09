# Diary Entry Application

A command-line diary for IT 566 Computer Scripting Techniques. Users write dated entries that are saved to a text file, one entry per line.

## Features

- Add a dated diary entry (press Enter to use today's date)
- View entries for a specific date
- View all entries
- Choose or load a different diary file
- Entries are saved in the format `YYYY-MM-DD | Entry text`

## Requirements

Python 3.10 or newer (the menu uses `match`/`case`).

## How to Run

From the project root directory, run `python src/main.py`

On macOS or Linux, use `python3 src/main.py`

## Project Structure

- `src/main.py`: main entry point; handles the menu and user input
- `src/diary_manager.py`: reads, writes, and filters diary entries
- `tests/`: reserved for unit tests
- `docs/`: reserved for project documentation

## Author

Jimmy Morrison
(Student Marymount University)
