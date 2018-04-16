#!/usr/bin/python
# -*- coding: utf-8 -*-
from node import Node
import math


# examples is an array

# {{Class: 'democrat', handicapped-individual: 'y'}, ...}

def ID3(examples, default):
    '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''

    lst = []
    for example in examples:
        lst.append(example['Class'])
    t = Node()

    if len(examples) == 0:
        t.label= default
        return t
    
    elif lst[1:] == lst[:-1]:

  # elif ALL EXAMPLES ARE THE SAME or CANNOT SPLIT EASILY:
    # Node.Node(Mode(examples), examples.
                            # include check for non trivial splits
        t.label = (Mode(examples))
        return t

    else:

        values = []
        best = chooseBestAttribute(examples,'Class')
        t.attribute = best 

        for item in examples:
            if item[best] not in values:
                values.append(item[best])

        for val in values:
            examplesi = []
            for example in examples:
                if example[best] == val:
                    examplesi.append(example)
                subtree = ID3(remove(examplesi,best), Mode(examples))
                t.addBranch(subtree, val)
        return t


def Mode(examples):
    modeDic = {}
    for example in examples:
        if example['Class'] not in modeDic.keys():
            modeDic[example['Class']] = 1
        else:
            modeDic[example['Class']] += 1

  # If the lengths are the same, it takes the attribute that appears first in the dictionary

    return max(modeDic, key=modeDic.get)

def remove(examples,attribute):
  copy = examples.copy()

  if copy.has_key(attribute):
    copy.remove(attribute)

  return copy


## For this next infogain function, we should use dictionaries to store attributes: values
## one of their values should be a dict with number of democrats and number of republicans
## I was stuck on how to a)Create this dict and b) how to access different values of it

def chooseBestAttribute(examples, targetAtt):
    '''

  KEEP COUNT OF :
  total amount of each attribute - eg: handicapped - # of yes, # of no, # of q...
  within the particular value of an attribute - #democrat, # republican
  '''

    countDict = {}


  # TODO: TAKE OUT CLASS FROM ATTRIBUTES

  # Going through each example

    for example in examples:

      # Getting all the attributes from that example

        for (attribute, value) in example.iteritems():

          # Checking if that one attribute has already been looked at for other examples

            if attribute in countDict.keys():

              # if it has that attribute, check to see if that value has already been looked at for that attribute for other examples

                if value in countDict[attribute].keys():

                  # If it has that value, check to see if that value of the targetAtt has been looked at for that value of that attribute for other examples

                    if example[targetAtt] \
                        in countDict[attribute][value].keys():

                      # If that value of that target attribute has already been looked at for this value of this attribute of this example, just incrememt it

                        countDict[attribute][value][example[targetAtt]] += \
                            1
                    else:

                      # Otherwise add that value of that target attribute to the dictionary

                        countDict[attribute][value][example[targetAtt]] = \
                            1
                else:

                  # Does not have the value, add that value and value of the TargetAtt to the dictionary

                    countDict[attribute][value] = {}
                    countDict[attribute][value][example[targetAtt]] = 1
            else:
                countDict[attribute] = {}
                countDict[attribute][value] = {}
                countDict[attribute][value][example[targetAtt]] = 1

  # EXAMPLE OF WHAT THE DICTIONARY ^^^ THAT WOULD CREATE
  # {{att1:
  #         {x: {'democrat': 0, 'republican': 0}},
  #         {y: {'democrat': 5, 'republican': 2}},
  #         {z: {'democrat': 2, 'republican': 6}},
  #         {?: {'democrat': 0, 'republican': 1}}},
  #  {att2:
  #         {x: {'democrat': 0, 'republican': 0}},
  #         {y: {'democrat': 5, 'republican': 2}},
  #         {z: {'democrat': 2, 'republican': 6}},
  #         {?: {'democrat': 0, 'republican': 1}}}}

    entropy = 0.0
    gain = 0.0
    attributeCount = 0
    valCount = 0
    best = ''

    for (attribute, value) in countDict.iteritems():
        newGain = 0.0
        attributeCount = 0.0
        valueResults = []
        valueTotals = []
        for (val, targetAtts) in value.iteritems():
            itemCounts = []
            valTotal = 0.0
            valResult = 0.0
            for (item, count) in targetAtts.iteritems():
                valTotal += count
                itemCounts.append(count)

            for num in itemCounts:
                valResult += num / valTotal * math.log(num / valTotal,
                        2)

            attributeCount += valCount
            valueResults.append(valResult)
            valueTotals.append(valTotal)

        for (counter, num) in enumerate(valueResults):
            newGain += valueTotals[counter] / len(examples) * num

        if abs(newGain) >= gain:
            gain = abs(newGain)
            best = attribute

    return best


def prune(node, examples):
    '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''


def test(node, examples):
    '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''

    count = 0.0
    for example in examples:
        exclass = evaluate(node, example)
        if exclass == example['Class']:
            count += 1
    acc = count / len(examples)
    return acc


def evaluate(node, example):
    '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''

  if len(node.children==0):
    return node.value

    while len(node.children) is not 0:
      for val, branch in node.children.iteritems():
        if example[node.attribute] == val: #match --> move down tree
          node=branch
      

    return node.value
