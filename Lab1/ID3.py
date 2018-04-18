from node import Node
import math
import copy 


# examples is an array

# {{Class: 'democrat', handicapped-individual: 'y'}, ...}

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  countDict = getCountDict(examples,'Class') #it can still have the attribute but we may need to remove it
  t = Node()

  lst = []
  for example in examples:
      lst.append(example['Class'])

  if len(examples) == 0:
      t.value= default
      t.majority = default
      return t

  elif lst[1:] == lst[:-1]:
      t.value = examples[0]['Class']
      t.majority = examples[0]['Class']
      return t

  #chooseBestAttribute(examples) is '':
  elif not countDict:
      t.value = Mode(examples)
      t.majority = Mode(examples)
      return t

  best = chooseBestAttribute(examples,countDict)

  if len(countDict[best]) == 1: 
      t.value  = Mode(examples)
      t.majority = Mode(examples)
      return t 

  else:

      values = []
      t.attribute = best 

      for item in examples:
          if item[best] not in values:
              values.append(item[best])
      
      for val in values:
          examplesi = []
          for example in examples: 
              if example[best] == val:
                  examplesi.append(example)
          subtree=Node()
          subtree = ID3(examplesi, Mode(examples))
          t.children[val] = subtree

      return t


def Mode(examples):
  #Takes in a set of examples and returns the most common Class 
  modeDic = {}
  for example in examples:
      if example['Class'] not in modeDic.keys():
          modeDic[example['Class']] = 1
      else:
          modeDic[example['Class']] += 1
  
# If the lengths are the same, it takes the attribute that appears first in the dictionary

  return max(modeDic, key=modeDic.get)


def removeAtt(examples,attribute):
  #removes attribute to prevent it occurring again in the sub tree
  newExamples = copy.deepcopy(examples)

  for example in newExamples:
      if example.has_key(attribute):
          del example[attribute]

  return newExamples
    

def getCountDict(examples, targetAtt):
  '''

  KEEP COUNT OF :
  total amount of each attribute - eg: handicapped - # of yes, # of no, # of q...
  within the particular value of an attribute - #democrat, # republican
  '''

  countDict = {}

  # Going through each example

  for example in examples:

    # Getting all the attributes from that example

    for (attribute, value) in example.iteritems():

      # Removing Class 

        if attribute == targetAtt:
            pass

      # Checking if that one attribute has already been looked at for other examples

        elif attribute in countDict.keys():

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

  return countDict
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



'''
def prune(node, examples):
    
    Takes in a trained tree and a validation set of examples.  Prunes nodes in order
    to improve accuracy on the validation data; the precise pruning strategy is up to you.
    
    acc = test(node,examples)
    newTree = dfs(node,examples)


    return newTree

def dfs(node, examples,acc):
    leaves = []
    numLeaves = len(node.children)
    for value, child in node.children.iteritems():
        if child.value is None:
            newNode = dfs(child, examples)
            if test(node,examples) > acc:
               child = newNode

            child = newNode


            if newNode.value is not None:
                leaves.append(child)
        else:
            leaves.append(child)

    #if all children were added to leaves then check to see if you should prune
    if len(leaves) == numLeaves:
        count = {}
        for leaf in leaves:
            if leaf.value not in count:
                count[leaf.value] = 1
            else:
                count[leaf.value] += 1
        mostFrequent = max(count, key=count.get)

        node.children = {}
        node.value = mostFrequent



    return node

def dfs2 (node,examples,acc):
  attributes = [] 
  while node.children is not None:
    attributes.append(node)
  for x in attributes: 
    set x.value = x.majority 
    set x.children = {}
    newacc = test (oldtree without the node,examples)
    if newacc >= acc: 
      acc=newacc
      dfs (restoftree,examples,acc)


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
  '''Takes in a tree and one example.  Returns the Class value that the tree assigns to the example.
  '''
  while len(node.children) != 0: #check for an empty dict 
    for value, child in node.children.iteritems(): # get value (int) and children (nodes)
     
      if example[node.attribute] == value: #find a match?
          node = child #set node to be the child
          break
    
    #set the node to be the children 
    node = child
  return node.value


def chooseBestAttribute(examples,countDict):

    entropy = 0.0
    gain = float("inf")
    best = ''
    newgain = 0.0

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
                valResult -= num / valTotal * math.log(num / valTotal,
                        2)

            valueResults.append(valResult)
            valueTotals.append(valTotal)
        


        for (counter, num) in enumerate(valueResults):
            newGain += valueTotals[counter] / len(examples) * num
            
            if newGain<=gain:
                gain = newGain 
                best = attribute

    return best