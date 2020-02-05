# change note
from tkinter import Tk, Label, Button, Frame, LEFT, RIGHT, TOP, BOTH, BOTTOM, N, Text, Menu, filedialog


class ChangeNote(object):

    def __init__(self, master):
        self.master = master
        master.title("Simple GUI")

        # menubar
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_command(label="Save as...", command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)

        # top area
        top_frame = Frame(master, height=100)
        top_frame.pack(side=TOP, fill=BOTH)

        # main area
        main_frame = Frame(master, bg="#eee", borderwidth=5)
        main_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)

        self.text = Text(main_frame, bg="#444", fg="#eee")
        self.text.configure(insertbackground='white')
        self.text.pack(expand=True, fill='both')

    def get_text(self):
        return self.text.get("1.0", 'end-1c')

    def new_file(self):
        pass

    def open_file(self):
        # TODO
        return True

    def open_template(self):
        # TODO
        pass

    def save(self):
        txt = self.get_text()
        file = open(self.path, 'w')
        file.write(txt)
        file.close()

    def save_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".xml",
            filetypes=(("xml file", "*.xml"), ("All Files", "*.*")))

        if not path:
            return False

        self.path = path
        self.save()
        return True

    def browse(self):
        # TODO
        pass

    def close_file(self):
        # TODO
        pass

    def main_form(self):
        # TODO
        pass


if __name__ == '__main__':
    root = Tk()
    change_note_app = ChangeNote(root)
    root.geometry("1024x768")
    root.mainloop()
