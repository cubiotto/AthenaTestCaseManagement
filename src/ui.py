import customtkinter as ctk

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
    # Logic for creating a new project
        print("Button clicked: Create New Project")
    pass

    def select_existing_project(self):
    # Logic for selecting an existing project
        print("Button clicked: Select Existing Project")
    pass
