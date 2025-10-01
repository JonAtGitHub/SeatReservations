Puzzle from AJS (source unkownd):

There are 100 passengers waiting in line to board an airliner with 100 passenger seats.
The seats are numbered from 1 to 100.
Each passenger holds a ticket with his seat number.
You are the last passenger in line.
One of the passengers ahead of you in line is crazy.
We don’t know which one. He will ignore his seat assignment and sit in a random empty seat.
Every other passenger will sit in their assigned seat — unless it is already taken, 
in which case they too will sit in a random empty passenger seat.
Passengers board one by one.
What is the probability that you will sit in your assigned seat?
NOTE: The crazy person might sit in his assigned seat; he is equally likely to sit in any other open seat.

Added note: boarding order is random.

Solution from AJS:

If C is crazy, and N is normal and Y is you, then there only 4 possible outcomes:

NOTE  1: If a Crazy ever takes his own seat  You WIN your seat.
NOTE  2: If a Crazy ever takes your seat  You LOSE your seat.
NOTE  3: If a Crazy takes anyone else's seat, they become a new Crazy.
NOTE  4: Any time 3 happens, there's one less person in front of you.

Because of NOTE 4, eventually there are only 3 people left (a C, an N and You) and only 4 possible cases:

CASE 1. C takes his own seat  You WIN your seat. See NOTE 1.
CASE 2. C takes your seat: You LOSE your seat. See NOTE 2. 

If neither of the above cases happens, only a New Crazy and You will be left. See NOTES 3 and 4. 

CASE 3. C took the N's seat and that N (now a new C)  takes the previous C's seat.  You WIN your seat.
CASE 4. C took the N's seat and that N (now a new C) takes your seat,  You LOSE your seat.

Two WINs and Two LOSSES! A 50% chance your seat will be the last chosen.

