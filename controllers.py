from models import Candidate


class ElectionController:
    def __init__(self):
        self.candidates = []
        self.voters = set()

    def add_candidate(self, name: str):     # Candidates
        self.candidates.append(Candidate(name))

    def record_vote(self, candidate_name: str, voter_id: str):      # Makes sure of Unique Voter ID
        if voter_id not in self.voters:
            self.vote_for_candidate(candidate_name)
            self.voters.add(voter_id)

    def check_voter(self, voter_id: str) -> bool:       # Checks to see if Voter has Voted Before
        return voter_id in self.voters

    def vote_for_candidate(self, candidate_name: str):      # Voting
        for candidate in self.candidates:
            if candidate.name == candidate_name:
                candidate.add_vote()
                return True
        return False

    def get_results(self) -> str:               # Results
        return "\n".join(f"{c.name}: {c.votes} votes" for c in self.candidates)

    def get_candidate_names(self) -> list:          # List of Candidates
        return [candidate.name for candidate in self.candidates]

    def reset_votes(self):      #Resets votes
        for candidate in self.candidates:
            candidate.votes = 0
        self.voters.clear()
