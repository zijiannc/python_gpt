import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from controller.wise_group_controller import WiseGroupChatController

import os
import sys

class WiseGroupChatbotUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("讨论组")
        self.geometry("800x900")
        self.resizable(False, False)
        self.iconbitmap(self.resource_path("assets\dog_icon_215212.ico"))
        self.controller = WiseGroupChatController(self)

        self.create_widgets()

    def create_widgets(self):
        self.conversation_frame = ttk.Frame(self)
        self.conversation_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.conversation = scrolledtext.ScrolledText(self.conversation_frame, wrap="word", state="disabled")
        self.conversation.pack(fill="both", expand=True)
        self.conversation.tag_configure("gray", foreground="gray")
        self._add_message_to_conversation("请你输入你想问的问题,软件设置的讨论组会根据你提出的问题进行讨论,并不会直接回答...","gray")

        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(padx=10, pady=10, fill="x")

        self.input_var = tk.StringVar()
        self.input_entry = tk.Text(self.input_frame, height=10, wrap="word")

        self.input_entry.configure(spacing1=2, spacing2=2, spacing3=0.5)
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
        self.conversation.insert("end", f"讨论组:\n{message}\n")
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
        self.input_entry.insert(tk.INSERT, '')

    def _add_message_to_conversation(self, message, tag=None):
        self.conversation.configure(state="normal")
        if tag:
            self.conversation.insert("end", message + "\n", tag)
        else:
            self.conversation.insert("end", message + "\n")
        self.conversation.configure(state="disabled")
        self.conversation.see("end")


    def resource_path(self,relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)