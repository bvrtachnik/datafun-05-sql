import sqlite3
import pathlib
import pandas as pd

# Use pathlib to ensure correct file paths
ROOT_DIR = pathlib.Path(__file__).parent
db_file_path = ROOT_DIR.joinpath("project.db")
sql_file_path = ROOT_DIR.joinpath("sql", "create_tables.sql")
author_data_path = ROOT_DIR.joinpath("data", "authors.csv")
book_data_path = ROOT_DIR.joinpath("data", "books.csv")

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
        authors_df = pd.read_csv(author_data_path, encoding="utf-8")
        books_df = pd.read_csv(book_data_path, encoding="utf-8")
        with sqlite3.connect(db_path) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")

def main():
    paths_to_verify = [sql_file_path, author_data_path, book_data_path]
    verify_and_create_folders(paths_to_verify)
    
    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_file_path, author_data_path, book_data_path)

if __name__ == "__main__":
    main()
