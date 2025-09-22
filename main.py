
import itertools
import random

NSEATS = 100
NRUNS = 100000

def pick_seat(seats):
    allseats = set(range(1,NSEATS+1))
    available = allseats.difference(seats)
    choice = random.choice(list(available))
    return choice

def runone(crazy):
    boarding_order = list(range(1, NSEATS+1))
    random.shuffle(boarding_order)
    seats = {}
    for passenger in boarding_order:
        seat = passenger
        if passenger == crazy or seat in seats:
            seat = pick_seat(seats.keys())
        seats[seat] = passenger
    assigned = boarding_order[-1]
    return seats[assigned] == assigned

hits = 0
runs = 0
for run in range(1, NRUNS+1):
    crazy = random.choice(list(range(1, NSEATS+1)))
    runs += 1
    inseat = runone(crazy)
    if inseat:
        hits += 1
print("{0}%".format(hits*100/runs))
