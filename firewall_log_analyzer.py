import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class FirewallLogAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Firewall Log Analyzer")
        
        self.log_data = None
        
        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self.root, text="Load Log File", command=self.load_log_file)
        self.load_button.pack(pady=10)

        self.display_button = tk.Button(self.root, text="Display Log", command=self.display_log)
        self.display_button.pack(pady=10)

        self.config_button = tk.Button(self.root, text="Set Configurations", command=self.set_configurations)
        self.config_button.pack(pady=10)

        self.log_text = tk.Text(self.root, wrap=tk.WORD, height=20, width=50)
        self.log_text.pack(pady=10)

    def load_log_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Log Files", "*.log"), ("All Files", "*.*")])
        if file_path:
            try:
                self.log_data = pd.read_csv(file_path, delimiter=' ', header=None)  # Adjust delimiter as needed
                messagebox.showinfo("Success", "Log file loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load log file: {e}")

    def display_log(self):
        if self.log_data is not None:
            self.log_text.delete(1.0, tk.END)  # Clear previous text
            self.log_text.insert(tk.END, self.log_data.to_string())
        else:
            messagebox.showwarning("Warning", "No log file loaded!")

    def set_configurations(self):
        # Placeholder for configuration settings
        messagebox.showinfo("Configurations", "Configuration settings can be set here.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FirewallLogAnalyzer(root)
    root.mainloop()
