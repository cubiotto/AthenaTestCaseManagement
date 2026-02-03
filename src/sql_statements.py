"""
SQL statements for Athena Test Case Management database initialization.
"""

# Table creation statements
CREATE_TABLES = [
    """
    CREATE TABLE IF NOT EXISTS projects (
        project_id TEXT PRIMARY KEY,
        project_name TEXT NOT NULL,
    )
    """
]

# Index creation statements
CREATE_INDEXES = [

]

# Sample data insertion statements
SAMPLE_DATA = [
    """

    """,
    
    """

    """,
    
    """

    """
]

# Complete initialization - combines all statements
ALL_STATEMENTS = CREATE_TABLES + CREATE_INDEXES + SAMPLE_DATA

# You can also create specific combinations
SCHEMA_ONLY = CREATE_TABLES + CREATE_INDEXES
TABLES_ONLY = CREATE_TABLES