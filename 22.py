import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from sklearn.model_selection import train_test_split

class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dataset Cleaner & Splitter")

        self.df = None

        # Buttons
        tk.Button(root, text="Load Dataset", command=self.load_data, width=25).pack(pady=10)
        tk.Button(root, text="Clean Data", command=self.clean_data, width=25).pack(pady=10)
        tk.Button(root, text="Split Data", command=self.split_data, width=25).pack(pady=10)

        self.status = tk.Label(root, text="No dataset loaded", fg="blue")
        self.status.pack(pady=10)

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.df = pd.read_csv(file_path)
            self.status.config(text=f"Loaded: {file_path}")

    def clean_data(self):
        if self.df is None:
            messagebox.showerror("Error", "Load dataset first!")
            return

        # Example cleaning:
        self.df.drop_duplicates(inplace=True)
        self.df.dropna(inplace=True)

        messagebox.showinfo("Success", "Data cleaned successfully!")

    def split_data(self):
        if self.df is None:
            messagebox.showerror("Error", "Load dataset first!")
            return

        try:
            train, test = train_test_split(self.df, test_size=0.2, random_state=42)

            # Save files
            train.to_csv("train.csv", index=False)
            test.to_csv("test.csv", index=False)

            messagebox.showinfo("Success", "Data split into train.csv and test.csv")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x250")
    app = DataApp(root)
    root.mainloop()