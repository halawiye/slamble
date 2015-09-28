from classes import *
from random import choice
import statistics

NUM_PLAYERS = 6
NUM_ROUNDS = 10000
VERBOSE = False

players = deque()
for i in range(NUM_PLAYERS):
    players.appendleft(Player())

deck = Deck()

for i in range(deck.size()):
    next = deck.next()
    players[-1].dealt(next)
    players.rotate(1)
players.reverse()

slams = []
for i in range(NUM_ROUNDS):
    if VERBOSE: print("ROUND ",i + 1)
    count = 0
    slam = 0
    cards = deque()
    while(slam == 0):
        try:
            cards.appendleft(players[-1].next())
        except IndexError:
            players.rotate(1)
            continue
        if VERBOSE: print(str(cards[0]))
        count += 1
        if cards[0].value.value == ((count-2) % 13) + 1 or cards[0].value.value == (count % 13) + 1:
            slam += 1
        if count > 1 and cards[0].value == cards[1].value:
            slam += 1
        if count > 2 and cards[0].value == cards[2].value:
            slam += 1
        if cards[0].value.value == 1:
            slam = 2
        players.rotate(1)
    if VERBOSE: print(slam," handed slam")
    slams.append((count,slam,cards[0]))
    loser = choice(players)
    loser.pickUp(cards)
    players.rotate(len(players) - 1 - players.index(loser))
    
print("number of rounds: ",NUM_ROUNDS)
round_lengths = [x[0] for x in slams]
length_freq = [0 for x in range(max(round_lengths))]
length_cumfreq = [0 for x in range(max(round_lengths))]
for l in round_lengths:
    length_freq[l-1] += 1
    for i in range(l):
        length_cumfreq[i] += 1
print("average round length: ",statistics.mean(round_lengths)," cards")
print("average number of hands (per person): ",statistics.mean([x[1] for x in slams])," hands")
slam_values = [x[2].value for x in slams]
for value in Value:
    freq = slam_values.count(value)
    print(value.name,": ", freq," slams (", float(100*freq/NUM_ROUNDS),"%)")
    
for i in range(10):
    print("probability of slam in round ", i+1,": ",float(length_freq[i]/NUM_ROUNDS))

        

    
