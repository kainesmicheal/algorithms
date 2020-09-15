import java.util.*;

class Program {
  static class DoublyLinkedList {
    public Node head;
    public Node tail;

    public void setHead(Node node) {
      if (head == null) {
				head = node;
				tail = node;
				return;
			}
			insertBefore(head, node);
    }

    public void setTail(Node node) {
      if (tail == null) {
				setHead(node);
				return;
			}
			insertAfter(tail, node);
    }

    public void insertBefore(Node node, Node nodeToInsert) {
      if (nodeToInsert == head && nodeToInsert == tail) {
					return;
			}
			remove(nodeToInsert);
			nodeToInsert.prev = node.prev;
			nodeToInsert.next = node;
			
			if (node.prev == null) {
				head = nodeToInsert;
			} else {
				node.prev.next = nodeToInsert;
			}		
			node.prev = nodeToInsert;
    }

    public void insertAfter(Node node, Node nodeToInsert) {
      if (nodeToInsert == head && nodeToInsert == tail) {
				return;
			}
			remove(nodeToInsert);
			nodeToInsert.prev = node;
			nodeToInsert.next = node.next;
			if (node.next == null) {
				tail = nodeToInsert;
			} else {
				node.next.prev = nodeToInsert;
			}
			node.next = nodeToInsert;
    }

    public void insertAtPosition(int position, Node nodeToInsert) {
      if (position == 1) {
				setHead(nodeToInsert);
				return;
			}
			Node currentNode = head;
			int currentPosition = 1;
			while (currentNode != null && currentPosition++ != position) {
				currentNode = currentNode.next;
			}
			if (currentNode != null) {
				insertBefore(currentNode, nodeToInsert);
			} else {
				setTail(nodeToInsert);
			}
    }

    public void removeNodesWithValue(int value) {
     	Node node = head;
			while (node != null) {
				Node next = node.next;
				if (node.value == value) {
					remove(node);
				}
				node = next;
			}
    }

    public void remove(Node node) {
      if (head == node){
				head = head.next;
			}
			if (tail == node) {
				tail = tail.prev;
			}
			disassembleNode(node);
		}
		public void disassembleNode(Node node) {
			if (node.prev != null) {
				node.prev.next = node.next;
			}
			if (node.next != null) {
				node.next.prev = node.prev;
			}
			node.prev = null;
			node.next = null;
		}

    public boolean containsNodeWithValue(int value) {
      Node currentNode = head;
			while(currentNode != null && currentNode.value != value) {
				currentNode = currentNode.next;
			}
      return currentNode != null;
    }
  }

  // Do not edit the class below.
  static class Node {
    public int value;
    public Node prev;
    public Node next;

    public Node(int value) {
      this.value = value;
    }
  }
}
// time complexity for insertion and iterartion is o(n) or (d) other methodsa are o(1)
// space complexity is o(1) as everthing is in place operations
