from statistics import mean, stdev

import war_main

def main():
    results = []
    for x in xrange(10000):
        results.append(war_main.main())
    print(round(mean(results)), '+/-', round(stdev(results)))

if __name__ == '__main__':
    main()
