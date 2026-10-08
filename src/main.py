"""Diary Entry Application.

Main entry point. Lets the user choose a diary file, add dated entries,
and print entries filtered by date.
"""

import diary_manager

DEFAULT_DIARY_FILE = 'diary.txt'


def print_menu(current_file):
    """Display the main menu and the diary file currently in use."""
    print()
    print('=' * 50)
    print('DIARY ENTRY APPLICATION')
    print(f'Current diary file: {current_file}')
    print('=' * 50)
    print('1. Add a diary entry')
    print('2. View entries by date')
    print('3. View all entries')
    print('4. Select or load a different diary file')
    print('5. Quit')


def select_diary_file(current_file):
    """Ask the user which file to use as the diary and return its path."""
    file_name = input('Enter diary file name (press Enter to keep '
                      'the current file): ').strip()

    if not file_name:
        return current_file

    if not file_name.endswith('.txt'):
        file_name = f'{file_name}.txt'

    new_file = diary_manager.prepare_diary_file(file_name)
    print(f'Now using diary file: {new_file}')
    return new_file


def prompt_for_date(prompt):
    """Keep asking until the user enters a valid date or presses Enter.

    Pressing Enter returns today's date.
    """
    while True:
        date_text = input(prompt).strip()

        if not date_text:
            return diary_manager.get_today()

        if diary_manager.is_valid_date(date_text):
            return date_text

        print('Invalid date. Please use the format YYYY-MM-DD.')


def add_entry(current_file):
    """Get a date and entry text from the user and save the entry."""
    entry_date = prompt_for_date('Entry date YYYY-MM-DD '
                                 '(press Enter for today): ')
    entry_text = input('Write your entry: ').strip()

    if not entry_text:
        print('Entry was empty. Nothing was saved.')
        return

    diary_manager.add_entry(current_file, entry_date, entry_text)
    print(f'Entry saved for {entry_date}.')


def view_entries_by_date(current_file):
    """Print every entry that matches a date chosen by the user."""
    target_date = prompt_for_date('Date to view YYYY-MM-DD '
                                  '(press Enter for today): ')
    entries = diary_manager.read_entries(current_file)
    matches = diary_manager.filter_entries_by_date(entries, target_date)

    if not matches:
        print(f'No entries found for {target_date}.')
        return

    print(f'\nEntries for {target_date}:')
    for entry in matches:
        print(diary_manager.format_entry(entry))


def view_all_entries(current_file):
    """Print every entry in the current diary file."""
    entries = diary_manager.read_entries(current_file)

    if not entries:
        print('This diary file has no entries yet.')
        return

    print(f'\nAll entries ({len(entries)}):')
    for entry in entries:
        print(diary_manager.format_entry(entry))


def main():
    """Run the diary menu loop until the user quits."""
    try:
        current_file = diary_manager.prepare_diary_file(DEFAULT_DIARY_FILE)
    except OSError as e:
        print(f'Could not open the default diary file: {e}')
        return

    while True:
        print_menu(current_file)
        choice = input('Choose an option (1-5): ').strip()

        try:
            match choice:
                case '1':
                    add_entry(current_file)
                case '2':
                    view_entries_by_date(current_file)
                case '3':
                    view_all_entries(current_file)
                case '4':
                    current_file = select_diary_file(current_file)
                case '5':
                    print('Goodbye!')
                    break
                case _:
                    print('Invalid choice. Please enter a number from 1 to 5.')
        except OSError as e:
            print(f'File error: {e}')


if __name__ == '__main__':
    main()
