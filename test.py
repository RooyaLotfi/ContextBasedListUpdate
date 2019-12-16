from typing import Tuple
import string


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        self.probability = 0

    def get_data(self):
        return self.data

    def set_data(self, val):
        self.data = val

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, val):
        self.next_node = val

    def get_probability(self):
        return self.probability

    def set_probability(self, val):
        self.probability = val


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def make_alphabet_list(self):
        for l in list(string.ascii_lowercase):
            new_node = Node(l, self.head)
            self.head = new_node
            self.size += 1

    def get_size(self):
        return self.size

    def add_node(self, data):
        curr = self.head
        while curr:
            if curr.get_data() == data:
                return False, "already in the list"
            curr = curr.get_next_node()

        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1
        return True, "Added to the list"

    def print_node(self):
        curr = self.head
        while curr:
            print(curr.get_data())
            curr = curr.get_next_node()

    def remove_node(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.get_data() == value:
                if prev:
                    prev.set_next_node(curr.get_next_node())
                else:
                    self.head = curr.get_next_node()
                return True

            prev = curr
            curr = curr.get_next_node()
        return False

    def find_node(self, value):
        curr = self.head
        while curr:
            if curr.get_data() == value:
                return True
            curr = curr.get_next_node()
        return False

    def get_list(self):
        curr = self.head
        all_list = []
        while curr:
            all_list.append(curr.get_data())
            curr = curr.get_next_node()
        return all_list

    def find_probability(self, value):
        curr = self.head
        while curr:
            if curr.get_data() == value:
                return curr.get_probability()
            curr = curr.get_next_node()
        return 0


def update_probability(list):
    curr = list.head
    index = 0
    n = len(list.get_list())-1
    while curr:
        curr.set_probability(index/n)
        index = index + 1
        curr = curr.get_next_node()


class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """
    counter = 0

    def __init__(self, char):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1


def add(root_node, word: str):
    """
    Adding a word in the trie data structure
    """
    node = root_node
    found_in_child = False
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                node = child
                found_in_child = True
                break
        # We did not find it so add a new child
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


def _add(root_node, word: str):
    """
    Adding a word in the trie structure
    """
    node = root_node
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
        # We did not find it so add a new child
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True


def find_prefix(root_node, prefix: str) -> Tuple[bool, int]:
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root_node
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root_node.children:
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


def is_in_list(root_node, prefix: str):
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
    """
    node = root_node
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root_node.children:
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


def change_point_probability():

    return


def find_weight(root_node, prefix: str):
    """
    Check and return
      2. If yes then how may words actually have the prefix
    """
    node = root_node
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root_node.children:
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
            if find_weight(root, nums[i]) > find_weight(root,nums[i + 1]):
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
    return nums


def update_list(linked_list, str, context_len):
    j = len(str) - context_len + 1
    max_weight = -1
    candid_items = []
    list_iter = linked_list.get_list()

    while j <= len(str):
        # if candid_items is only one item then we need to sort them based on their number
        # of occurrence in the input that is why we separate them
        if j < len(str):
            candid_items = []
            f = 0
            for i in list_iter:
                in_list, weight = find_prefix(root, str[j:len(str)] + i)

                if weight == max_weight:
                    #print(str[j:len(str)] + i, weight)
                    f = f + 1
                    candid_items.append(i)
                if max_weight < weight:
                    #print(str[j:len(str)] + i, weight)
                    f = 1
                    max_weight = weight
                    candid_items = []
                    candid_items.append(i)
            #print("adding and removing ", str[j])
            linked_list.remove_node(str[j])
            linked_list.add_node(str[j])
        else:
            # sort items by number of occurance
            #print("candid_items before :", candid_items)
            bubble_sort(candid_items)
            #print("candid_items after", candid_items)
            # when swapping items in the list in a function the actual list changes

        if f == 1:  # age candid_items 1 item dasht
            j = j + 1
            while j < len(str):
                #print("adding and removing ", str[j])
                linked_list.remove_node(str[j])
                linked_list.add_node(str[j])
                j = j + 1
            #print(" i is : ", candid_items[0])
            #print("adding and removing ", candid_items[0])
            linked_list.remove_node(candid_items[0])
            linked_list.add_node(candid_items[0])
            candid_items = []
            break

        j = j + 1
    # if all items have the same weight then candid_items is 26
    # if candid_items is 26 it means that all patterns had the same weights or a new character has been
    # added to the front like it was : "aaababa" now it is "aaababac" so we should check if
    # the last item is new or previously seen

    for candid in candid_items:
        #print("adding and removing", candid)
        linked_list.remove_node(candid)
        linked_list.add_node(candid)


def contextbased_listupdate(root_node, str, context_len):

    for i in range(context_len):
        substr = str[i:context_len]
        #print(substr)
        _add(root_node, substr)

    for j in range(context_len, len(str)):
        for k in range(context_len):
            substr = str[j - context_len + 1 + k: j + 1]
            add(root_node, substr)

        print("**************list before******************")
        myList.print_node()
        update_list(myList, str[j - context_len + 1: j + 1], context_len)
        print("probability of ",str[j], " of being a change point is : ", myList.find_probability(str[j]))
        print("********adding node********")
        print("string is ", str[j - context_len + 1: j + 1])
        print("node is : ", str[j])
        print("**************list after******************")
        myList.print_node()
        update_probability(myList)
        #str[j]
        #myList.print_node()


if __name__ == "__main__":

    root = TrieNode('*')
    myList = LinkedList()
    myList.make_alphabet_list()

    str = "aababcab"

    index = 3
    contextbased_listupdate(root, str, index)

    # print(find_weight(root,"ab"))
    # myList.print_node()




