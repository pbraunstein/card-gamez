from argparse import ArgumentParser

from games.war.war import War

def main():
    parser = ArgumentParser(description='play a game of war')
    parser.add_argument('--debug_print', action='store_true')
    args = parser.parse_args()
    game = War()
    print(game.simulate_game(args.debug_print))

if __name__ == '__main__':
    main()
