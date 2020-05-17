### Questions
1. On average, how many turns is a game of War?
2. How much does a player's skill in slapping influence the outcome
    of Egyptian Rat Tail?

### Answers
1. 607 +/- 499. This answer war calculated by simulating 10,000 games of war.
    Note that there is a high degree of variance. Simulating more games of war
    (1,000,000) did not affect the stdev or the mean at 609 +/- 499.


### Commands
To simulate 10,000 games of War run:
python simulate_many_games_of_war.py

To run unit tests, run the following command from the base directory:
python -m unittest discover -p "*test.py"
