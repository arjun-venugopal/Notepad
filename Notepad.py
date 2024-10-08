import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button


class SimpleEditor:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title('Notepad') 
        self.file_path = None 

        # Creating Text widget
        self.text_area: Text = Text(self.root, wrap="word")
        self.text_area.pack(fill="both", expand=True)

        # Creating Frame
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        # Creating Save Button
        self.save_button: Button = Button(self.button_frame, text="Save", command=self.save_file)
        self.save_button.pack(side="left")

        # Creating Load Button
        self.load_button: Button = Button(self.button_frame, text="Load", command=self.load_file)
        self.load_button.pack(side="left")

    # Creating Save function
    def save_file(self) -> None:
        if not self.file_path:  
            self.file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])

        if self.file_path:  
            with open(self.file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            print(f"File saved at {self.file_path}")

    # Creating Load function
    def load_file(self) -> None:
        self.file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])
        if self.file_path: 
            with open(self.file_path, 'r') as file:
                content: str = file.read()
                self.text_area.delete(1.0, tk.END)  
                self.text_area.insert(tk.INSERT, content)
            print(f"File loaded from {self.file_path}")

    # Creating Run function
    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleEditor = SimpleEditor(root)
    app.run()


if __name__ == "__main__":
    main()
