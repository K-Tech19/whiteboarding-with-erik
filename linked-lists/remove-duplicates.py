class Node:
  def __init__(self, data):
    self.next = None
    self.__data = data

  def set_data(self, val):
    self.__data = val

  def get_data(self):
    return self.__data

  def append(self, val):
    end = Node(val)
    n = self
    while (n.next):
      n = n.next
    n.next = end


# Remove Dups: Write code to remove duplicates from an unsorted linked list
from collections import defaultdict
def remove_dups(front):
  dd = defaultdict(bool)
  temp = front
  dd[temp.get_data()] = True
  while (temp.next):
    # check the value of next Node
    # print("CHECKING", temp.get_data())
    if (dd[temp.next.get_data()]):
      #if found in dictionary, remove it
      temp.next = temp.next.next
    else:
      dd[temp.next.get_data()] = True
      temp = temp.next
  print(dd)

ll = Node(1)
ll.append(1)
ll.append(7)
ll.append(3)
ll.append(3)
ll.append(1)

remove_dups(ll)

node = ll
while node.next:
  print(node.get_data())
  node = node.next
print(node.get_data())