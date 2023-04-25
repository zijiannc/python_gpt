import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from controller.nana_controller import NaNa_ChatController

import os
import sys

class ChatbotUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("NaNa")
        self.geometry("700x550")
        self.resizable(False, False)
        self.iconbitmap(self.resource_path("assets\dog_icon_215212.ico"))
        self.controller = NaNa_ChatController(self)

        self.create_widgets()

    def create_widgets(self):
        self.conversation_frame = ttk.Frame(self)
        self.conversation_frame.pack(padx=10, pady=10)

        self.conversation = scrolledtext.ScrolledText(self.conversation_frame, wrap="word", state="disabled")
        self.conversation.pack(fill="both", expand=True)

        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(padx=10, pady=10, fill="x")

        self.input_var = tk.StringVar()
        self.input_entry = tk.Text(self.input_frame, height=5, wrap="word")

        self.input_entry.pack(fill="x", expand=True)
        self.input_entry.bind("<Return>", self._send_message)
        self.input_entry.bind("<Shift-Return>", self._insert_newline)


        self.send_button = ttk.Button(self.input_frame, text="Send", command=self._send_message)
        self.send_button.pack(side="right", padx=(0, 5),pady=(5, 5))

        self.clear_button = ttk.Button(self.input_frame, text="Clear", command=self._clear_conversation)
        self.clear_button.pack(side="left", padx=(5, 0),pady=(5, 5))

    def display_user_message(self, message):
        self.conversation.configure(state="normal")
        self.conversation.insert("end", f"You: {message}\n")
        self.conversation.configure(state="disabled")

    def display_bot_message(self, message):
        self.conversation.configure(state="normal")
        self.conversation.insert("end", f"-------------------------------------------------------------------------------\n")
        self.conversation.insert("end", f"NaNa: {message}\n")
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
            user_message = self.input_entry.get("1.0", "end").strip()
            if user_message:
                self.controller.send_message(user_message)
            self.input_entry.configure(state="normal")
            self.input_entry.delete("1.0", "end")
            self.input_entry.configure(state="disabled")
            self.conversation.see("end")


    def _clear_conversation(self):
        self.conversation.configure(state="normal")
        self.conversation.delete("1.0", "end")
        self.conversation.configure(state="disabled")


    def _insert_newline(self, event=None):
        self.input_entry.insert(tk.INSERT, '\n')

    def resource_path(self,relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)