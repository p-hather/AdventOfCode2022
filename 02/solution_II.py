
guide = {
    "moves": {
        "A": "rock",
        "B": "paper",
        "C": "scissors"
    },
    "result": {
        "X": "lose",
        "Y": "draw",
        "Z": "win"
    }
}

# [their_move][result]
strategy = {
    "rock": {
        "draw": "rock",
        "win": "paper",
        "lose": "scissors"
    },
    "paper": {
        "lose": "rock",
        "draw": "paper",
        "win": "scissors"
    },
    "scissors": {
        "win": "rock",
        "lose": "paper",
        "draw": "scissors"
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

with open('02/input.txt', 'r') as file:
    rps_input = file.read().strip()

score = 0

rounds = rps_input.split('\n')
for round in rounds:
    round_split = round.split()
    their_move = guide["moves"][round_split[0]]
    result = guide["result"][round_split[1]]
    your_move = strategy[their_move][result]

    round_score = scoring["result"][result] + scoring["your_move"][your_move]

    score += round_score

print(score)
