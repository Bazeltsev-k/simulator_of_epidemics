import sys
import getopt
import random
import time


def epidemic(nodes, best):
    x = Stack(nodes, best)
    x.change(x.arr[random.randrange(0, 20, 1)].choose(4, best))
    count = 0
    for a in x.arr:
        if a.n == 2:
            count += 1
        else:
            pass
    if count == 20:
        return 1
    else:
        return 0


iteration = 0


class Node(object):
    n = 0

    def __init__(self, ind):
        self.index = ind

    def choose(self, x, best):
        global iteration
        self.n = 2
        chooses = []
        i = 0
        while i < x:
            rand = random.randrange(0, 20, 1)
            if (rand in chooses and best) or rand == self.index:
                pass
            else:
                chooses.append(rand)
                i += 1
            iteration += 1
        return chooses


class Stack:
    def __init__(self, nodes, best):
        self.best = best
        self.arr = [Node(i) for i in range(0, nodes)]

    def change(self, choosed):
        global iteration
        for ch in choosed:
            if self.arr[ch].n == 0:
                self.arr[ch].n = 1
            else:
                pass
            iteration += 1
        self.send()

    def send(self):
        global iteration
        for a in self.arr:
            if a.n == 1:
                self.change(a.choose(4, self.best))
            else:
                pass
            iteration += 1


def main(argv):
    global iteration
    random.seed(time.time())
    start_time = time.time()
    nodes = 0
    times = 0
    your_algorithm = False
    try:
        opts, args = getopt.getopt(argv, "hn:i:", ["your-algorithm", "help"])
    except getopt.GetoptError:
        print('simulate.py -n <number of nodes> -i <number of times algorithm should be ran> --your-algorithm for better results')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ['-h', '--help']:
            print('simulate.py -n <number of nodes> -i <number of times algorithm should be ran> --your-algorithm for better results')
            sys.exit()
        elif opt == "-n":
            nodes = int(arg)
        elif opt == "-i":
            times = arg
        elif opt == "--your-algorithm":
            your_algorithm = True
    if not your_algorithm:
        best_algorithm = False
        summ = 0
        for i in range(0, int(times)):
            summ += epidemic(nodes, best_algorithm)
            if i == 0:
                print("Algorithm takes", iteration, "iterations to finish 1 time")
        percent = (summ / int(times)) * 100
        print("In", "{:.2f}".format(percent), "% cases all nodes received the packet")
        print("Time of execution:", "{:.2f}".format(time.time() - start_time), "seconds")
    elif your_algorithm:
        best_algorithm = True
        summ = 0
        for i in range(0, int(times)):
            summ += epidemic(nodes, best_algorithm)
            if i == 0:
                print("Algorithm takes", iteration, "iterations to finish 1 time")
        percent = (summ / int(times)) * 100
        print("In", "{:.2f}".format(percent), "% cases all nodes received the packet")
        print("Time of execution:", "{:.2f}".format(time.time() - start_time), "seconds")


if __name__ == "__main__":
    main(sys.argv[1:])
