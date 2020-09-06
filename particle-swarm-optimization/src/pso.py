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


class PSO():
    def __init__(self, num_iter=300, population=100, phi_1=0.5, phi_2=0.5, num_neuron=12, maxVelocity=1, path='train4dAll.txt'):
        super(PSO, self).__init__()
        self.maxVelocity = maxVelocity
        # loadDataSet
        self.dataSet = rbfn.loadTrain(path)
        self.num_inp = len(self.dataSet[0])-1
        # normalization
        for data in self.dataSet:
            data[:-1] = [rbfn.normalization(d, 0, 80) for d in data[:-1]]
            data[-1] = rbfn.normalization(data[-1], -40, 40)
        
        # init params
        self.num_iter = num_iter
        self.population = population
        self.phi_1 = phi_1
        self.phi_2 = phi_2
        self.num_neuron = num_neuron
        self.BestRBFN = None
        # random init
        self.RBFNSet = [None] * self.population
        for i in range(self.population):
            self.RBFNSet[i] = rbfn.RBFN(self.num_inp, num_neuron)
        # initialize RBFN error
        for i in range(self.population):
            err = 0
            for data in self.dataSet:
                output = self.RBFNSet[i].output(data[:-1])
                err += abs(output - data[-1])
            err /= len(self.dataSet)
            self.RBFNSet[i].error = err * 40
        self.RBFNSet.sort(key=lambda x: x.error)
        if self.BestRBFN == None or self.BestRBFN.error > self.RBFNSet[0].error:
            self.BestRBFN = copy.deepcopy(self.RBFNSet[0])
        # initialize pastself
        self.RBFN_self = copy.deepcopy(self.RBFNSet)
        # initialize velocity
        self.RBFN_v = [None] * self.population
        for i in range(self.population):
            self.RBFN_v[i] = rbfn.RBFN(self.num_inp, num_neuron)
            for j in range(self.RBFN_v[i].num_neuron):
                self.RBFN_v[i].wgt[j] = 0
                self.RBFN_v[i].std[j] = 0
                for k in range(self.RBFN_v[i].num_inp):
                    self.RBFN_v[i].mu[j][k] = 0

    def evalPSO(self):
        for i in range(self.population):
            err = 0
            for data in self.dataSet:
                output = self.RBFNSet[i].output(data[:-1])
                err += abs(output - data[-1])
            err /= len(self.dataSet)
            self.RBFNSet[i].error = err * 40
            # update RBFN_self
            if self.RBFNSet[i].error < self.RBFN_self[i].error:
                self.RBFN_self[i] = copy.deepcopy(self.RBFNSet[i])
        
        # print('hahahahahahahha')
        # for i in range(10):
        #     print(self.RBFNSet[i].error)
        
        # sort self.RBFN_self
        ######################################################
        idx = sorted(range(self.population), key=lambda x: self.RBFNSet[x].error)
        # for i in range(self.population):
        #     print(idx[i], self.RBFNSet[idx[i]].error)
        tempRBFN = [None] * self.population
        for i in range(self.population):
            tempRBFN[i] = self.RBFNSet[idx[i]]
        self.RBFN_self = copy.deepcopy(tempRBFN)
        ######################################################
        self.RBFNSet.sort(key=lambda x: x.error)
        if self.BestRBFN == None or self.BestRBFN.error > self.RBFNSet[0].error:
            self.BestRBFN = copy.deepcopy(self.RBFNSet[0])

    def iter(self):
        for i in range(self.population):
            self.RBFNSet[i].threshold, self.RBFN_v[i].threshold = self.PSOalgorithm(self.RBFN_v[i].threshold, self.RBFN_self[i].threshold, self.BestRBFN.threshold, self.RBFNSet[i].threshold)
            for j in range(self.RBFNSet[i].num_neuron):
                self.RBFNSet[i].wgt[j], self.RBFN_v[i].wgt[j] = self.PSOalgorithm(self.RBFN_v[i].wgt[j], self.RBFN_self[i].wgt[j], self.BestRBFN.wgt[j], self.RBFNSet[i].wgt[j])
                self.RBFNSet[i].std[j], self.RBFN_v[i].std[j] = self.PSOalgorithm(self.RBFN_v[i].std[j], self.RBFN_self[i].std[j], self.BestRBFN.std[j], self.RBFNSet[i].std[j])
                if self.RBFNSet[i].std[j] < 0:
                    self.RBFNSet[i].std[j] = 0
                for k in range(self.RBFNSet[i].num_inp):
                    self.RBFNSet[i].mu[j][k], self.RBFN_v[i].mu[j][k] = self.PSOalgorithm(self.RBFN_v[i].mu[j][k], self.RBFN_self[i].mu[j][k], self.BestRBFN.mu[j][k], self.RBFNSet[i].mu[j][k])
        self.evalPSO()
        print(self.BestRBFN.error)

    def PSOalgorithm(self, last_v, previous, neighbor, itself):
        v = last_v + self.phi_1 * (previous - itself) + self.phi_2 * (neighbor - itself)
        if v > self.maxVelocity:
            v = self.maxVelocity
        newself = itself + v
        if newself > 1:
            newself = 1
        elif newself < -1:
            newself = -1
        return newself, v


if __name__ == "__main__":
    # for test in range(10):
        # p = PSO()
        # for i in range(1):
        #     p.iter()
    #     print('\n\n\n')


    # s = [2, 3, 1, 4, 5]
    # temp = sorted(range(len(s)), key=lambda k: s[k])
    # print(temp)
    # print(s)
    pass
