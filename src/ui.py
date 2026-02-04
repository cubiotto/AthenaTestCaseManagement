import customtkinter as ctk
from src.database import db_manager
from src.sql_statements import ALL_STATEMENTS

# 1. Global Settings
ctk.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class TCMApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 2. Window Setup
        self.title("ATHENA Test Case Manager")
        self.geometry("1080x1920")

        # 3. Grid Layout Configuration
        # We split the window into 2 columns: 
        # Column 0 is the Sidebar (narrow), Column 1 is the Main Area (wide)
        self.grid_columnconfigure(0, weight=0)  # Sidebar fixed width
        self.grid_columnconfigure(1, weight=1)  # Main area expands
        self.grid_rowconfigure(0, weight=1)     # Full height

        # 4. Home Page Setup
        self.home_frame = ctk.CTkFrame(self)
        self.home_frame.grid(row=0, column=1, sticky="nsew")

        self.title_label = ctk.CTkLabel(self.home_frame, text="Athena Test Case Manager", font=("Arial", 24))
        self.title_label.pack(pady=20)

        self.new_project_button = ctk.CTkButton(self.home_frame, text="Create New Project", command=self.create_new_project)
        self.new_project_button.pack(pady=10)

        self.existing_project_button = ctk.CTkButton(self.home_frame, text="Select Existing Project", command=self.select_existing_project)
        self.existing_project_button.pack(pady=10)

    def create_new_project(self):
        # Create a new top-level window
        new_window = ctk.CTkToplevel(self)
        new_window.title("Create New Project")
        new_window.geometry("800x600")
        new_window.attributes("-topmost", True)
        new_window.grid_columnconfigure(0, weight=1)
        new_window.grid_columnconfigure(1, weight=1)

        # Add title label
        label = ctk.CTkLabel(new_window, text="Enter Project Details:", font=("Arial", 16))
        label.pack(pady=20)

        # Project ID row frame
        project_id_frame = ctk.CTkFrame(new_window, fg_color="transparent")
        project_id_frame.pack(pady=10, padx=50, fill="x")
        project_id_frame.grid_columnconfigure(1, weight=1)
        
        project_id_entry_label = ctk.CTkLabel(project_id_frame, text="Project ID:", font=("Arial", 14))
        project_id_entry_label.grid(row=0, column=0, padx=(0, 20), sticky="w")
        project_id_entry = ctk.CTkEntry(project_id_frame, width=300)
        project_id_entry.grid(row=0, column=1, sticky="ew")

        # Project Name row frame
        project_name_frame = ctk.CTkFrame(new_window, fg_color="transparent")
        project_name_frame.pack(pady=10, padx=50, fill="x")
        project_name_frame.grid_columnconfigure(1, weight=1)
        
        project_name_entry_label = ctk.CTkLabel(project_name_frame, text="Project Name:", font=("Arial", 14))
        project_name_entry_label.grid(row=0, column=0, padx=(0, 20), sticky="w")
        project_name_entry = ctk.CTkEntry(project_name_frame, width=300)
        project_name_entry.grid(row=0, column=1, sticky="ew")
        
        # Add create button
        create_button = ctk.CTkButton(new_window, text="Create", 
                                       command=lambda: self.handle_project_creation(project_id_entry.get(), project_name_entry.get(), new_window))
        create_button.pack(pady=20)
    
    def handle_project_creation(self, project_id, project_name, window):
        # Logic to handle project creation
        if project_id.strip() and project_name.strip():
            try:
                # Initialize database if needed
                db_manager.init_database(ALL_STATEMENTS)
                
                # Insert the new project
                db_manager.execute_query(
                    "INSERT OR IGNORE INTO projects (project_id, project_name) VALUES (?, ?)",
                    (project_id.strip(), project_name.strip())
                )
                
                print(f"Creating project: {project_id} - {project_name}")
                window.destroy()
                
                # You can add logic here to switch to the main project view
                
            except Exception as e:
                print(f"Error creating project: {e}")
        else:
            print("Both Project ID and Project Name are required")

    def select_existing_project(self):
    # Logic for selecting an existing project
        print("Button clicked: Select Existing Project")
    pass
