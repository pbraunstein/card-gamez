from argparse import ArgumentParser

from games.egrt import Egrt

def main():
    parser = ArgumentParser(description='play a game of Egyptian Rat Tail')
    parser.add_argument('--debug_print', action='store_true')
    args = parser.parse_args()
    game = Egrt(0.7)
    result_tuple = game.simulate_game(args.debug_print)
    if args.debug_print:
        print(result_tuple)
    return result_tuple

if __name__ == '__main__':
    main()
