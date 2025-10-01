
import random

# number of passengers and seats
NSEATS = 100

# number of simulation runs
NRUNS = 100000

# used as both passenger and seat #
NRANGE = range(1, NSEATS+1)

def pick_seat(seats_in_use):
    all_seats = set(NRANGE)
    available_seats = all_seats.difference(seats_in_use)
    choice = random.choice(list(available_seats))
    return choice

def runone():
    # assign seats (indexed by passenger #)
    assigned_seats = list(NRANGE)
    random.shuffle(assigned_seats)
    assigned_seat = {}
    actual_seat = {}
    for passenger in NRANGE:
        assigned_seat[passenger] = assigned_seats[passenger-1]

    # determine boarding order
    boarding_order = list(NRANGE)
    random.shuffle(boarding_order)

    # pick the crazy (can't be last to board)
    possible_crazy = boarding_order[:len(boarding_order)-1]
    crazy = random.choice(possible_crazy)

    # board the passengers
    seats = {} # indexed by seat #
    for passenger in boarding_order:
        seat = assigned_seat[passenger]
        if passenger == crazy or seat in seats:
            seat = pick_seat(seats.keys())
        seats[seat] = passenger
        actual_seat[passenger] = seat
    
    # did last passenger get his assigned seat
    last_passenger = boarding_order[-1]
    assigned = assigned_seat[last_passenger]
    actual = actual_seat[last_passenger]
    return (assigned == actual, ) # a tuple in case more info desired in future

in_assigned = 0
runs = 0
for run in range(0, NRUNS):
    runs += 1
    results = runone()
    if results[0]:
        in_assigned += 1
print("{0}%".format(in_assigned*100/runs))
