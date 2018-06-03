import sys
import getopt
import random
import time


iteration = 0


class Stack:
    def __init__(self, nodes, best, x):
        self.nodes = nodes
        self.best = best
        self.arr = [0 for i in range(0, nodes)]
        self.x = x

    def choose(self, index, x, best): #change node value, that supposed to send message to 2 and choose recipients
        global iteration
        chooses = []
        i = 0
        self.arr[index] = 2
        while i < x:
            rand = random.randrange(0, self.nodes, 1)
            if (rand in chooses and best) or rand == index:
                pass
            else:
                chooses.append(rand)
                if self.arr[rand] == 0:
                    self.arr[rand] = 1
                else:
                    pass
                i += 1
            iteration += 1
        self.send()

    def send(self): #call choose() for all nodes, that supposed to send message
        global iteration
        i = 0
        for a in self.arr:
            if a == 1:
                self.choose(i, self.x, self.best)
            else:
                pass
            i += 1
            iteration += 1


def epidemic(nodes, best, amount_of_recipients):
    x = Stack(nodes, best, amount_of_recipients)
    x.choose(x.arr[random.randrange(0, nodes, 1)], amount_of_recipients, best)#change random node to 2 and choose it recipients
    count = 0
    for a in x.arr: #count nodes, that recieved packets
        if a == 2:
            count += 1
        else:
            pass
    if count == nodes: #if all nodes recieved messages - return 1, else - 0
        return 1
    else:
        return 0


def main(argv):
    global iteration
    random.seed(time.time())
    start_time = time.time()
    nodes = 0
    times = 0
    x = 4
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
        summ += epidemic(nodes, your_algorithm, x)
        if i == 0:
            print("Algorithm takes", iteration, "iterations to finish 1 time")
    percent = (summ / int(times)) * 100
    print("In", "{:.2f}".format(percent), "% cases all nodes received the packet")
    print("Time of execution:", "{:.2f}".format(time.time() - start_time), "seconds")


if __name__ == "__main__":
    main(sys.argv[1:])
