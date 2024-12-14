import json
from models import Candidate


def save_data(controller):      # Saves Data in a JSON File
    with open('vote_data.json', 'w') as file:
        data = {
            'candidates': {candidate.name: candidate.votes for candidate in controller.candidates},
            'voters': list(controller.voters)
        }
        json.dump(data, file)


def load_data(controller):      # Loads JSON File
    try:
        with open('vote_data.json', 'r') as file:
            data = json.load(file)
            controller.candidates.clear()
            controller.voters = set(data['voters'])
            for name, votes in data['candidates'].items():
                candidate = Candidate(name)
                candidate.votes = votes
                controller.candidates.append(candidate)
    except FileNotFoundError:
        pass
