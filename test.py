from typing import Tuple
import numpy as np
import string


class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def make_alphabet_list(self):
        for l in list(string.ascii_lowercase):
            newNode = Node(l, self.head)
            self.head = newNode
            self.size += 1

    def get_size(self):
        return self.size

    def addNode(self, data):
        curr = self.head
        while curr:
            if curr.getData() == data:
                return False, "already in the list"
            curr = curr.getNextNode()

        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True, "Added to the list"

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.getData())
            curr = curr.getNextNode()

    def removeNode(self, value):

        prev = None
        curr = self.head
        while curr:
            if curr.getData() == value:
                if prev:
                    prev.setNextNode(curr.getNextNode())
                else:
                    self.head = curr.getNextNode()
                return True

            prev = curr
            curr = curr.getNextNode()
        return False

    def findNode(self, value):
        curr = self.head
        while curr:
            if curr.getData() == value:
                return True
            curr = curr.getNextNode()
        return False

    def get_list(self):
        curr = self.head
        all_list = []
        while curr:
            all_list.append(curr.getData())
            curr = curr.getNextNode()
        return all_list


class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """
    counter = 0

    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1


def add(root, word: str):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                #print("character is : ", char)
                #print("node.child is :", child.char)
                #print(child.char == char)
                #print("\n")
                # We found it, increase the counter by 1 to keep track that another
                # word has it as well
                # And point the node to the child that contains this char

                node = child
                found_in_child = True
                break
        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node

    if found_in_child:
        node.counter = node.counter + 1

    # Everything finished. Mark it as the end of a word.
    # node.counter += 1
    node.word_finished = True


def _add(root, word: str):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found it, increase the counter by 1 to keep track that another
                # word has it as well
                child.counter += 1
                # And point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False, 0
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return True, node.counter

def is_in_list(root, prefix: str):
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False, 0
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return True

def find_weight(root, prefix: str):
    """
    Check and return
      2. If yes then how may words actually have the prefix
    """
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return 0
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return node.counter

def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            #print(find_weight(root, nums[i]) < find_weight(root,nums[i + 1]))
            if (find_weight(root, nums[i]) > find_weight(root,nums[i + 1])):
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
    return nums


def update_list(myList,str, index):
    j = len(str) - index + 1
    max = -1
    str_max = ""
    candid = []

    list_iter = myList.get_list();
    while j < len(str)+1:
        # if candid is only one item then we need to sort them based on their number
        # of occurance in the input that is why we separate them
        if (j <len(str)):
            candid = []
            f = 0

            for i in list_iter:
                in_list, weight = find_prefix(root, str[j:len(str)] + i)

                if weight == max:
                    print(str[j:len(str)] + i, weight)
                    f = f + 1
                    candid.append(i)
                if max < weight:
                    print(str[j:len(str)] + i, weight)
                    f = 1
                    str_max = str[j:len(str)] + i
                    max = weight
                    candid = []
                    candid.append(i)
            print("adding and removing ", str[j])
            myList.removeNode(str[j])
            myList.addNode(str[j])
        else:
            # sort items by number of occurance
            print("candid before :", candid)
            bubble_sort(candid)
            print("candid after", candid) # when swaping items in the list in a function the actual list changes

        if f == 1:  # age candid 1 item dasht
            j = j + 1
            while j < len(str):
                #print("J is : ", str[j])
                print("adding and removing ", str[j])
                myList.removeNode(str[j])
                myList.addNode(str[j])
                j = j + 1
            print(" i is : ", candid[0])
            print("adding and removing ", candid[0])
            myList.removeNode(candid[0])
            myList.addNode(candid[0])
            candid = []
            break

        # candid = []
        j = j + 1
    # if all itmes have the same weight then candid is 26
    # if candid is 26 it means that all patterns had the same weights or a new character has been
    # added to the front like it was : "aaababa" now it is "aaababac" so we should check if
    # the last item is new or previously seen

    for candids in candid:
        print("adding and removing", candids)
        myList.removeNode(candids)
        myList.addNode(candids)

    #if f != 26:
     #   for candids in candid:
      #      print("adding and removing",candids)
       #     myList.removeNode(candids)
        #    myList.addNode(candids)
    #else:
     #   print("no candids sort by number of occurance of each character")
      #  print("candid is : ", candid)

        #print("CANDID BEFORE :", candid)
        #x = bubble_sort(candid)
        #print("CANDID AFTER :",x)
        #for candids in x:
         #   myList.removeNode(candids)g
          #  myList.addNode(candids)

def make_tri(root, str, index):

    for i in range(index):
        substr = str[i:index]
        print(substr)
        _add(root, substr)

    for j in range(index, len(str)):
        for k in range(index):
            substr = str[j - index + 1 + k: j + 1]
            add(root, substr)

        update_list(myList, str[j - index + 1: j + 1], index)
        myList.printNode()

if __name__ == "__main__":
    root = TrieNode('*')
    myList = LinkedList()
    myList.make_alphabet_list()

    str = "aababca"

    index = 3
    make_tri(root, str, index)

    #sorted = bubble_sort(['b', 'a'])
    #print(sorted)




