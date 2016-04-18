#!/usr/bin/env python

import sys


def main(configFile, predictFile, truthFile):
	configInput = open(configFile)
	costDict = {'all': {}, '1': {}, '2': {}, '3': {}, '4': {}, '5': {}}
	for line in configInput:
		line = line.strip().split(',')
		lessCost = int(line[2].split('_')[0])
		moreCost = int(line[2].split('_')[1])
		costDict[line[1]][line[0]] = {0: lessCost, 1: moreCost}

	configInput.close()

	predictInput = open(predictFile)
	predictDict = {'all': {}, '1': {}, '2': {}, '3': {}, '4': {}, '5': {}}
	for line in predictInput:
		line = line.strip().split(',')
		predictDict[line[1]][line[0]] = int(line[3])

	predictInput.close()

	sumCost = 0
	truthInput = open(truthFile)
	for line in truthInput:
		line = line.strip().split(',')
		predict = predictDict[line[1]][line[0]]
		if predict < int(line[2]):
			sumCost += costDict[line[1]][line[0]][0] * (int(line[2]) - predict)
		else:
			sumCost += costDict[line[1]][line[0]][1] * (predict - int(line[2]))

	truthInput.close()


if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2], sys.argv[3])




