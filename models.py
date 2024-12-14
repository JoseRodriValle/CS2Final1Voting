class Candidate:            # Candidates
    def __init__(self, name: str):
        self.name = name
        self.votes = 0

    def add_vote(self):     # Adds a vote
        self.votes += 1

