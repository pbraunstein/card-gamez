from statistics import mean, stdev

from games.egrt import Egrt

probabilities = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.9999999]
N = 100000.0

FILE_NAME = 'egrt_simulation_{}.csv'.format(int(N))

def main():
    print('output file is {}'.format(FILE_NAME))
    filew = open(FILE_NAME, 'w')
    filew.write('A_SLAP_PROBABILITY,A_WIN_PERCENTAGE,TURNS_MEAN,TURNS_STDEV\n')
    for prob in probabilities:
        winners = [] 
        turns = []
        for x in range(int(N)):
            game = Egrt(prob)
            victor, counter = game.simulate_game()
            winners.append(victor)
            turns.append(counter)
        a_win_percentage = winners.count('A') / float(N)
        mean_turns = round(mean(turns))
        stdev_turns = round(stdev(turns))
        print('A slap win probability is {}%'.format(prob))
        print('A wins {}%'.format(a_win_percentage))
        print(mean_turns, '+/-', stdev_turns)
        filew.write('{},{},{},{}\n'.format(
            prob, a_win_percentage, mean_turns, stdev_turns))
    filew.close()

if __name__ == '__main__':
    main()
