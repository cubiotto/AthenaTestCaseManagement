"""
SQL statements for Athena Test Case Management database initialization.
"""

# Table creation statements
CREATE_TABLES = [
    """
    CREATE TABLE IF NOT EXISTS test_cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        test_id TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        preconditions TEXT,
        test_steps TEXT,
        expected_result TEXT,
        priority TEXT DEFAULT 'Medium',
        status TEXT DEFAULT 'Active',
        category TEXT,
        tags TEXT,
        created_date TEXT NOT NULL,
        modified_date TEXT NOT NULL,
        created_by TEXT DEFAULT 'System',
        assigned_to TEXT
    )
    """,
    
    """
    CREATE TABLE IF NOT EXISTS test_executions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        test_case_id INTEGER NOT NULL,
        execution_date TEXT NOT NULL,
        result TEXT NOT NULL,
        notes TEXT,
        executed_by TEXT,
        execution_time INTEGER,
        environment TEXT,
        build_version TEXT,
        FOREIGN KEY (test_case_id) REFERENCES test_cases (id)
    )
    """,
    
    """
    CREATE TABLE IF NOT EXISTS test_suites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        description TEXT,
        created_date TEXT NOT NULL,
        created_by TEXT DEFAULT 'System'
    )
    """,
    
    """
    CREATE TABLE IF NOT EXISTS test_suite_cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        suite_id INTEGER NOT NULL,
        test_case_id INTEGER NOT NULL,
        sequence_order INTEGER DEFAULT 0,
        FOREIGN KEY (suite_id) REFERENCES test_suites (id),
        FOREIGN KEY (test_case_id) REFERENCES test_cases (id),
        UNIQUE(suite_id, test_case_id)
    )
    """,
    
    """
    CREATE TABLE IF NOT EXISTS defects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        defect_id TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        severity TEXT DEFAULT 'Medium',
        priority TEXT DEFAULT 'Medium',
        status TEXT DEFAULT 'Open',
        found_in_version TEXT,
        fixed_in_version TEXT,
        test_case_id INTEGER,
        created_date TEXT NOT NULL,
        created_by TEXT DEFAULT 'System',
        assigned_to TEXT,
        FOREIGN KEY (test_case_id) REFERENCES test_cases (id)
    )
    """
]

# Index creation statements
CREATE_INDEXES = [
    "CREATE INDEX IF NOT EXISTS idx_test_cases_test_id ON test_cases(test_id)",
    "CREATE INDEX IF NOT EXISTS idx_test_cases_status ON test_cases(status)",
    "CREATE INDEX IF NOT EXISTS idx_test_cases_priority ON test_cases(priority)",
    "CREATE INDEX IF NOT EXISTS idx_test_cases_category ON test_cases(category)",
    "CREATE INDEX IF NOT EXISTS idx_test_executions_test_case_id ON test_executions(test_case_id)",
    "CREATE INDEX IF NOT EXISTS idx_test_executions_result ON test_executions(result)",
    "CREATE INDEX IF NOT EXISTS idx_test_executions_date ON test_executions(execution_date)",
    "CREATE INDEX IF NOT EXISTS idx_defects_status ON defects(status)",
    "CREATE INDEX IF NOT EXISTS idx_defects_priority ON defects(priority)",
    "CREATE INDEX IF NOT EXISTS idx_test_suite_cases_suite_id ON test_suite_cases(suite_id)"
]

# Sample data insertion statements
SAMPLE_DATA = [
    """
    INSERT OR IGNORE INTO test_cases 
    (test_id, title, description, preconditions, test_steps, expected_result, 
     priority, category, tags, created_date, modified_date, created_by) 
    VALUES 
    ('TC-001', 'User Login - Valid Credentials', 
     'Test user login functionality with valid credentials',
     'User account exists in system',
     '1. Navigate to login page\n2. Enter valid username\n3. Enter valid password\n4. Click login button',
     'User should be logged in successfully and redirected to dashboard',
     'High', 'Authentication', 'login,authentication,smoke',
     datetime('now'), datetime('now'), 'System')
    """,
    
    """
    INSERT OR IGNORE INTO test_cases 
    (test_id, title, description, preconditions, test_steps, expected_result, 
     priority, category, tags, created_date, modified_date, created_by) 
    VALUES 
    ('TC-002', 'User Login - Invalid Password', 
     'Test user login functionality with invalid password',
     'User account exists in system',
     '1. Navigate to login page\n2. Enter valid username\n3. Enter invalid password\n4. Click login button',
     'Error message should be displayed and user should not be logged in',
     'High', 'Authentication', 'login,authentication,negative',
     datetime('now'), datetime('now'), 'System')
    """,
    
    """
    INSERT OR IGNORE INTO test_suites 
    (name, description, created_date, created_by) 
    VALUES 
    ('Smoke Test Suite', 'Critical functionality tests for smoke testing', 
     datetime('now'), 'System')
    """
]

# Complete initialization - combines all statements
ALL_STATEMENTS = CREATE_TABLES + CREATE_INDEXES + SAMPLE_DATA

# You can also create specific combinations
SCHEMA_ONLY = CREATE_TABLES + CREATE_INDEXES
TABLES_ONLY = CREATE_TABLES