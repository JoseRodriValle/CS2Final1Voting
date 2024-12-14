import tkinter as tk
from tkinter import simpledialog, messagebox
from controllers import ElectionController


class MainApplication(tk.Tk):
    def __init__(self, controller: ElectionController):
        super().__init__()
        self.controller = controller

        self.title('Voting System')
        self.geometry('300x200')

        tk.Label(self, text="Vote for a Candidate").pack()

        for candidate_name in controller.get_candidate_names():     # Grabs Candidate Names
            button = tk.Button(self, text=candidate_name,
                               command=lambda c=candidate_name: self.request_id_and_vote(c))
            button.pack()

        results_button = tk.Button(self, text="Show Results", command=self.show_results)        # Result Button
        results_button.pack()

        reset_button = tk.Button(self, text="Reset Votes", command=self.reset_votes)        # Reset Button
        reset_button.pack()

    def request_id_and_vote(self, candidate_name: str):
        voter_id = simpledialog.askstring("ID Check", "Enter your voter ID:")       # Input ID
        if voter_id and not self.controller.check_voter(voter_id):
            self.vote(candidate_name, voter_id)
        else:
            messagebox.showinfo("Vote", "You have already voted!")

    def vote(self, candidate_name: str, voter_id: str):         # Vote Confirmed Screen
        self.controller.record_vote(candidate_name, voter_id)
        messagebox.showinfo("Vote", f"Voted for {candidate_name}")

    def show_results(self):         # Result Screen
        results = self.controller.get_results()
        messagebox.showinfo("Results", results)

    def reset_votes(self):                  # Reset Screen
        self.controller.reset_votes()
        messagebox.showinfo("Reset", "The votes have been reset.")
