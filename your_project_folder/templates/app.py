from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Define suits and values (remove cards below 5)
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
points = {'J': 5, 'Q': 10, 'K': 15, 'A': 20, 'Q of Spades': 60}  # Points for face cards and Queen of Spades

# Create deck without cards below 5
def create_deck():
    return [(value, suit) for value in values for suit in suits]

# Deal 4 cards to each player (for the first bidding phase)
def deal_initial_cards():
    deck = create_deck()
    random.shuffle(deck)
    players = {f'Player {i+1}': [] for i in range(5)}
    
    # Deal 4 cards to each player
    for _ in range(4):
        for player in players:
            players[player].append(deck.pop())
    
    return players, deck

# Bidding logic
def bidding_phase():
    bid = 150
    return bid

# Select trump suit based on the highest bidder
def select_trump():
    trump_suit = random.choice(suits)
    return trump_suit

# Select friends (Queen of Spades and one more friend)
def select_friends():
    return [('Q', 'Spades'), ('A', 'Hearts')]  # Example selection

# Calculate points for a round based on the cards played
def calculate_points(cards_played):
    round_points = 0
    for card in cards_played:
        if card[0] in points:
            round_points += points[card[0]]
    return round_points

# Route to deal initial cards and return the result as JSON
@app.route('/deal')
def deal():
    players, deck = deal_initial_cards()
    return jsonify({'players': players, 'deck': deck})

# Route to simulate bidding
@app.route('/bid')
def bid():
    bid = bidding_phase()
    return jsonify({'highest_bid': bid})

# Route to select trump suit
@app.route('/trump')
def trump():
    trump_suit = select_trump()
    return jsonify({'trump_suit': trump_suit})

# Route to select friends
@app.route('/friends')
def friends():
    selected_friends = select_friends()
    return jsonify({'friends': selected_friends})

# Route to simulate a round and return points
@app.route('/play_round', methods=['POST'])
def play_round():
    cards_played = request.json['cards_played']  # Get cards played in the round
    round_points = calculate_points(cards_played)
    return jsonify({'round_points': round_points})

if __name__ == '__main__':
    app.run(debug=True)
