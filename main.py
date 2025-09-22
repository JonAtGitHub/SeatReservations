
import itertools
import random

NSEATS = 100
NRUNS = 100000

def pick_seat(seats):
    allseats = set(range(1,NSEATS+1))
    available = allseats.difference(seats)
    choice = random.choice(list(available))
    return choice

def runone():
    boarding_order = list(range(1, NSEATS+1))
    random.shuffle(boarding_order)
    possible_crazy = boarding_order[:len(boarding_order)-1] # can't be last to board
    crazy = random.choice(possible_crazy)
    seats = {}
    for passenger in boarding_order:
        seat = passenger
        if passenger == crazy or seat in seats:
            seat = pick_seat(seats.keys())
        seats[seat] = passenger
    assigned = boarding_order[-1]
    return (seats[assigned] == assigned, ) # a tuple in case more info desired in future

in_assigned = 0
runs = 0
for run in range(0, NRUNS):
    runs += 1
    results = runone()
    if results[0]:
        in_assigned += 1
print("{0}%".format(in_assigned*100/runs))
