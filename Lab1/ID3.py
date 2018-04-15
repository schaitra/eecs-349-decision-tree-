from node import Node
import math


#examples is an array


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

  return tree

  if len(examples) == 0:
    #return an empty node
    return default

  # elif ALL EXAMPLES ARE THE SAME or CANNOT SPLIT EASILY:
    #Node.Node(Mode(examples), examples.
  elif lst[1:] == lst[:-1]: #include check for non trivial splits 
    return Mode(examples)

  else:
    values = []
    best = chooseBestAttribute(examples)
    t = Node.Node(best)

    for item in examples:
      if item[best] not in values:
       values.append(item[best])

    for val in values:
      examplesi = []
      for example in examples:
        if example[best] == val:
          examplesi.append(example)
        subtree = ID3(examplesi,Mode(examples))
        t.addBranch(subtree,val)
    return t    



def Mode(examples):
  modeDic = {}
  for example in examples:
    if example['Class'] not in modeDic.keys():
      modeDic[example['Class']] = 1
    else:
      modeDic[example['Class']] += 1

  #If the lengths are the same, it takes the attribute that appears first in the dictionary

  return max(modeDic, key=modeDic.get)



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

def chooseBestAttribute(examples, targetAtt):
  '''

  KEEP COUNT OF :
  total amount of each attribute - eg: handicapped - # of yes, # of no, # of q...
  within the particular value of an attribute - #democrat, # republican
  '''

  # Array of all attributes without 'democrat' or 'republican' (Class)
  # att = examples[1].keys()
  # del att['Class']
  #
  # l = len(examples)


  # for item in examples:
  #     for attribute in att:
  #         if value of example[attribute] in dict:
  #
  #             count of item in dictionary +1
  #
  #             if class of item is already included
  #                 class +=1
  #             else:
  #                 class = 1
  #         else:
  #         count of item = 1
  #         class of item +1

  countDict = {}

  #Going through each example
  for example in examples:
      #Getting all the attributes from that example
      for attribute, value in example.iteritems():
          #Checking if that one attribute has already been looked at for other examples
          if attribute in countDict.keys():
              #if it has that attribute, check to see if that value has already been looked at for that attribute for other examples
              if value in countDict[attribute].keys():
                  #If it has that value, check to see if that value of the targetAtt has been looked at for that value of that attribute for other examples
                  if example[targetAtt] in countDict[attribute][value].keys():
                      #If that value of that target attribute has already been looked at for this value of this attribute of this example, just incrememt it
                      countDict[attribute][value][example[targetAtt]] += 1

                  else:
                      #Otherwise add that value of that target attribute to the dictionary
                      countDict[attribute][value][example[targetAtt]] = 1
              else:
                  #Does not have the value, add that value and value of the TargetAtt to the dictionary
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
  best = ""

  for attribute, value in countDict.iteritems():
      newGain = 0.0
      attributeCount =0.0
      valueResults = []
      valueTotals = []
      for val, targetAtts in value.iteritems():
          itemCounts = []
          valTotal = 0.0
          valResult = 0.0
          for item, count in targetAtts.iteritems():
              valTotal += count
              itemCounts.append(count)

          for num in itemCounts:
              valResult += (num/valTotal) * math.log((num/valTotal),2)

          attributeCount += valCount
          valueResults.append(valResult)
          valueTotals.append(valTotal)

      for counter, num in enumerate(valueResults):
          newGain += (valueTotals[counter]/len(examples)) * num

      if abs(newGain) > gain:
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
      exclass = evaluate(node,example)
      if exclass  == example['Class'].value():
        count+=1
    acc = count/len(examples)
  return acc


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
