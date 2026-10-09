"""Read, write, and filter diary entries stored in a text file.

Each diary entry is saved as one line in the diary file using this format:

    YYYY-MM-DD | Entry text
"""

import os
from datetime import date, datetime

DATE_FORMAT = '%Y-%m-%d'
SEPARATOR = ' | '


def get_today():
    """Return today's date as a YYYY-MM-DD string."""
    return date.today().strftime(DATE_FORMAT)


def is_valid_date(date_text):
    """Return True if date_text is a real date in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_text, DATE_FORMAT)
        return True
    except ValueError:
        return False


def prepare_diary_file(file_path):
    """Make sure the diary file exists, creating it if needed.

    Returns the full (absolute) path to the diary file.
    """
    full_path = os.path.abspath(file_path)
    folder = os.path.dirname(full_path)

    if not os.path.exists(folder):
        os.makedirs(folder)

    # Opening in append mode creates the file if it does not exist
    # and leaves any existing entries untouched.
    with open(full_path, 'a', encoding='utf-8'):
        pass  # Nothing to see here. This line is just enjoying the view.

    return full_path


def add_entry(file_path, entry_date, entry_text):
    """Append one dated entry to the diary file as a single line."""
    # Replace any line breaks so the entry stays on one line.
    clean_text = ' '.join(entry_text.splitlines()).strip()

    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f'{entry_date}{SEPARATOR}{clean_text}\n')


def read_entries(file_path):
    """Return a list of (date, text) tuples from the diary file.

    Blank lines and lines that are not in the expected format are skipped.
    """
    entries = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if SEPARATOR not in line:
                continue

            # Split only on the first separator so the entry text
            # can safely contain the | character.
            entry_date, entry_text = line.split(SEPARATOR, 1)
            if is_valid_date(entry_date):
                entries.append((entry_date, entry_text))

    return entries


def filter_entries_by_date(entries, target_date):
    """Return only the entries that match target_date."""
    return [entry for entry in entries if entry[0] == target_date]


def format_entry(entry):
    """Return an entry tuple as a printable string."""
    entry_date, entry_text = entry
    return f'{entry_date}  {entry_text}'

# TODO:
# - search entries by keyword
# - delete an entry
# - main() function with a menu
# - teach the diary to keep secrets
