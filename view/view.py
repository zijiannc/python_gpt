import tkinter as tk
from tkinter import ttk
from controller.nana_controller import NaNa_ChatController
from tkinter import scrolledtext


class ChatbotUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("NaNa")
        self.geometry("700x500")
        self.resizable(False, False)
        self.iconbitmap('assets\icon.png')
        self.controller = NaNa_ChatController(self)

        self.create_widgets()

    def create_widgets(self):
        self.conversation_frame = ttk.Frame(self)
        self.conversation_frame.pack(padx=10, pady=10)

        self.conversation = tk.Text(self.conversation_frame, wrap="word", state="disabled")
        self.conversation.pack(fill="both", expand=True)
        self.conversation = scrolledtext.ScrolledText(self.conversation_frame, wrap="word", state="disabled")


        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(padx=10, pady=10, fill="x")

        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(self.input_frame, textvariable=self.input_var)
        self.input_entry.pack(fill="x", expand=True)
        self.input_entry.bind("<Return>", self._send_message)

        self.send_button = ttk.Button(self.input_frame, text="Send", command=self._send_message)
        self.send_button.pack(ipadx=10)

        self.clear_button = ttk.Button(self.input_frame, text="Clear", command=self._clear_conversation)
        self.clear_button.pack(ipadx=10, side="left")  


    def display_user_message(self, message):
        self.conversation.configure(state="normal")
        self.conversation.insert("end", f"You: {message}\n")
        self.conversation.configure(state="disabled")

    def display_bot_message(self, message):
        self.conversation.configure(state="normal")
        self.conversation.insert("end", f"-------------------------------------------------------------------------------\n")
        self.conversation.insert("end", f"Bot: {message}\n")
        self.conversation.insert("end", f"===============================================================================\n")
        self.conversation.configure(state="disabled")
        self.conversation.see("end")


    def disable_input(self):
        self.input_var.set("")
        self.input_entry.configure(state="disabled")
        self.send_button.configure(state="disabled", text="Sending...")

    def enable_input(self):
        self.input_entry.configure(state="normal")
        self.send_button.configure(state="normal", text="Send")

    def _send_message(self, event=None):
        if event and event.state == 1:  # Shift key is being pressed
            self.input_entry.insert(tk.INSERT, '\n')
        else:
            user_message = self.input_var.get()
            self.controller.send_message(user_message)

    def _clear_conversation(self):
        self.conversation.configure(state="normal")
        self.conversation.delete("1.0", "end")
        self.conversation.configure(state="disabled")