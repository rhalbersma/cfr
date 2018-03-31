#          Copyright Rein Halbersma 2018.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          http://www.boost.org/LICENSE_1_0.txt)

import numpy as np

class RPSTrainer:
    def __init__(self):
        self.NUM_ACTIONS = 3
        self.regretSum = np.zeros(self.NUM_ACTIONS)
        self.strategySum = np.zeros(self.NUM_ACTIONS)
        self.oppStrategy = [.4, .3, .3]
    
    def getStrategy(self):
        strategy = self.regretSum.clip(min=0)
        normalizingSum = np.sum(strategy)
        if normalizingSum > 0:
            strategy /= normalizingSum
        else:
            strategy = np.repeat(1 / self.NUM_ACTIONS, self.NUM_ACTIONS)
        self.strategySum += strategy
        return strategy
    
    def getAction(self, strategy):
        return np.random.choice(len(strategy), p=strategy)
    
    def train(self, iterations):
        actionUtility = np.zeros(self.NUM_ACTIONS)
        
        for i in range(iterations):
            strategy = self.getStrategy()
            myAction = self.getAction(strategy)
            otherAction = self.getAction(self.oppStrategy)
            
            actionUtility[otherAction] = 0
            actionUtility[0 if otherAction == self.NUM_ACTIONS - 1 else otherAction + 1] = 1
            actionUtility[self.NUM_ACTIONS - 1 if otherAction == 0 else otherAction - 1] = -1
            
            for a in range(self.NUM_ACTIONS):
                self.regretSum[a] += actionUtility[a] - actionUtility[myAction]
    
    def getAverageStrategy(self):
        normalizingSum = np.sum(self.strategySum)
        if normalizingSum > 0:
            avgStrategy = self.strategySum / normalizingSum
        else:
            avgStrategy = np.repeat(1 / self.NUM_ACTIONS, self.NUM_ACTIONS)
        return avgStrategy
        
def main():
    trainer = RPSTrainer()
    trainer.train(1000000)
    print(trainer.getAverageStrategy())
    
if __name__ == "__main__":
    main()
