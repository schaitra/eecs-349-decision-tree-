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




def chooseBestAttribute(examples):

def entropy(examples, attribute):
  #see how many are yes and no and ?
  #sum(prob()log()prob())



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
