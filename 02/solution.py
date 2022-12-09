
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
    input = file.read().strip()

rounds = input.split('\n')


############
## Part 1 ##
############

guide = {
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
strategy = {
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

score = 0

for round in rounds:
    moves = round.split()
    their_move = guide["opponent"][moves[0]]
    your_move = guide["response"][moves[1]]

    result = strategy[their_move][your_move]
    round_score = scoring["your_move"][your_move] + scoring["result"][result]

    score += round_score

print(score)


############
## Part 2 ##
############

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

score = 0

for round in rounds:
    round_split = round.split()
    their_move = guide["moves"][round_split[0]]
    result = guide["result"][round_split[1]]
    your_move = strategy[their_move][result]

    round_score = scoring["result"][result] + scoring["your_move"][your_move]

    score += round_score

print(score)
