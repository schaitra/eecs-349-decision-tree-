class Node:
  # attribute = "" 
  # children = {}
    
  def __init__(self,att):
    self.attribute = att
    self.children = {}
    
  def addBranch(self,tree, val):
  	self.children[val] = tree


 # Node1:
 # attribute = physician-fee-freeze
 # children = {y: Node2, n: Node3, ?: 'democrat'}

 # Node2:
 # attribute = anti-satellite-test-ban
 # children = {y: 'democrat', n: 'republican', ?: 'democrat'}

 # Node3:
 # attribute = education-spending
 # children = {y: 'republican', n: 'republican', ?: 'democrat'}



