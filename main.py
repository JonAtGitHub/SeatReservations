
import itertools
import random

NSEATS = 100
NRUNS = 10000

def pick_seat(seats):
    allseats = set(range(1,NSEATS+1))
    available = allseats.difference(seats)
    choice = random.choice(list(available))
    return choice

def runone(crazy):
    seats = {}
    for passenger in range(1, NSEATS+1):
        seat = passenger
        if passenger == crazy or seat in seats:
            seat = pick_seat(seats.keys())
        seats[seat] = passenger
    return seats[NSEATS] == NSEATS

hits = 0
runs = 0
for run in range(1, NRUNS+1):
    for crazy in range(1, NSEATS):
        runs += 1
        inseat = runone(crazy)
        if inseat:
            hits += 1
print(hits/runs)
