// Copyright Todd W. Neller and Marc Lanctot 2013.

import java.util.Arrays;
import java.util.Random;

public class RPSTrainer {
        
    public static final int ROCK = 0, PAPER = 1, SCISSORS = 2, NUM_ACTIONS = 3;
    public static final Random random = new Random();
    double[] regretSum = new double[NUM_ACTIONS], 
             strategy = new double[NUM_ACTIONS], 
             strategySum = new double[NUM_ACTIONS], 
             oppStrategy = { 0.4, 0.3, 0.3 }; 

    private double[] getStrategy() {
        double normalizingSum = 0;
        for (int a = 0; a < NUM_ACTIONS; a++) {
            strategy[a] = regretSum[a] > 0 ? regretSum[a] : 0;
            normalizingSum += strategy[a];
        }
        for (int a = 0; a < NUM_ACTIONS; a++) {
            if (normalizingSum > 0)
              strategy[a] /= normalizingSum;
            else
              strategy[a] = 1.0 / NUM_ACTIONS;
            strategySum[a] += strategy[a];
        }
        return strategy;
    }
    

    public int getAction(double[] strategy) {
        double r = random.nextDouble();
        int a = 0;
        double cumulativeProbability =  0;
        while (a < NUM_ACTIONS - 1) {
            cumulativeProbability += strategy[a];
            if (r < cumulativeProbability)
                break;
            a++;
        }
        return a;
    }
    

    public void train(int iterations) {
        double[] actionUtility = new double[NUM_ACTIONS];
        for (int i = 0; i < iterations; i++) {
            double[] strategy = getStrategy();
            int myAction = getAction(strategy);
            int otherAction = getAction(oppStrategy);

            actionUtility[otherAction] = 0;
            actionUtility[otherAction == NUM_ACTIONS - 1 ? 0 : otherAction + 1] = 1;
            actionUtility[otherAction == 0 ? NUM_ACTIONS - 1 : otherAction - 1] = -1;

            for (int a = 0; a < NUM_ACTIONS; a++)
                regretSum[a] += actionUtility[a] - actionUtility[myAction];

        }
    }
    

    public double[] getAverageStrategy() {
        double[] avgStrategy = new double[NUM_ACTIONS];
        double normalizingSum = 0;
        for (int a = 0; a < NUM_ACTIONS; a++)
            normalizingSum += strategySum[a];
        for (int a = 0; a < NUM_ACTIONS; a++) 
            if (normalizingSum > 0)
                avgStrategy[a] = strategySum[a] / normalizingSum;
            else
                avgStrategy[a] = 1.0 / NUM_ACTIONS;
        return avgStrategy;
    }

    public static void main(String[] args) {
        RPSTrainer trainer = new RPSTrainer();
        trainer.train(1000000);
        System.out.println(Arrays.toString(trainer.getAverageStrategy()));
    }


}
