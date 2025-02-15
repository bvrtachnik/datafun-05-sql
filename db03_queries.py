import sqlite3
import pathlib
import pandas as pd

def execute_sql_file(db_path, sql_file_path):
    """Executes SQL queries from a file and prints SELECT results in a formatted table."""
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, 'r') as file:
                sql_script = file.read()
            
            cursor = conn.cursor()
            queries = sql_script.strip().split(";")  # Split multiple queries
            
            print(f"\nExecuting queries from: {sql_file_path.name}\n")

            for query in queries:
                query = query.strip()
                if not query:
                    continue  # Skip empty queries
                
                print(f"Executing query:\n{query}\n")  # Debugging output
                try:
                    cursor.execute(query)

                    # If it's a SELECT query, fetch and display results
                    if query.upper().startswith("SELECT"):
                        rows = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description] if cursor.description else []

                        if rows:
                            df = pd.DataFrame(rows, columns=columns)
                            print("\nQuery Output:\n")
                            print(df.to_string(index=False))  # Neatly print table
                        else:
                            print("No results found.")

                        print("-" * 80)  # Separator for clarity
                
                except sqlite3.Error as e:
                    print(f"Error executing query: {e}")
                    print(f"Query: {query}")

            conn.commit()
    except sqlite3.Error as e:
        print(f"Error executing {sql_file_path.name}: {e}")

def main():
    ROOT_DIR = pathlib.Path(__file__).parent
    DB_PATH = ROOT_DIR.joinpath("project.db")  # Ensure correct path to database
    SQL_QUERIES_DIR = ROOT_DIR.joinpath("sql_queries")
    
    sql_files = [
        "query_aggregation.sql",
        "query_filters.sql",
        "query_group_by.sql",
        "query_join.sql",
        "query_sorting.sql"
    ]
    
    print("\nExecuting SQL Queries...\n")
    for sql_file in sql_files:
        sql_file_path = SQL_QUERIES_DIR.joinpath(sql_file)
        if sql_file_path.exists():
            print(f"Found SQL file: {sql_file_path}")
            execute_sql_file(DB_PATH, sql_file_path)
        else:
            print(f"Error: SQL file not found: {sql_file_path}")
    
    print("\nAll queries executed successfully!")

if __name__ == "__main__":
    main()
