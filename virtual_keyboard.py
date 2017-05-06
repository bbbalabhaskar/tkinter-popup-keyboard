from Tkinter import *


class _PopupKeyboard(Toplevel):
    """
    A Top level instance that displays a keyboard that is attached to
    another widget. Only the Entry widget has a subclass in this version.
    """

    def __init__(self, parent, attach, x, y, keycolor, keysize=5):
        """
        Popup Keyboard
        :param parent: parent
        :param attach: is attached to
        :param x: x position
        :param y: y position
        :param keycolor: key color
        :param keysize: key size
        """
        Toplevel.__init__(self, takefocus=0)

        self.overrideredirect(True)
        self.attributes('-alpha', 0.85)

        self.parent = parent
        self.attach = attach
        self.keysize = keysize
        self.keycolor = keycolor
        self.x = x
        self.y = y

        self.normal_keys = Frame(self)
        self.normal_keys.pack(fill=BOTH)

        self.row0 = Frame(self.normal_keys)
        self.row1 = Frame(self.normal_keys)
        self.row2 = Frame(self.normal_keys)
        self.row3 = Frame(self.normal_keys)
        self.row4 = Frame(self.normal_keys)

        self.row0.grid(row=0)
        self.row1.grid(row=1)
        self.row2.grid(row=2)
        self.row3.grid(row=3)
        self.row4.grid(row=4, columnspan=5, sticky=W+E+N+S)

        self.shift_keys = Frame(self)
        self.s_row0 = Frame(self.shift_keys)
        self.s_row1 = Frame(self.shift_keys)
        self.s_row2 = Frame(self.shift_keys)
        self.s_row3 = Frame(self.shift_keys)
        self.s_row4 = Frame(self.shift_keys)

        self.s_row0.grid(row=0)
        self.s_row1.grid(row=1)
        self.s_row2.grid(row=2)
        self.s_row3.grid(row=3)
        self.s_row4.grid(row=4, columnspan=5, sticky=W+E+N+S)

        self._init_keys()

        # resize to fit keys
        self.update_idletasks()

        x = (self.winfo_screenwidth()-self.winfo_width()) / 2
        y = (self.winfo_screenheight()-self.winfo_height()) - 20

        self.geometry('{}x{}+{}+{}'.format(self.winfo_width(),
                                           self.winfo_height(),
                                           x, y))

    def _init_keys(self):
        self.alpha = {
            'row0': ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '<-'],
            'row1': ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
            'row2': ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'Enter'],
            'row3': ['Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
            'row4': ['Space']
        }

        self.shift_alpha = {
            'row0': ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '<-'],
            'row1': ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|'],
            'row2': ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Enter'],
            'row3': ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'],
            'row4': ['Space']
        }

        for row in self.alpha.iterkeys():  # iterate over dictionary of rows
            if row == 'row0':
                i = 1  # for readability and functionality
                for k in self.alpha[row]:
                    Button(self.row0,
                           text=k,
                           width=self.keysize,
                           bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                    i += 1
            if row == 'row1':  # TO-DO: re-write this method
                i = 1  # for readability and functionality
                for k in self.alpha[row]:
                    Button(self.row1,
                           text=k,
                           width=self.keysize,
                           bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                    i += 1
            elif row == 'row2':
                i = 2
                for k in self.alpha[row]:
                    Button(self.row2,
                           text=k,
                           width=self.keysize,
                           bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                    i += 1
            elif row == 'row3':
                i = 2
                for k in self.alpha[row]:
                    Button(self.row3,
                           text=k,
                           width=self.keysize,
                           bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                    i += 1
            elif row == 'row4':
                i = 3
                for k in self.alpha[row]:
                    Button(self.row4, text=k, width=self.keysize, bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).pack(fill=X)
                    i += 1

        for row in self.shift_alpha.iterkeys():  # iterate over dictionary of rows
            if row == 'row0':
                i = 1  # for readability and functionality
                for k in self.shift_alpha[row]:
                    Button(self.s_row0,
                           text=k,
                           width=self.keysize,
                           bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                    i += 1
            if row == 'row1':  
                i = 1  # for readability and functionality
                for k in self.shift_alpha[row]:
                    Button(self.s_row1,
                           text=k,
                           width=self.keysize,
                           bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                    i += 1
            elif row == 'row2':
                i = 2
                for k in self.shift_alpha[row]:
                    Button(self.s_row2,
                           text=k,
                           width=self.keysize,
                           bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                    i += 1
            elif row == 'row3':
                i = 2
                for k in self.shift_alpha[row]:
                    Button(self.s_row3,
                           text=k,
                           width=self.keysize,
                           bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                    i += 1
            elif row == 'row4':
                i = 3
                for k in self.shift_alpha[row]:
                    Button(self.s_row4, text=k, width=self.keysize, bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).pack(fill=X)
                    i += 1

    def destroy_popup(self):
        self.destroy()

    def _attach_key_press(self, k):
        if k == 'Space':
            self.attach.insert(END, ' ')

        elif k == 'Shift':
            if self.normal_keys.winfo_ismapped():
                self.normal_keys.pack_forget()
                self.shift_keys.pack(fill=BOTH)
            else:
                self.shift_keys.pack_forget()
                self.normal_keys.pack(fill=BOTH)

        elif k =='<-':
            self.attach.delete(len(self.attach.get())-1)

        elif k == 'Enter':
            self.attach.event_generate('<<Fout>>')

        else:
            self.attach.insert(END, k)


class KeyboardEntry(Frame):

    def __init__(self, parent, keysize=3, keycolor='white', *args, **kwargs):
        Frame.__init__(self, parent)
        self.parent = parent

        self.entry = Entry(self, *args, **kwargs)
        self.entry.pack()

        self.keysize = keysize
        self.keycolor = keycolor

        self.state = 'idle'

        self.entry.bind('<Button-1>', self._call_popup)
        self.entry.bind('<<Fout>>', self._destroy_popup)
        self.entry.bind('<FocusOut>', self._destroy_popup)

    def _call_popup(self, event):

        if (not hasattr(self, 'kb')) or (hasattr(self, 'kb') and self.kb is None):
            self.kb = _PopupKeyboard(attach=self.entry, parent=self.parent, x=self.entry.winfo_rootx(),
                                     y=self.entry.winfo_rooty() + self.entry.winfo_reqheight(), keysize=self.keysize,
                                     keycolor=self.keycolor)
        elif not hasattr(self, 'kb'):
            self.kb = _PopupKeyboard(attach=self.entry, parent=self.parent, x=self.entry.winfo_rootx(),
                                     y=self.entry.winfo_rooty() + self.entry.winfo_reqheight(), keysize=self.keysize,
                                     keycolor=self.keycolor)

    def _destroy_popup(self, event):
        if self.kb is not None:
            self.kb.destroy_popup()
        self.kb = None

    def get_text(self):
        return self.entry.get()


