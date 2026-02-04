#!/usr/bin/env python3
"""
Initialize the Athena Test Case Management database for the first time.
"""

from src.database import db_manager
from src.sql_statements import ALL_STATEMENTS, SCHEMA_ONLY, TABLES_ONLY

def initialize_database():
    """Initialize the database with current SQL statements."""
    print("Initializing Athena Test Case Management Database...")
    
    try:
        # Use ALL_STATEMENTS to create tables, indexes, and sample data
        db_manager.init_database(ALL_STATEMENTS)
        print("✓ Database initialized successfully!")
        
        # Verify the database was created
        result = db_manager.fetch_one("SELECT name FROM sqlite_master WHERE type='table' AND name='projects'")
        if result:
            print("✓ Projects table created successfully")
        else:
            print("✗ Projects table not found")
            
    except Exception as e:
        print(f"✗ Failed to initialize database: {e}")

if __name__ == "__main__":
    initialize_database()