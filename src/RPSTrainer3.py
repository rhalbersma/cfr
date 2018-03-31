#          Copyright Rein Halbersma 2018.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          http://www.boost.org/LICENSE_1_0.txt)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as sm

class RPSTrainer:
    def __init__(self):
        self.NUM_ACTIONS = 3
        self.actionUtility = np.array([
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ])        
        self.regretSum = np.zeros(self.NUM_ACTIONS)
        self.strategySum = np.zeros(self.NUM_ACTIONS)
        self.oppStrategy = [.4, .3, .3]
    
    def normalize(self, strategy):
        normalizingSum = np.sum(strategy)
        if normalizingSum > 0:
            strategy /= normalizingSum
        else:
            strategy = np.repeat(1 / self.NUM_ACTIONS, self.NUM_ACTIONS)
        return strategy       
    
    def getStrategy(self):
        return self.normalize(self.regretSum.clip(min=0))
    
    def getAverageStrategy(self):
        return self.normalize(np.copy(self.strategySum))
        
    def bestResponse(self, utility): 
        return np.eye(self.NUM_ACTIONS)[np.argmax(utility)]
        
    def exploitability(self, strategy):
        utility = np.dot(self.actionUtility, self.oppStrategy)
        return np.dot(self.bestResponse(utility) - strategy, utility)
    
    def train(self, iterations, df=None, sample=.001):        
        for i in range(iterations):
            strategy = self.getStrategy()
            self.strategySum += strategy
            
            Q_values = np.dot(self.actionUtility, self.oppStrategy)
            value = np.dot(strategy, Q_values)
            regret = Q_values - value
            for a in range(self.NUM_ACTIONS):
                # Trick by Brown & Sandholm (NIPS 2015) to track negative cumulative regret
                if regret[a] > 0 and self.regretSum[a] <= 0:
                    self.regretSum[a] = regret[a]
                else:
                    self.regretSum[a] += regret[a]
                
            if df is None or np.random.random() > sample:
                continue
            target_policy = self.getAverageStrategy()
            df = df.append(
                pd.DataFrame(
                    np.append(
                        np.array([i, self.exploitability(target_policy)]),
                        target_policy                        
                    ).reshape(-1, 2 + self.NUM_ACTIONS), 
                    columns=list(df)
                ), 
                ignore_index=True
            )
        
        return df
    
def main():
    columns = ['iterations', 'exploitability', 'rock', 'paper', 'scissors']
    df = pd.DataFrame(columns=columns)        
    
    trainer = RPSTrainer()
    df = trainer.train(1000000, df)
    target_policy = trainer.getAverageStrategy()
    
    print('Target policy: %s' % (target_policy))
    for c in columns[2:]:
        plt.loglog(df[columns[0]], df[c], label=c)
    plt.xlabel(columns[0])
    plt.ylabel('target policy')
    plt.legend()
    plt.show()
    
    print('Exploitability: %s' % (trainer.exploitability(target_policy)))
    plt.loglog(df[columns[0]], df[columns[1]])
    plt.xlabel(columns[0])
    plt.ylabel(columns[1])
    plt.legend()
    plt.show()
    
    model = sm.ols(formula="np.log(exploitability) ~ np.log(iterations)", data=df).fit()
    print(model.params)
    
if __name__ == "__main__":
    main()
