import customtkinter as ctk

# 1. Global Settings
ctk.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class TCMApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 2. Window Setup
        self.title("ATHENA Test Case Manager")
        self.geometry("1000x600")

        # 3. Grid Layout Configuration
        # We split the window into 2 columns: 
        # Column 0 is the Sidebar (narrow), Column 1 is the Main Area (wide)
        self.grid_columnconfigure(0, weight=0)  # Sidebar fixed width
        self.grid_columnconfigure(1, weight=1)  # Main area expands
        self.grid_rowconfigure(0, weight=1)     # Full height

        self.setup_sidebar()
        self.setup_main_view()

    def setup_sidebar(self):
        """Creates the navigation panel on the left."""
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        # App Logo / Title
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="TCM Tool", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Navigation Buttons
        self.btn_dashboard = ctk.CTkButton(self.sidebar_frame, text="All Test Cases", command=self.dummy_action)
        self.btn_dashboard.grid(row=1, column=0, padx=20, pady=10)

        self.btn_settings = ctk.CTkButton(self.sidebar_frame, text="Settings", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.btn_settings.grid(row=2, column=0, padx=20, pady=10)

    def setup_main_view(self):
        """Creates the main content area on the right."""
        # Main Container
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent") # Transparent = uses window background
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        # -- Header Section (Title + Buttons) --
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_frame.pack(fill="x", pady=(0, 20))

        self.lbl_title = ctk.CTkLabel(self.header_frame, text="Project: My First Test", font=ctk.CTkFont(size=24, weight="bold"))
        self.lbl_title.pack(side="left")

        # Action Buttons (Right aligned)
        self.btn_add = ctk.CTkButton(self.header_frame, text="+ New Test Case", fg_color="#2CC985", hover_color="#26AB72")
        self.btn_add.pack(side="right", padx=10)
        
        self.btn_import = ctk.CTkButton(self.header_frame, text="Import Excel", fg_color="#3B8ED0")
        self.btn_import.pack(side="right")

        # -- The Test Case List (Scrollable) --
        # We use a ScrollableFrame to hold our list of test cases
        self.scroll_frame = ctk.CTkScrollableFrame(self.main_frame, label_text="Test Cases List")
        self.scroll_frame.pack(fill="both", expand=True)

        # Let's add some "Fake" data so you can see what it looks like
        for i in range(1, 15): 
            self.create_test_row(i, f"Verify login functionality - Case {i}", "High", "Pending")

    def create_test_row(self, t_id, title, priority, status):
        """Helper to draw a single row for a test case."""
        # A row is just a Frame with labels inside
        row_frame = ctk.CTkFrame(self.scroll_frame)
        row_frame.pack(fill="x", pady=2)

        # ID Label
        ctk.CTkLabel(row_frame, text=f"#{t_id}", width=50).pack(side="left", padx=10)
        # Title Label
        ctk.CTkLabel(row_frame, text=title, anchor="w").pack(side="left", fill="x", expand=True, padx=10)
        # Status Label (Colored badge logic could go here)
        ctk.CTkLabel(row_frame, text=status, width=100).pack(side="right", padx=10)
        # Priority Label
        ctk.CTkLabel(row_frame, text=priority, width=80, text_color="orange").pack(side="right", padx=10)

    def dummy_action(self):
        print("Button clicked!")