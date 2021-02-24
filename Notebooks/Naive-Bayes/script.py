#import libraries
import csv
import math
import random

def loaddata(file):
    data = csv.reader(open('pima_diabetes.csv','r'))
    dataset = list(data)
    for i in range (len(dataset)):
        try:
            dataset[i] = [float(x) for x in dataset[i]]
        except (ValueError) as e:
             print (e)
    return dataset


def split(dataset,splitRatio):
    train_size = int(len(dataset) * splitRatio)
    train_set = []
    copy = list(dataset)
    while len(train_set) < train_size:
        index = random.randrange(len(copy))
        train_set.append(copy.pop(index))
    return [train_set, copy]

def separateClass(dataset):
    separated = []
    for i in range(len(dataset)):
        vector = dataset[i]
        if(vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

def mean(number):
    return sum(number)/float(len(number))

def standarddev(number):
    avg = mean(number)
    variance = sum([pow(x-avg,2) for x in number])/float(len(number)-1)
    return math.sqrt(variance)


def summarize(dataset):
    summaries = [(mean(attribute), standarddev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries


def summariesClass(dataset):
    separated = separateClass(dataset)
    summaries = {}
    for classVal, instances in separated.items():
        summaries[classVal] = summarize(instances)
    return summaries


def CalProbability(x , mean, std):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(std,2))))
    return (1/(math.sqrt(2*math.pi)*std))*exponent


def CalclassProb(summaries, inputVec):
    probabilities = {}
    for ClassVal, classSummaries in summaries.item():
        probabilities[ClassVal] = 1
        for i in range(len(classSummaries)):
            mean, std = classSummaries[i]
            x = inputVec[i]
            probabilities[ClassVal] *= CalProbability(x, mean, std)
        return probabilities


def predict(summaries, inputVec):
    probabilities = CalclassProb(summaries, inputVec)
    bestlabel, bestPro = None, -1
    for ClassVal, probability in probabilities.items():
        if bestlabel is None or probability > bestPro:
            bestPro = probability
            bestlabel = ClassVal
    return bestlabel

def getPred(summaries, test_set):
    predictions = []
    for i in range(len(test_set)):
        result = predict(summarires, test_set[i])
        predictions.append(result)
    return predictions

def Accuracy(test_set, predictions):
    correct = 0
    for i in range(len(test_set)):
        if test_set[i][-1] == predictions[i]:
            correct += 1
    return (correct/float(len(test_set)))*100.0

def main():
    file = 'pima_diabetes.csv'
    splitRatio = 0.8
    dataset = loaddata(file)
    trainingset, test_Set = split(dataset, splitRatio)
    print('Split {0} rows into train = {1} and test = {2} rows'.format(len(dataset),len(trainingset),len(test_Set)))
    summaries = summariesClass(trainingset)
    predictions = getPred(summaries, test_Set)
    accuracy = Accuracy(test_Set, predictions)
    print('Accuracy: {0}%'.format(accuracy))
    
main()