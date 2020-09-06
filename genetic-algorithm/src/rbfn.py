import time
import math
import random
import os, sys
parent = os.path.dirname(os.getcwd())


# input float number between -1~1, return string of bits
def float2bin(number, place=16):
    assert isinstance(number, float) and number <= 1 and number >= -1
    if number == 1:
        number = 0.99999
    if number == -1:
        number = -0.99999
    ret = str(1 if number < 0 else 0) #sign
    number = abs(number)
    for _ in range(place-1):
        number *= 2
        if number >= 1:
            ret += '1'
        else:
            ret += '0'
        number = number - math.floor(number)
    return ret


# input string of bits, return float number between -1~1
def bin2float(number):
    assert isinstance(number, str)
    sign = -1 if number[0] == '1' else 1
    ret = 0
    for i in range(1, len(number)):
        ret += int(number[-i])
        ret /= 2
    ret *= sign
    return ret


def loadTrain(path='train4dAll.txt'):
    dataset = []
    with open(parent+'/data/'+path, 'r') as f:
        for line in f.readlines():
            data = line.split()
            data = [float(i) for i in data]
            dataset.append(data)
    return dataset


# input number and its range, return the normalized number between -1~1
def normalization(num, lower, upper):
    assert lower < upper
    half, mean = (upper-lower)/2, (upper+lower)/2
    return (num-mean) / half


# input number between -1~1 and its range, return the denormalized number
def denormalization(num, lower, upper):
    assert lower < upper
    half, mean = (upper-lower)/2, (upper+lower)/2
    return num * half + mean


class RBFN():
    def __init__(self, num_inp=3, num_neuron=3):
        # threshold + weight + mean + sigma
        # init params to -1~1, set sigma to 0~1
        self.num_inp, self.num_neuron = num_inp, num_neuron
        self.threshold = 0.0
        self.wgt = [random.uniform(-1, 1) for _ in range(num_neuron)]
        self.mu = [[random.uniform(-1, 1) for _ in range(num_inp)] for _ in range(num_neuron)]
        self.std = [random.uniform(0, 1) for _ in range(num_neuron)]
        self.error = float('inf')

    def saveParams(self):
        # t = time.strftime('_%H%M%S')
        with open(parent+'/weights/RBFN_params_' + str(self.num_inp) + '_' + str(self.num_neuron) + '.txt', 'w') as f:
            f.write('{:07.4f}\n'.format(self.threshold))
            for i in range(self.num_neuron):
                f.write('{:07.4f} '.format(self.wgt[i]))
                for j in range(self.num_inp):
                    f.write('{:07.4f} '.format(self.mu[i][j]))
                f.write('{:07.4f}'.format(self.std[i]))
                f.write('\n')
    
    def loadParams(self, path='RBFN_params.txt'):
        with open(parent+'/weights/'+path, 'r') as f:
            lines = [line.replace('\n', '').split(' ') for line in f.readlines()]
            lines = [[float(f) for f in line] for line in lines]

            self.num_inp = len(lines[1]) - 2
            self.num_neuron = len(lines) - 1
            self.wgt = [None] * self.num_neuron
            self.mu = [[None] * self.num_inp] * self.num_neuron
            self.std = [None] * self.num_neuron

            self.threshold = lines[0][0]
            for i in range(self.num_neuron):
                self.wgt[i] = lines[i+1][0]
                self.mu[i] = lines[i+1][1:-1]
                self.std[i] = lines[i+1][-1]

    # with normalized input, return normalized output
    def output(self, inp):
        assert len(inp) == self.num_inp
        phi = [None] * self.num_neuron
        for i in range(self.num_neuron):
            if self.std[i] == 0.0:
                self.std[i] = 0.0001
            numerator = [(x-y)*(x-y) for x, y in zip(inp, self.mu[i])]
            numerator = sum(numerator)
            phi[i] = math.exp( - numerator / (2*self.std[i]*self.std[i]))
        result = self.threshold + sum([x*y for x, y in zip(self.wgt, phi)])
        return result
    

if __name__ == "__main__":
    pass
    # test load/save
    
    # a = RBFN(1, 1)
    # a.loadParams()
    # print(a.num_inp, a.num_neuron)
    # print(a.error)
    # print(a.threshold)
    # print(a.wgt)
    # print(a.mu)
    # print(a.std)
    # a.saveParams()
    

    # test output
    '''
    a = RBFN(3, 1)
    inp = [22, 8.4, 8.4]
    inp[0:3] = [normalization(i, 0, 80) for i in inp[0:3]]
    a.wgt, a.mu, a.std = [1], [[1, 1, 1]], [1]
    result = a.output(inp)
    print(result)
    '''