
strategy = {
    "opponent": {
        "A": "rock",
        "B": "paper",
        "C": "scissors"
    },
    "response": {
        "X": "rock",
        "Y": "paper",
        "Z": "scissors"
    }
}

# [their_move][your_move]
results = {
    "rock": {
        "rock": "draw",
        "paper": "win",
        "scissors": "lose"
    },
    "paper": {
        "rock": "lose",
        "paper": "draw",
        "scissors": "win"
    },
    "scissors": {
        "rock": "win",
        "paper": "lose",
        "scissors": "draw"
    }
}

scoring = {
    "your_move": {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    },
    "result": {
        "win": 6,
        "draw": 3,
        "lose": 0
    }
}

def rps_outcome(their_move, your_move):
    return results[their_move][your_move]

with open('02/input.txt', 'r') as file:
    rps_input = file.read().strip()

score = 0

rounds = rps_input.split('\n')
for round in rounds:
    moves = round.split()
    their_move = strategy["opponent"][moves[0]]
    your_move = strategy["response"][moves[1]]

    result = results[their_move][your_move]
    round_score = scoring["your_move"][your_move] + scoring["result"][result]

    score += round_score

print(score)
