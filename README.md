### Questions
1. On average, how many turns is a game of War?
2. How much does a player's skill in slapping influence the outcome
    of Egyptian Rat Tail?

### Answers
1. 607 +/- 499. This answer war calculated by simulating 10,000 games of war.
    Note that there is a high degree of variance. Simulating more games of war
    (1,000,000) did not affect the stdev or the mean at 609 +/- 499.
2. A player's skill has a very large effect on the outcome; however skill isn't always enough to win. Even when player A has a 0 percent chance at winning slaps, they still win 0.1345% of games.


### Commands
To simulate 10,000 games of War run:
`python simulate_many_games_of_war.py`

To simulate an Egyptian Rat Tail Game game with debug print statements to watch the game run:
`python egrt_main.py --a_slap_probability 0.5 --debug_print`

To run unit tests, run the following command from the base directory:
`python -m unittest discover -p "*test.py"`
