class Node:
    v = "" 
    children = []
    
  def __init__(self,v,attributes):
        self.value = v
        self.children = attributes.keys()
    
  def addBranch(self,tree,val):
  	self.value = val; 
  	self.children = tree