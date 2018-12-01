from argparse import ArgumentParser

from games.war import War

def main():
    parser = ArgumentParser(description='play a game of war')
    parser.add_argument('--debug_print', action='store_true')
    args = parser.parse_args()
    game = War()
    num_turns = game.simulate_game(args.debug_print)

    if args.debug_print:
        print(num_turns)

    return num_turns

if __name__ == '__main__':
    main()
