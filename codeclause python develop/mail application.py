import tkinter as tk
class TextEditor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.text = tk.Text()
        self.text.pack(side="top", fill="both", expand=True)
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=False)
        self.filemenu.add_command(label="New", command=self.new_file)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_command(label="Save As", command=self.save_as_file)
        self.filemenu.add_command(label="Close", command=self.close_file)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.editmenu = tk.Menu(self.menubar, tearoff=False)
        self.editmenu.add_command(label="Cut", command=self.cut)
        self.editmenu.add_command(label="Copy", command=self.copy)
        self.editmenu.add_command(label="Paste", command=self.paste)
        self.editmenu.add_command(label="Find", command=self.find)
        self.editmenu.add_command(label="Replace", command=self.replace)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.formatmenu = tk.Menu(self.menubar, tearoff=False)
        self.formatmenu.add_command(label="Font", command=self.change_font)
        self.formatmenu.add_command(label="Size", command=self.change_size)
        self.menubar.add_cascade(label="Format", menu=self.formatmenu)
        self.viewmenu = tk_font = tk.StringVar()
        sel_font.set("Arial")
        sel_size = tk.IntVar()
        sel_size.set(12)
        self.font_menu = tk.OptionMenu(self.menubar, sel_font, "Arial", "Helvetica", "Times New Roman", "Verdana")
        self.font_menu.config(font=("Arial", 12))
        self.font_menu.pack(side="left")
        self.size_menu = tk.OptionMenu(self.menubar, sel_size, 8, 10, 12, 14, 16, 18, 20)
        self.size_menu.pack(side="left")
        self.config(menu=self.menubar)
    def new_file(self):
        self.text.delete("1.0", "end")
    def open_file(self):
        file = tk.filedialog.askopenfile(mode="r", filetypes=[("All Files", "*.*")])
        if file:
            content = file.read()
            self.text.delete("1.0", "end")
            self.text.insert("1.0", content)
    def save_file(self):
        file = tk.filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("All Files", "*.*")])
        if file:
            content = self.text.get("1.0", "end-1c")
            file.write(content)
            file.close()
    def save_as_file(self):
        file = tk.filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("All Files", "*.*")])
        if file:
            content = self.text.get("1.0", "end-1c")
            file.write(content)
            file.close()
    def close_file(self):
        pass
    def cut(self):
        pass
    def copy(self):
        pass
    def paste(self):
        pass
    def find(self):
        pass
    def replace(self):
        pass
    def change_font(self):
        pass
    def change_size(self):
        pass
root = tk.Tk()
root.title("Text Editor")