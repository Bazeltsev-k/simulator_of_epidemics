import sys
import getopt
import random
import time


def epidemic(nodes, best):
    x = Stack(nodes, best)
    x.change(x.arr[random.randrange(0, nodes, 1)].choose(4, best)) #change random node to 2 and choose it recipients
    count = 0
    for a in x.arr: #count nodes, that recieved packets
        if a.n == 2:
            count += 1
        else:
            pass
    if count == nodes: #if all nodes recieved messages - return 1, else - 0
        return 1
    else:
        return 0


iteration = 0


class Node(object):
    n = 0

    def __init__(self, ind, nodes):
        self.index = ind
        self.nodes = nodes

    def choose(self, x, best): #change node value to 2 (it sends a message) and choose recipients
        global iteration
        self.n = 2
        chooses = []
        i = 0
        while i < x:
            rand = random.randrange(0, self.nodes, 1)
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
        self.arr = [Node(i, nodes) for i in range(0, nodes)]

    def change(self, choosed): #change nodes, that suppose to recieve packets to 1
        global iteration
        for ch in choosed:
            if self.arr[ch].n == 0:
                self.arr[ch].n = 1
            else:
                pass
            iteration += 1
        self.send()

    def send(self): #change nodes, that supposed to send message to 2 and choose their recipients
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
            times = int(arg)
        elif opt == "--your-algorithm":
            your_algorithm = True #use better algorithm or not
    summ = 0
    for i in range(0, int(times)):
        summ += epidemic(nodes, your_algorithm)
        if i == 0:
            print("Algorithm takes", iteration, "iterations to finish 1 time")
    percent = (summ / int(times)) * 100
    print("In", "{:.2f}".format(percent), "% cases all nodes received the packet")
    print("Time of execution:", "{:.2f}".format(time.time() - start_time), "seconds")


if __name__ == "__main__":
    main(sys.argv[1:])
