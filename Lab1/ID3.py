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
      t.majority = Mode(examples)

      print 'attribute: ', t.attribute
      print 'examples: ', examples
      print 'majority: ', t.majority

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
      #Look through majority of all the children
      # t.majority = Mode(examples)
      # count = {}
      # for child in t.children.values():
        

      #     if child.majority not in count:
      #         count[child.majority] = 1
      #     else:
      #         count[child.majority] += 1
      # print count
      # #most frequent
      # # t.majority = majority that corresponds to max(array of children.numexamples)
      # t.majority = max(count, key=count.get)

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


def prune(node, examples):
    '''
    Takes in a trained tree and a validation set of examples.  Prunes nodes in order
    to improve accuracy on the validation data; the precise pruning strategy is up to you.
    '''

    node = dfs(node, examples)

    return node


def dfs(node, examples):

    # print 'children', node.children
    # print 'examples', examples

    att = node.attribute
    examplesi = []

    for value, child in node.children.iteritems():
        for example in examples:
            if value == example[att]:
                examplesi.append(example)
        node.children[value] = dfs(child, examplesi)
        examplesi = []

    #Base case - compare acc for pruned node and not pruned
    # return pruned node if it's better
    copyNode = copy.copy(node)
    copyNode.children = {}

    if len(examples) is not 0 and test(node, examples) <= test(copyNode, examples):
        # print 'before prune: ', test(node, examples), 'after prune: ', test(copyNode, examples)
        return copyNode

    return node

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
  return node.majority
  # return node.value


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
            
            if newGain<gain:
                gain = newGain 
                best = attribute

    return best


def printNode(node):
  print 'attribute: ', node.attribute
  print 'majority: ', node.majority
  print 'children: ', printChildren(node)
  print 'value: ', node.value
  for key, child in node.children.iteritems():
      print 'key', key
      printNode(child)

def printChildren(node):
  for value, child in node.children.iteritems():
    print ' key:',value, ' child att:',child.attribute, ' child majority:',child.majority, ' child value:',child.value, ' num children:', len(child.children)

