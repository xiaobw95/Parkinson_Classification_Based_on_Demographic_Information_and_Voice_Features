# -*- coding: utf-8 -*-
"""
Created on Tue May 08 00:40:03 2018

@author: xiaob
"""

import sys, os
import random
import numpy
from neural_network import NeuralNet

def train_the_neural_net(neural_net,epochs=1):
    print 'Training the neural network.'
    training_data_file = open('train.csv', 'r')
    training_data_list = training_data_file.readlines()
    training_data_file.close()
    
    epochs = epochs
    for i in range(epochs):
        print 'Training epoch {}/{}.'.format(i+1, epochs)
        for record in training_data_list:
            if numpy.random.binomial(1,0.25) == 1:
                all_values = record.split(',')
                inputs = numpy.asfarray(all_values[1:])
                if int(all_values[0]) == 1:
                    targets = 0.99
                else:
                    targets = 0.01
            #targets = numpy.zeros(output_nodes) + 0.4
            #targets[int(all_values[0])] = 0.6

        neural_net.train(inputs, targets)

    print 'complete.'


def test_the_neural_net(neural_net):
    print 'Testing the neural network.'
    test_data_file = open('test.csv', 'r')
    test_data_list = test_data_file.readlines()
    test_data_file.close()

    scorecard = []
    for i in xrange(len(test_data_list)):
        record = test_data_list[i]
        all_values = record.split(',')
        correct_label = int(all_values[0])
        inputs = numpy.asfarray(all_values[1:])

        outputs = neural_net.query(inputs)
        if outputs[0] > 0.5:
            label = 1
        else:
            label =0
        #label = numpy.argmax(outputs)
        if label == correct_label:
            scorecard.append(1)
        else:
            scorecard.append(0)

    print 'complete.'

    return scorecard


if __name__ == '__main__':

    print 'Starting neural network to recognize handwritten digits.'

    input_nodes = 102
    hidden_nodes = 30
    output_nodes = 1
    learning_rate = 0.1
    
    weight_file = open('sd.txt', 'r')
    weight_list = weight_file.readlines()
    weight_list = numpy.asfarray(weight_list)
    weight_file.close()

    nn = NeuralNet(input_nodes, hidden_nodes, output_nodes, learning_rate, weight_list)

    # Train
    train_the_neural_net(nn,epochs=100)

    # Test
    test_results = numpy.asarray(test_the_neural_net(nn))

    # Print results
    print('Neural network is {}% accurate at predicting handwritten digits.'
        .format(test_results.sum() / float(test_results.size) * 100.0))