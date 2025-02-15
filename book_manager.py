# Import from Python Standard Library first
import sqlite3
import pathlib

# Import from external packages
import pandas as pd

# Define paths using joinpath with correct folder structure
ROOT_DIR = pathlib.Path(__file__).parent  # Root directory of the project
db_file_path = ROOT_DIR.joinpath("project.db")  # Database in the root folder
sql_file_path = ROOT_DIR.joinpath("sql_create", "02_create_tables.sql")  # Correct SQL create path
author_data_path = ROOT_DIR.joinpath("data", "authors.csv")  # CSV file (optional)
book_data_path = ROOT_DIR.joinpath("data", "books.csv")  # CSV file (optional)

def verify_and_create_folders(paths):
    """Verify and create folders if they don't exist."""
    for path in paths:
        folder = path.parent
        if not folder.exists():
            print(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
        else:
            print(f"Folder already exists: {folder}")

def create_database(db_path):
    """Create a new SQLite database file if it doesn't exist."""
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")

def create_tables(db_path, sql_file_path):
    """Read and execute SQL statements to create tables."""
    if not sql_file_path.exists():
        print(f"Error: SQL file not found: {sql_file_path}")
        return

    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def insert_data_from_csv(db_path, author_data_path, book_data_path):
    """Read data from CSV files and insert the records into their respective tables."""
    if not author_data_path.exists() or not book_data_path.exists():
        print("Error: One or both CSV files are missing.")
        return

    try:
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_path) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")

def main():
    paths_to_verify = [sql_file_path]  # Only verify SQL path (CSV files removed)
    verify_and_create_folders(paths_to_verify)
    
    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)

if __name__ == "__main__":
    main()
