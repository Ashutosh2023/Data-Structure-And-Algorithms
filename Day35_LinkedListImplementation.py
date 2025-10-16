class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Insert a new node at the end."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:      # move to the last node
            current = current.next
        current.next = new_node  # link last node to new one

    def prepend(self, value):
        """Insert a new node at the beginning."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        """Print the list in a readable format."""
        current = self.head
        if not current:
            print("Empty list")
            return

        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    def find(self, value):
        """Search for a value and return the node if found."""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        """Delete the first occurrence of value."""
        if self.head is None:
            return  # empty list

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next


ll = LinkedList()
ll.append(40)
ll.delete(10)
ll.display()


# constructor to initialize a new node with data
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Create the first node (head of the list)
head = Node(10)

# Link the second node
head.next = Node(20)

# Link the third node
head.next.next = Node(30)

# Link the fourth node
head.next.next.next = Node(40)

# printing linked list
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next