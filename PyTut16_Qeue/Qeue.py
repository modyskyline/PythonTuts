'''
Created on Jul 16, 2016

@author: modys
'''

from Node import Node

class Qeue:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.first = None
        self.last = None
    
    def isEmpty(self):
        return self.first is None
    
    def __str__(self):
        if self.isEmpty():
            return"The list is Empty"
        
        currentNode=self.first
        strings="The list is "
        
        while currentNode is not None:
            strings+=str(currentNode.getData())
            strings+="--> "
            currentNode=currentNode.getNextNode()
            
        strings+="None"
        
        return strings
            
    def qeue(self,value):
        newNode=Node(value)
        if self.isEmpty():
            self.first = self.last = newNode
        else:
            self.last.setNextNode(newNode)
            self.last = newNode
           
        print(self.__str__()) 
        
    def deqeue(self):
        if self.isEmpty():
            raise(IndexError,"Remove is Error")
        current = self.first
        self.first=self.first.getNextNode()
        current.setNextNode(None)
        print(self.__str__())
                
    def getCount(self):
        
        if self.isEmpty():
            raise(ValueError,"List is empty")
            
        current = self.first
        countList=0
        
        while current is not None :
            countList+=1
            current = current.getNextNode()
        return countList
                
            
    