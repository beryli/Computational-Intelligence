# basic lib
import os,sys
import copy
import time
import math
import random
# plot
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# self define file
import rbfn
import car
parent = os.path.dirname(os.getcwd())

# eval
# encode
# reproduction: roulette wheel
# crossover: one point
# decode

class GA():
    def __init__(self, num_iter=300, population=100, p_mutation=0.5, p_crossover=0.2, num_neuron=12, path='train4dAll.txt', wheel=True):
        super(GA, self).__init__()
        assert population %2 == 0
        # init params
        self.wheel = wheel
        self.dataSet = rbfn.loadTrain(path)
        self.num_inp = len(self.dataSet[0])-1
        self.num_neuron = num_neuron
        self.num_iter = num_iter
        self.population = population
        self.p_m = p_mutation
        self.p_c = p_crossover
        self.BestRBFN = None
        # random init
        self.RBFNSet = [None] * self.population
        for i in range(self.population):
            self.RBFNSet[i] = rbfn.RBFN(self.num_inp, num_neuron)
        # loadDataSet
        # normalization
        for data in self.dataSet:
            data[:-1] = [rbfn.normalization(d, 0, 80) for d in data[:-1]]
            data[-1] = rbfn.normalization(data[-1], -40, 40)

    def evalRBFN(self):
        for i in range(self.population):
            err = 0
            for data in self.dataSet:
                output = self.RBFNSet[i].output(data[:-1])
                err += abs(output - data[-1])
            err /= len(self.dataSet)
            self.RBFNSet[i].error = err * 40
        
        # print('hahahahahahahha')
        # for i in range(10):
        #     print(self.RBFNSet[i].error)
        
        self.RBFNSet.sort(key=lambda x: x.error)
        if self.BestRBFN == None or self.BestRBFN.error > self.RBFNSet[0].error:
            self.BestRBFN = copy.deepcopy(self.RBFNSet[0])
    
    def reproduction(self):
        half = int(self.population/2)
        self.RBFNSet[half:] = copy.deepcopy(self.RBFNSet[:half])
        self.RBFNSet[-1] = copy.deepcopy(self.BestRBFN)

    def reproduction_wheel(self):
        sum = 0
        for i in range(self.population):
            sum += 1/self.RBFNSet[i].error

        newSet = [None] * self.population
        good, idx = 0, 0
        while idx < self.population:
            for _ in range(math.ceil(((1/self.RBFNSet[good].error)/sum)*self.population)):
                newSet[idx] = copy.deepcopy(self.RBFNSet[good])
                idx += 1
                if idx >= self.population:
                    break
            good += 1
        self.RBFNSet = copy.deepcopy(newSet)

    def crossover(self, s1, s2):
        r1, r2 = '', ''
        for i, _ in enumerate(zip(s1, s2)):
            if random.random() < self.p_c:
                r1 += s2[i]
                r2 += s1[i]
            else:
                r1 += s1[i]
                r2 += s2[i]
        return r1, r2

    def mutation(self, s):
        r = ''
        for i, _ in enumerate(s):
            if random.random() < self.p_m:
                r += '1' if s[i] == '0' else '0'
            else:
                r += s[i]
        return r

    def evolution(self):
        self.evalRBFN()
        if self.wheel:
            self.reproduction_wheel()
        else:
            self.reproduction()
        ##################################         encode, crossover and mutation, decode         ##################################
        random.shuffle(self.RBFNSet)
        # for i in range(0, 2, 2):
        for i in range(0, self.population, 2):
            a, b = self.RBFNSet[i], self.RBFNSet[i+1]
            # encode
            a_params, b_params = [], []
            # a
            a_params += [rbfn.float2bin(a.threshold)]
            a_params += [rbfn.float2bin(i) for i in a.wgt]
            for m in a.mu:
                a_params += [rbfn.float2bin(j) for j in m]
            a_params += [rbfn.float2bin(i) for i in a.std]
            # b
            b_params += [rbfn.float2bin(b.threshold)]
            b_params += [rbfn.float2bin(i) for i in b.wgt]
            for m in b.mu:
                b_params += [rbfn.float2bin(j) for j in m]
            b_params += [rbfn.float2bin(i) for i in b.std]
            # crossover and mutation
            for idx, _ in enumerate(zip(a_params, b_params)):
                # crossover
                a_params[idx], b_params[idx] = self.crossover(a_params[idx], b_params[idx])
                # mutation
                a_params[idx] = self.mutation(a_params[idx])
                b_params[idx] = self.mutation(b_params[idx])
            # decode
            # a
            self.RBFNSet[i].threshold = rbfn.bin2float(a_params[0])
            self.RBFNSet[i].wgt = [rbfn.bin2float(i) for i in a_params[1:1+self.num_neuron]]
            for idx, _ in enumerate(self.RBFNSet[i].mu):
                s = 1 + self.num_neuron + self.num_neuron*idx
                self.RBFNSet[i].mu[idx] = [rbfn.bin2float(i) for i in a_params[s:s+self.num_neuron]]
            self.RBFNSet[i].std = [rbfn.bin2float(i) for i in a_params[-self.num_neuron:]]
            # b
            self.RBFNSet[i+1].threshold = rbfn.bin2float(b_params[0])
            self.RBFNSet[i+1].wgt = [rbfn.bin2float(i) for i in b_params[1:1+self.num_neuron]]
            for idx, _ in enumerate(self.RBFNSet[i+1].mu):
                s = 1 + self.num_neuron + self.num_neuron*idx
                self.RBFNSet[i+1].mu[idx] = [rbfn.bin2float(i) for i in b_params[s:s+self.num_neuron]]
            self.RBFNSet[i+1].std = [rbfn.bin2float(i) for i in b_params[-self.num_neuron:]]
                
            
if __name__ == "__main__":
    pass
    # reproduction
    '''
    g = GA()
    g.evalRBFN()
    for i in range(g.population):
        print(g.RBFNSet[i].error)
    print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    g.reproduction_wheel()
    for i in range(g.population):
        print(g.RBFNSet[i].error)
    '''
    # for _ in range(5):
    #     g.evolution()
    #     print(g.BestRBFN.error)
    # g.BestRBFN.saveParams()



