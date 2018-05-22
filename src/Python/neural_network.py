# -*- coding: utf-8 -*-
"""
Created on Tue May 08 00:40:41 2018

@author: xiaob
"""

import numpy
import scipy.special


class NeuralNet(object):

    def __init__(self, n_input, n_hidden, n_output, learning_rate, weight_list):

        self.n_input = n_input
        self.n_hidden = n_hidden
        self.n_output = n_output

        self.learning_rate = learning_rate
        self.weight = weight_list
        
        #self.wih = numpy.random.normal(0.0, pow(self.n_hidden, -0.5), (self.n_hidden, self.n_input))/100
        self.wih = numpy.array([numpy.repeat(each,self.n_hidden) for each in numpy.loadtxt('initial.txt')]).T
        self.wih.shape =  (self.n_hidden, self.n_input)
        #self.who = numpy.random.normal(0.0, pow(self.n_output, -0.5), (self.n_output, self.n_hidden))
        self.who = numpy.ones((self.n_output, self.n_hidden))/self.n_hidden

    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors)
        
        output_drop = scipy.special.expit(abs(output_errors))
        hidden_drop = scipy.special.expit(sum(abs(hidden_errors)))
        diff1 = self.learning_rate * numpy.dot(output_errors * final_outputs * (1.0 - final_outputs), hidden_outputs.T)
        diff2 = self.learning_rate * numpy.dot(hidden_errors * hidden_outputs * (1.0 - hidden_outputs), inputs.T)
        for each in diff1:
            each = each * numpy.random.binomial(1,0.5*hidden_drop)
        for each in diff2:
            each = each * numpy.random.binomial(1,0.5*output_drop)
        for i in xrange(self.n_input):
            diff2[:,i] = diff2[:,i]/((self.weight[i])*(self.weight[i]))
        self.who += diff1
        self.wih += diff2
        
    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return hidden_outputs

    def activation_function(self, x):
        return scipy.special.expit(x)