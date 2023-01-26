from tkinter import *

TIME_TO_DELETE = 5000


class Application(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self)
        self.pack()

        self._after_id = None
        self.textarea = Text(self)
        self.textarea.pack()
        self.textarea.bind('<Key>', self.on_typing)

    def on_typing(self, event):
        if self._after_id is not None:
            self.after_cancel(self._after_id)

        self._after_id = self.after(TIME_TO_DELETE, self.erase_text)

    def erase_text(self):
        self.textarea.delete("1.0", "end")
