from node import Node
import math


#examples is an array

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''

  curTree = Node.Node()

  tree = ID3helper(currTree, examples, default)

  return tree

  if len(examples) == 0:
    #return an empty node
    return Node.Node()

  # elif ALL EXAMPLES ARE THE SAME or CANNOT SPLIT EASILY:
    #Node.Node(Mode(examples), examples.

  else:
    best = chooseBestAttribute(examples)
    t = Node.Node(best,  )


def ID3Helper():


def Mode(examples):
  modeDic = {}
  for example in examples:
    if example['Class'] not in modeDic.keys():
      modeDic[example['Class']] = 1
    else:
      modeDic[example['Class']] += 1

  #If the lengths are the same, it takes the attribute that appears first in the dictionary

  return max(modeDic, key=modeDic.get)




def chooseBestAttribute(examples,attributes,class):

  bestgain = 0 
  bestattribute = ""

  for item in attributes: 
    gain  = infgain (examples)
    if gain>bestgain:
      bestgain = gain
      bestattribute = item 

  return bestgain,bestattribute


def targetentropy(examples, class): #works for binary classification not sure if we need this at all

entropy = 0.0 

v1 = 0 
v2 = 0 
q = 0

for item in examples: 
    if item[class] == "0": #0  means republican 
        v1 = v1+1 
    elif item[class] == '1': #democrat 
        v2 = v2 + 1 
    else:
        q = q+1

pv1 = v1/ (v1+v2+q)
pv2 = v2/ (v1+v2+q)
pq = q/ (v1+v2+q) 

entropy = - (pv1 * math.log(pv1,2)) - (pv2 * math.log(pv2,2)) - (pq * math.log(pq,2))
return entropy


## For this next infogain function, we should use dictionaries to store attributes: values
## one of their values should be a dict with number of democrats and number of republicans 
## I was stuck on how to a)Create this dict and b) how to access different values of it 

def infogain (examples):
'''

KEEP COUNT OF :
total amount of each attribute - eg: handicapped - # of yes, # of no, # of q...
within the particular value of an attribute - #democrat, # republican
'''
    
att = data[1].keys()
del att['Class']

dict = {} 
l = len(examples)
entropy = 0.0 
gain = 0.0

for item in examples: 
    for attribute in att:
        if value of item[attribute] in dict
        count of item in dictionary +1 
            if class of item is already included
                class +=1 
            else:
                class =1 
        else: 
        count of item = 1 
        class of item +1 

#results in a dictionary with {attribute:values}
#eg: {handicapped infants: y, democrats:, republicans:, n...., ?...}

for value in dict (y/n/?):
    for nextvalue in next dict:
     entropy += nextvalue/(sum of democrats and republicans)*math.log(nextvalue/sum of democrats and republicans)
     gain += value/len(examples)*entropy 
     return abs(gain)





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


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
