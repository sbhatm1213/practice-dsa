

class Node:
  """
  This is an object to store a single node in a linked list.
  
  Attributes:
  data: data stored in the node
  next_node: reference to the next node in the linked list
  """

  def __init__(self, data, next_node=None):
    self.data = data
    self.next_node = next_node

  def __repr__(self):
    return f"Node(data={self.data}, next_node={self.next_node})"


class SinglyLinkedList:
  """
  Linear DataStructure that stores values in nodes.
  The list maintains a reference to the first node, also called head.
  Each node points to the next node in the list.

  Attributes:
  head: first node of the list
  """

  def __init__(self):
    self.head = None
  
  def is_empty(self):
    return self.head == None
  
  def size(self):
    """
    Returns number of nodes in the linked list.
    
    Takes linear time, O(n) - because it has to traverse full list.
    """
    current = self.head
    count = 0
    
    while current:
      count += 1
      current = current.next_node
      
    return count

  def add_to_start(self, data):
    """
    Adds a new node containing data to the head of the linked list.

    Takes constant time, O(1) - bcoz no elements to be traversed , just add to head.
    """
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

  def __repr__(self):
    current = self.head
    list_to_print = []
    while current:
    #   print(current)
    #   exit()  
      list_to_print.append(repr(current.data))
      current = current.next_node
    return " -> ".join(list_to_print)


l = SinglyLinkedList()
n1 = Node(10)
# print(n1)
l.head = n1
print(l.size()) # 1
l.add_to_start(3)
print(l.size()) # 2
l.add_to_start(8)
print(l.size()) # 3

print(l)  #  8 -> 3 -> 10
