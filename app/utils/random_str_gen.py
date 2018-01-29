import sys
from string import letters, punctuation
from random import sample

class LNP(object):
    ''' Generates a random string from letters, numbers, and punctuation'''
    population = letters + ''.join(str(i) for i in range(26)) + punctuation * 2

    def __init__(self, strlen=10):
        self.strlen = int(strlen)

    def __len__(self):
        return sum(1 for x in list(self.population))

    def __repr__(self):
        while self.strlen > len(self):
            self.population *= 2
        return ''.join(sample(self.population, int(self.strlen)))

class LN(LNP):
    ''' Generates a random string from letters and numbers'''
    population = letters + ''.join(str(i) for i in range(26))

if __name__ == '__main__':
    print 'LN:  {}\nLNP: {:>3}'.format(LN(sys.argv[1]), LNP(sys.argv[1]))