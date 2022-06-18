#!/usr/bin/env python
# coding: utf-8

# # Linked List

# In[2]:


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def printingLinkedList(self):
        if self.head is None:
            print('LL is empty')
            return
        itr = self.head
        llist = ''
        while(itr):
            llist += str(itr.data) + "-->"
            itr = itr.next
        print(llist)
        
    def getLength(self):
        count = 1
        itr = self.head
        while itr.next:
            count+=1
            itr = itr.next
        return count
            
    def insertAtEnd(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
        else:    
            itr = self.head
            while itr.next:
                itr=itr.next
            node = Node(data, None)
            itr.next = node
            
    def insertAt(self, index, data):
        if index < 0 or index > self.getLength()+1:
            raise Exception("Enter the right index")
        elif index == 0:
            self.insertAtBeginning(data)
            return
        elif index == self.getLength()+1: ##If user enters exactlenght of LL(bcaz--no of nodes+1 = exactlength), we must add that node at the end..
            self.insertAtEnd(data)
            return
        else:
            count=1
            itr = self.head
            while itr:
                if count == index-1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                count+=1
                itr=itr.next
            
    def removeAt(self, index):
        if index < 0 or index > self.getLength():
            raise Exception("Index enter is either negative or out of bound!")
        elif index == 0:
            self.head = self.head.next
            return
        elif index == self.getLength():
            itr = self.head
            prevNode=Node
            while itr.next:
                prevNode = itr ## Just keep a copy of previous so that we could make 'next' as 'None' when itr is at LastNode
                itr = itr.next
            prevNode.next = None
            return
        else:
            print("Not so good")
            count = 1
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = itr.next.next
                    return
                itr = itr.next
                count+=1
                
    def insertValuesAtOnce(self, list_of_data): #This function creates a new Linked List. since there is (self.head=None)
        self.head = None
        for data in list_of_data:
            self.insertAtEnd(data)
        


# In[ ]:





# In[4]:


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBeginning(90)
    ll.insertAtBeginning(12)
    ll.insertAtEnd(99)
    ll.insertAtEnd(100)
    ll.insertAt(3,255)
    ll.insertAt(6,666)
    ll.printingLinkedList()
    print(ll.getLength())
    print('======After removing===========')
    ll.removeAt(6)
    ll.printingLinkedList()
    print(ll.getLength())
    print("=====Below used is insertValuesAtOnce=========")
    ll.insertValuesAtOnce(['Nexon', 'Altroz','SAFARI','Harrier','Punch',"Tiago"])
    ll.printingLinkedList()


# # Stack 
# https://docs.python.org/3/library/collections.html#deque-objects

# In[ ]:





# # Trees

# In[53]:


class TreeNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        
    def addChild(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                childNode = TreeNode(data)
                self.left = childNode
        else:
            if self.right:
                self.right.addChild(data)
            else:
                childNode = TreeNode(data)
                self.right = childNode
        
    def buildTree(self, elements):
        rootNode = TreeNode(elements[0])
        for i in range(1, len(elements)):
            rootNode.addChild(elements[i])
        return rootNode
        
                
    def inOrderTraversal(self): # returns set(dataType). Will always be in ascending order!
        elements_of_tree = []
        
        #visiting left tree
        if self.left:
            elements_of_tree+=self.left.inOrderTraversal()
        
        #visiting root node
        elements_of_tree.append(self.data)
        
        if self.right:
            elements_of_tree+=self.right.inOrderTraversal()
        
            
        return elements_of_tree
    
    def isValuePresent(self, value):
        if value == self.data:
            return True
        if value < self.data: # value maybe in left subtree
            if self.left:
                return self.left.isValuePresent(value) #'return is imp here, else returns NONE for any value other than root'
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.isValuePresent(value) #'return is imp here, else returns NONE for any value other than root'
            else:
                return False
            
    def findMinValue(self): #=======There is no ".left" here in this function=======
        if self.left is None:
            return self.data
        else:
            return self.left.findMinValue()
            
    def findMaxValue(self): #=======There is no ".right" here in this function=======
        if self.right is None:
            return self.data
        else:
            return self.right.findMaxValue()
    
    def deleteValue(self, value):
        if value < self.data: #Code for traversing in left subtree
            if self.left:
                self.left = self.left.deleteValue(value)
        elif value > self.data: #Code for traversing in right subtree
            if self.right:
                self.right = self.right.deleteValue(value)
        else:
            if self.left is None and self.right is None: #If there is no 'value' returns None
                return None
            if self.left is None: 
                return self.right  # Returns a tree with right sub-tree(which inturn is a tree itself)
            if self.right is None: 
                return self.left   #Returns a tree with left-sebtree(hich inturn is a tree itself)
            
            #===================APPROCH 1=========================================
            #min_value = self.right.findMinValue() ## Here, just find minimum value in right-subtree and assign it to....
            #self.data = min_value                 ## ...."self.data"(creates a duplicate node). Now delete the..
            #self.right = self.right.deleteValue(min_value)  #.. minValue in the right subtree!!
            
            #===================APPROCH 2=========================================
            max_value = self.left.findMaxValue()  ##Here, just find maximum value in left-subtree and assign it to..
            self.data = max_value              ##.. self.data(create a duplicate node). Now, delete the maxValue in
            self.left = self.left.deleteValue(max_value) ## ..the left sub-tree.!!
        return self
            


# In[60]:


if __name__ == "__main__":
    numbers=[10,90,77,23,57,44,50,87,99,500]
    tree = TreeNode()
    numbers_tree = tree.buildTree(numbers)
    print(numbers_tree.inOrderTraversal())
    print(numbers_tree.isValuePresent(4))
    numbers_tree.addChild(4)
    print("Minimum value is:",numbers_tree.findMinValue())
    print("Maximum value is:",numbers_tree.findMaxValue())
    #print("After deleting 10:", numbers_tree.deleteValue(10))
    print("Before deleting 23:", numbers_tree.inOrderTraversal())
    print("After deleting 23:", numbers_tree.deleteValue(23).inOrderTraversal())
    
    print("=====================--------------------====================") 
    
    tata_cars = ["Nexon","Safari","Harrier","Altroz","Punch","Tiago","Indica"]
    tata_carsTree = tree.buildTree(tata_cars)
    print(tata_carsTree.isValuePresent("Safari"))
    print(tata_carsTree.isValuePresent("Alto"))
    tata_carsTree.addChild("Punto")
    print(tata_carsTree.inOrderTraversal())


# In[10]:


print(tree)


# In[62]:


print("Hello world")


# # Binary Search

# In[73]:


def BinarySearchRecursive(num_list, value_to_find, left, right):
    if left > right:
        return -1
    
    mid_index = (left+right)//2
    if mid_index > len(num_list) or mid_index < 0:
        return -1
        
    mid_element = num_list[mid_index]
    
    if mid_element == value_to_find:
        return mid_index
    elif value_to_find < mid_element:
        #right = mid_index -1
        return BinarySearchRecursive(num_list, value_to_find, left, (mid_index-1))
    else:
        #left = mid_index + 1
        return BinarySearchRecursive(num_list, value_to_find, (mid_index + 1) ,right)
    # return BinarySearchRecursive(num_list, value_to_find, left, right)
        
    


# In[77]:


number_list = [1,3,5,34,44,65,69,88]
BinarySearchRecursive(number_list, 32, 0, (len(number_list)-1))


# In[97]:


def AgainBinaryREcursiveSearch(num_list, value_to_find, left, right):
    if left > right:
        return -1
    
    mid_index = (left + right)//2
    if mid_index < 0 or mid_index > len(num_list):
        return -1
    mid_element = num_list[mid_index]
    
    if value_to_find == mid_element:
        return mid_index
        #print("It is at place " +str(mid_index))
    elif value_to_find < mid_element:
        #right = mid_index - 1
        return AgainBinaryREcursiveSearch(num_list, value_to_find, left, (mid_index-1))
    else:
        #left = mid_index + 1
        return AgainBinaryREcursiveSearch(num_list, value_to_find, (mid_index+1), right)   


# In[103]:


number_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
AgainBinaryREcursiveSearch(number_list, 15, 0, (len(number_list)-1))


# # BubbleSort

# In[167]:


def BubbleSort(num_list):
    size = len(num_list)
    #print(size)
    for k in range(1):
        for i in range(size-1-k):
            if num_list[i] > num_list[i+1]:
                temp = num_list[i]
                num_list[i] = num_list[i+1]
                num_list[i+1] = temp


# In[168]:


num_list = [89,84,67,76,32,14]
BubbleSort(num_list)
print(num_list)


# In[169]:


num_list = [84, 67, 76, 32, 14, 89]
BubbleSort(num_list)
print(num_list)


# In[117]:


def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break


# In[120]:


num_list = [89,84,67,76,32,14]
print(bubble_sort(num_list))


# In[ ]:




