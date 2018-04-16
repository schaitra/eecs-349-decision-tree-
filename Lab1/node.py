


class Node:

  # attribute = ""
  # children = {}

    def __init__(self):
        self.attribute = None
        self.children = {}
        self.label=None

    def addBranch(self, tree, val):
        self.children[val] = tree

    def addLabel(self,label):
    	self.label=Label
    
 # Node1:
 # attribute = physician-fee-freeze
 # children = {y: Node2, n: Node3, ?: 'democrat'}

 # Node2:
 # attribute = anti-satellite-test-ban
 # children = {y: 'democrat', n: 'republican', ?: 'democrat'}

 # Node3:
 # attribute = education-spending
 # children = {y: 'republican', n: 'republican', ?: 'democrat'}



