import sqlite3
import os
from typing import Optional

class DatabaseManager:
    def __init__(self, db_path: str = "data/test_cases.db"):
        """
        Initialize the database manager with connection setup only.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self._ensure_data_directory()

    def _ensure_data_directory(self):
        """Ensure the data directory exists."""
        db_dir = os.path.dirname(self.db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)

    def get_connection(self) -> sqlite3.Connection:
        """
        Get a database connection with proper configuration.
        
        Returns:
            sqlite3.Connection: Database connection with row factory enabled
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enable column access by name
        return conn

    def execute_query(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """
        Execute a SQL query and return the cursor.
        
        Args:
            query: SQL query string
            params: Query parameters
            
        Returns:
            sqlite3.Cursor: Query cursor
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()
        return cursor

    def fetch_one(self, query: str, params: tuple = ()) -> Optional[sqlite3.Row]:
        """
        Execute a query and fetch one result.
        
        Args:
            query: SQL query string
            params: Query parameters
            
        Returns:
            sqlite3.Row or None: Single result row
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        conn.close()
        return result

    def fetch_all(self, query: str, params: tuple = ()) -> list:
        """
        Execute a query and fetch all results.
        
        Args:
            query: SQL query string
            params: Query parameters
            
        Returns:
            list: List of result rows
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results

    def init_database(self, sql_statements: list = None):
        """
        Initialize the database by executing SQL statements.
        
        Args:
            sql_statements: List of SQL statements to execute (CREATE TABLE, INSERT, etc.)
        """
        if sql_statements is None:
            sql_statements = []
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            for statement in sql_statements:
                if statement.strip():  # Skip empty statements
                    cursor.execute(statement)
            conn.commit()
            print(f"Successfully executed {len(sql_statements)} SQL statements")
        except sqlite3.Error as e:
            conn.rollback()
            print(f"Database error: {e}")
            raise
        finally:
            conn.close()

    def close(self):
        """Close database connections (cleanup method)."""
        pass  # sqlite3 connections are managed automatically


# Singleton instance for easy import
db_manager = DatabaseManager()