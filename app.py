import tkinter as tk
from tkinter import ttk
import sqlite3

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TEST Form")

        #Create labels and entry widgets
        self.label_name = ttk.Label(root, text="Name:")
        self.entry_name = ttk.Entry(root)

        self.label_age = ttk.Label(root, text="Age:")
        self.entry_age = ttk.Entry(root)

        self.label_company = ttk.Label(root, text="Company:")
        self.entry_company = ttk.Entry(root)

        #Create a combobox for state selection
        self.label_state = ttk.Label(root, text="State")
        self.state_var = tk.StringVar()
        self.state_combobox = ttk.Combobox(root, textvariable=self.state_var, values=self.get_state_list())

        #Create a button to submit the form
        self.submit_button = ttk.Button(root, text="Submit", command=self.submit_form)

        #Setup the layout using the grid geometry manager
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky="E")
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_age.grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.entry_age.grid(row=1, column=1, padx=10, pady=5)

        self.label_company.grid(row=2, column=0, padx=10, pady=5, sticky="E")
        self.entry_company.grid(row=2, column=1, padx=10, pady=5)

        self.label_state.grid(row=3, column=0, padx=10, pady=5, sticky="E")
        self.state_combobox.grid(row=3, column=1, padx=10, pady=5)

        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    def get_state_list(self):
        return [
            "Select State",
            "Alabama", "Alaska", "Arizona", "Arkansas", "California",
            "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
            "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
            "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
            "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
            "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
            "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
            "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
            "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
            "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming",
            "District of Columbia"
        ]
    def submit_form(self):
        #Fetch data from entry widgets and ComboBox
        name = self.entry_name.get()
        age = self.entry_age.get()
        company = self.entry_company.get()
        selected_state = self.state_var.get()

        # Update the database 
        self.update_database(name, age, company, selected_state)
        
        # #Testing UI, 
        # print(f"Name: {name}, Age: {age}, Company:{company}, State: {selected_state}")

    def update_database(self, name, age, company, selected_state):
        #Connect to the SQLite database (or create if not exist)
        connection = sqlite3.connect("data.db")

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        #Create a table if not exist
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       age INTEGER NOT NULL,
                       company TEXT NOT NULL,
                       selected_state TEXT NOT NULL
                       )
                       ''')
        
        # Insert data into the table
        cursor.execute('INSERT INTO users (name, age, company, selected_state) VALUES (?, ?, ?, ?)', (name, age, company, selected_state))

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

if __name__=="__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()