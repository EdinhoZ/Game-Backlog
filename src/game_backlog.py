import tkinter as tk
from linked_list import LinkedList

class GameBacklog(tk.Tk):
    def __init__(self):
        super().__init__()
        self.games = LinkedList()
        self.title("Game Backlog")
        self.geometry("800x600")

        self.add_game_button = tk.Button(self, text="Add Game", command=self.add_game)
        self.check_backlog_button = tk.Button(self, text="Check Backlog", command=self.check_backlog)
        self.exit_button = tk.Button(self, text="Exit", command=exit)

        self.add_game_button.pack()
        self.check_backlog_button.pack()
        self.exit_button.pack()

    def add_game(self):
        add_game_window = tk.Toplevel(self)
        add_game_window.title("Add Game")
        add_game_window.geometry("400x300")

        label = tk.Label(add_game_window, text="Enter game name:")
        label.pack()

        entry = tk.Entry(add_game_window)
        entry.pack()

        def submit_game():
            game_name = entry.get()
            if game_name:
                self.games.add_node(game_name)
            add_game_window.destroy()  # Close the dialog

        button = tk.Button(add_game_window, text="Submit", command=submit_game)
        button.pack()

    def check_backlog(self):
        check_backlog_window = tk.Toplevel(self)
        check_backlog_window.title("Backlog")
        check_backlog_window.geometry("400x300")

        backlog_list = tk.Listbox(check_backlog_window)
        backlog_list.pack(expand=True)

        backlog_list.delete(0, tk.END)
        current = self.games.head
        while current:
            backlog_list.insert(tk.END, current.data)
            current = current.next

    def exit(self):
        self.destroy()