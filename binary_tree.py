#!/usr/local/bin python3

class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left_child = left
        self.right_child = right

    def insert(self,data):
        if self.data:
            if data > self.data:
                if self.left_child is None:
                    self.left_child = Node(data)
                else:
                    self.left_child.insert(data)
            elif data < self.data:
                if self.right_child is None:
                    self.right_child = Node(data)
                else:
                    self.right_child.insert(data)
        else:
            self.data = data

    def lookup(self,data,parent=None, counter = 0):
        if data > self.data:
            if self.left_child is None:
                return "Node doesn't exist bruh"
            counter += 1
            return self.left_child.lookup(data,self,counter = counter)
        elif data < self.data:
            if self.right_child is None:
                return "Node doesn't exist bruv"
            counter += 1
            return self.right_child.lookup(data,self, counter = counter)
        else:
            return self.data,parent.data,"Depth = " + str(counter)
    