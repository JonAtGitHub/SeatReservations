
import random

# number of passengers and seats
NUM = 100

# number of simulation runs
NRUNS = 100000

# used as both passenger and seat #
NRANGE = range(1, NUM+1)

# 0=random otherwise 50/50
CRAZY_MODE = 0

def pick_random_seat(seats_in_use):
    all_seats = set(NRANGE)
    available_seats = all_seats.difference(seats_in_use)
    seat = random.choice(list(available_seats))
    return seat

def pick_crazy_seat(crazy_assigned_seat, seats_in_use):
    if CRAZY_MODE == 0 or random.randrange(100) < 50:
        # pick any available seat
        seat = pick_random_seat(seats_in_use)
    else:
        # pick any available seat excluding crazy's seat
        all_seats = set(NRANGE)
        available_seats = all_seats.difference(seats_in_use)
        candidate_seats = available_seats.difference([crazy_assigned_seat])
        seat = random.choice(list(candidate_seats))
    return seat

def pick_seat(passenger, passenger_assigned_seat, crazy, crazy_assigned_seat, seats):
    if passenger_assigned_seat in seats:
        # seat occupied
        seat = pick_random_seat(seats.keys())
    elif passenger == crazy:
        # seat not occupied but passenger is crazy
        seat = pick_crazy_seat(crazy_assigned_seat, seats.keys())
    else:
        seat = passenger_assigned_seat
    return seat

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
        seat = pick_seat(passenger, assigned_seat[passenger], crazy, assigned_seat[crazy], seats)
        seats[seat] = passenger
        actual_seat[passenger] = seat
    
    # did last passenger get his assigned seat
    last_passenger = boarding_order[-1]
    assigned = assigned_seat[last_passenger]
    actual = actual_seat[last_passenger]
    return (assigned == actual, ) # a tuple in case more info desired in future

in_assigned = 0
runs = 0
for run in range(NRUNS):
    runs += 1
    results = runone()
    if results[0]:
        in_assigned += 1
print("{0}%".format(in_assigned*100/runs))
