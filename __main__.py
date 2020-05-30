from mirrnum.calc import calc, InfiniteLoopError

import matplotlib.pyplot as plt

import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please also enter a number.')
        quit()
    
    try:
        result = calc(int(sys.argv[1]))
    except InfiniteLoopError:
        print('Infinite loop, try another number')
        quit()

    print('Result: {}'.format(result))

    filename = 'plot.png'

    plt.plot(result)
    plt.savefig(filename)

    print('Saved as: {}'.format(filename))
