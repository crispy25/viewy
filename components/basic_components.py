from tkinter import font, ttk, StringVar, Text, END
from tkinterweb import HtmlFrame

class VLabel(ttk.Label):
    def __init__(self, master, key, value, link, **kw):
        super().__init__(master, **kw)
        self.key = key
        self.value = value
        self.link = link
        
    def pack(self, **kw) -> None:
        super().pack(**kw)

class VConfig(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.btn = ttk.Button(master=self, text='Config', command=master.config_text.show_config_text)
        self.btn.pack(side='left')

        self.version = ttk.Label(master=self, text='    v0.1    ')
        self.version.pack(side='right')

        s = StringVar()
        self.font_choice = ttk.Combobox(self, width=20, height=10, textvariable=s, state='readonly')
        self.font_choice["values"] = font.families()
        self.font_choice.pack(side='right')
        self.font_choice.current(0)

        def change_font() -> None:
            self.master.custom_font.configure(family=s.get())
            if self.master.main_frame.selection:
                new_font = self.master.custom_font.copy()
                new_font.config(underline=True)
                self.master.main_frame.selection.config(font=new_font)

        self.font_choice.bind("<<ComboboxSelected>>", lambda event: change_font())

        self.save_button = ttk.Button(master=self, text='Save', command=master.config_text.save)
        self.save_button_showing = False

        self.pack(side='bottom', fill='both')

    def show_save_button(self) -> None:
        self.save_button_showing = not self.save_button_showing
        if self.save_button_showing:
            self.save_button.pack(side='left')
        else:
            self.save_button.forget()

class VConfigText(Text):
    def __init__(self, master, font, bg='#0d0a03', fg='#10e84b', padx=40, pady=40, borderwidth=3, border=4, selectforeground='#e0ffe3', insertbackground="#00db15", insertwidth=2):
        super().__init__(master, fg=fg, bg=bg, font=font, padx=padx, borderwidth=borderwidth, border=border, selectforeground=selectforeground, insertbackground=insertbackground, insertwidth=insertwidth)

        self.text = ''
        with open("utils/vconfig_file.txt") as file:
            self.text = file.read()
        self.insert(END, self.text)
        self.text_showing = False

    def show_config_text(self) -> None:
        self.text_showing = not self.text_showing
        if self.text_showing:
            self.tkraise()
            self.pack(side='bottom', fill='x', expand=False)
        else:
            self.forget()

        self.master.config_bar.show_save_button()

    def save(self) -> None:
        self.text = self.get("1.0",'end-1c')
        self.master.update_main_frame(self.text)

        with open("utils/vconfig_file.txt", "w+") as file:
            file.write(self.text)

class VMainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Style().configure('TFrame', background = 'black')
        self.pack(anchor='center', fill='both', expand=True)
    
        self.labels_frame = ttk.Frame(self)
        self.labels_frame.pack(side='left', padx=20, anchor='center')

        self.web_frame = HtmlFrame(self, messages_enabled = False)
        self.web_frame.pack(side='left', fill='both', expand=True, padx=100, pady=40)

        self.selection = None
        self.labels = {}
    
    def update(self, labels: dict) -> None:
        key = None
        if self.selection:
            key = self.selection.key

        self.selection = None

        for label in self.labels.values():
            label.destroy()

        [label.pack(anchor='w') for label in labels.values()]
        self.labels = labels

        if key:
            self.select(key)

    def select(self, key) -> None:
        if key in self.labels.keys():
            if self.selection:
                self.selection.config(font=self.master.custom_font)

            self.selection = self.labels.get(key)
            new_font = self.master.custom_font.copy()
            new_font.config(underline=True)
            self.selection.config(font=new_font)
            self.web_frame.load_website(self.selection.link)
            self.web_frame.pack(side='left', fill='both', expand=True, padx=100, pady=40)
