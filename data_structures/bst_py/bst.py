from enum import Enum
import os

class BST:
    # Binary Search Tree
    def __init__(self) -> None:
        self.root = None # Node() # pointer to root's node of the BST
        self.no_of_phones = 0 # the total number of Phones

    def __str__(self) -> str:
        return f'Root node = {self.root}, Total number of Phones in the store = {self.no_of_phones}'


class Phone:
    def __init__(self) -> None:
        self.name = '' # type of phone
        self.price = 0 # price
        self.quantity = 0 # Quantity in stock

    def __init__(self, name, price, quantity) -> None:
        self.name = name # type of phone
        self.price = price # price
        self.quantity = quantity # Quantity in stock

    def __str__(self) -> str:
        return f'Phone name : {self.name}, Price : {self.price}, Quantity left in stock : {self.quantity}'


class Node:
    def __init__(self) -> None:
        self.item = None # Phone()
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f'Phone node = {self.item}'


def createEmptyBST ():
    # This function creates an empty BST, with root pointing to null initially, and returns this instance of BST class.
    return BST()

def insertIntoBST (bst, phone):
    # This function inserts a phone record (as per the price of {phone} variable) at the appropriate position in the BST {bst}, and then returns the same BST (not a copy).

    def insert (node, key_node, success=True):
        if node == None:
            # If BST is empty, given node becomes root.
            return key_node, success

        if node.item.price == key_node.item.price:
            # Duplicate record check
            # As per our Assumption, name and price pair is unique, hence no separate check for name
            return node, False
        elif node.item.price < key_node.item.price:
            # If phone's price is less than current nodes price: Insert the node at right subtree
            if node.right == None:
                node.right = key_node
            else:
                node.right, success = insert(node.right, key_node, success)
        else:
            # If phone's price is less than current nodes price: Insert the node at left subtree
            if node.left == None:
                node.left = key_node
            else:
                node.left, success = insert(node.left, key_node, success)

        return node, success

    # Create a node to add it in BST
    key_node = Node()
    key_node.item = phone

    bst.root, success = insert(bst.root, key_node)

    # Don't update phone count for duplicate record.
    if success:
        bst.no_of_phones += 1

    return bst, success

def findInBST (bst, cost): 
    # This function finds whether there exists a Phone of price {cost}, and if there does, return that Phone variable, if not, return null.

    def search(node, key):
        # If node == None, key is not present in BST
        if node is None:
            return None

        # Key found
        if node.item.price == key:
            return node.item

        # If key not found, traverse left/right
        if node.item.price < key:
            # Key is greater than node's key: search right subtree
            if node.right == None:
                return None
            else:
                return search(node.right, key)
        else:
            # Key is lesser than node's key: search left subtree
            if node.left == None:
                return None
            else:
                return search(node.left, key)

    return search(bst.root, cost)

def search_max(node):
    # This function is used by findMaxPrice & findSecondMaxPrice functions
    if node.right == None:
        return node
    else:
        return search_max(node.right)

def findMaxPrice (bst):
    # This function returns the Phone with maximum price amongst all phones available in the store.

    if bst.root == None:
        print("No records in BST")
        return None

    return search_max(bst.root).item

def search_min(node):
    # This function is used by findMinPrice & findSecondMinPrice functions
    if node.left == None:
        return node
    else:
        return search_min(node.left)

def findMinPrice (bst):
    # This function returns the Phone with minimum price amongst all phones available in the store.

    if bst.root == None:
        print("No records in BST")
        return None

    return search_min(bst.root).item

def findSecondMaxPrice (bst):
    # This function returns the Phone with second highest price amongst all phones available in the store.
    if bst.root == None:
        print("No records in BST")
        return None

    if bst.root.right == None and bst.root.left == None:
        # Only one node in this BST. No second largest price.
        print("Only one record is found in the BST, hence second costliest is None")
        return None

    # At this point, BST definitely has more than one phone record
    # Second max element is in left sub tree
    if bst.root.right == None:
        return search_max(bst.root.left).item
    
    # Second max element may be root or on right sub tree of root
    if bst.root.right != None:
        first_largest = bst.root.right
        second_largest = bst.root

        # Traverse till the last right subtree and get largest and second largest nodes in the right links
        while(first_largest.right != None):
            second_largest = first_largest
            first_largest = first_largest.right

        # If the largest element has left subtree, then the second largest element will be the largest element in left subtree
        if first_largest.left != None:
            second_largest = search_max(first_largest.left)

    return second_largest.item

def findSecondMinPrice (bst) :
    # This function returns the Phone with second lowest price amongst all phones available in the store.
    if bst.root == None:
        print("No records in BST")
        return None

    if bst.root.right == None and bst.root.left == None:
        # Only one node in this BST. No second lowest price.
        print("Only one record is found in the BST, hence second cheapest phone is None")
        return None

    # At this point, BST definitely has more than one phone record
    # Second min element is in right sub tree
    if bst.root.left == None:
        return search_min(bst.root.right).item
    
    # Second min element may be root or on left sub tree of root
    if bst.root.left != None:
        first_lowest = bst.root.left
        second_lowest = bst.root

        # Traverse till the last left subtree and get lowest and second lowest nodes in the left links
        while(first_lowest.left != None):
            second_lowest = first_lowest
            first_lowest = first_lowest.left

        # If the lowest element has right subtree, then the second lowest element will be the lowest element in right subtree
        if first_lowest.right != None:
            second_lowest = search_min(first_lowest.right)

    return second_lowest.item


def printAllPhoneDetails(bst) :
    if bst.root is None:
        print("BST is empty")
        return
    # Inorder triversal to print the BST
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.item)
            inorder_traversal(root.right)
    inorder_traversal(bst.root)

class ListNode:
    def __init__(self, value):
        self.value = value   # price
        self.next = None

def sortedListFromBST(root):
    # Helper function for in-order traversal
    def inorder_traversal(node):
        nonlocal prev, head
        if node:
            inorder_traversal(node.left)
            # Create a new ListNode for the current node's value
            new_node = ListNode(node.item.price)
            if not head:
                head = new_node
            else:
                prev.next = new_node
            prev = new_node
            inorder_traversal(node.right)

    head = None  # head of the linked list
    prev = None  # pointer to the previous node
    inorder_traversal(root)
    return head

# write output to a file
def write_to_file(filename, data):
    file = open(filename, 'w')
    try:
        file.write(data)
    finally:
        file.close()

def listAllPrices (bst) :
    # Generate a linked list of prices of all Phones in increasing order, and return the same. You will have to implement all the required functionality of the Linked List data structure independently for this function. Once the Linked List is created, print it in the o/p file.
    # Get the sorted linked list from the BST
    if bst.root  is None:
        print("BST is  empty")
        return
    sorted_list_head = sortedListFromBST(bst.root)

    # Check if output file already exists
    output_file = input("Enter filename as *.txt, to save prices :\n")
    if os.path.exists(output_file):
        print(f"{output_file} already exists.")
        option = input("Do you want to overright the file: y/n\n").lower()
        if option != "y" :
            return

    output_data = ""
    # Print the sorted linked list
    current = sorted_list_head
    while current:
        output_data += str(current.value) + '\n'
        current = current.next
    # Write the output to the file
    write_to_file(output_file, output_data)

def modifyQtyInStock (bst, name, price, new_qty) :
    # Using this function, you should find the entry in the BST {bst} having {name} and {price} and set its quantity left in stock field to new_qty.
    def find_and_modify(node):
        if not node:
            return False
        if (node.item.name == name) and (node.item.price == price):
            node.item.quantity = new_qty
            return True
        elif node.item.price < price :
            return find_and_modify(node.right)
        else:
            return find_and_modify(node.left)

    found = find_and_modify(bst.root)
    if found:
        print(f"Phone : {name}, Price: {price}, Quantity: {new_qty}")
    else:
        print(f"No phone found with name '{name}' and price '{price}'")

def deleteFromBST (bst, name, price) :
    # This function is responsible for deleting a Phone entry from the BST, having same name and price as {name} and {price} respectively.

    def delete(node, name, price, success=True, display=True):
        if node is None:
            print("Node is not found in the BST")
            return node, False
        
        if price < node.item.price:                                                          #Check if price is less than key node price
            node.left, success = delete(node.left, name, price,display=display)              #call recursively to delete the node from left sub tree
            

        elif price > node.item.price:                                                        #Check if price is greater than key node price
            node.right, success = delete(node.right, name, price,display=display)            #call recursively to delete the node from right sub tree

            

        elif price == node.item.price and node.item.name != name:                            #Check if name and price of the phone matches with key node price and name
            if display:
                print("Node is not found in the BST")
            return node, False

        else:
            if node.right is None and node.left is None:                                     #Check if the node has no children
                if display:
                    print("Deleted phone details \n", node.item) 
                node = None                                                                  #delete the node
                return node, success
            elif node.left is None and node.right is not None:                               #Check if node has no left child
                current = node.right                                                         #Assign key node to right child
                if display:                                                                      
                    print("Deleted phone details \n", node.item)                
                node = None                                                                  #delete the node                      
                return current, success
            
            elif node.right is None and node.left is not None:                               #Check if node has no right child
                current = node.left                                                          #Assign key node to left child
                if display:  
                    print("Deleted phone details \n", node.item)                            
                node = None                                                                  #delete the node
                return current, success
            elif node.right is not None and node.left is not None:
                current = search_min(node.right)                                             #find the min value from right sub tree using defined function
                if display:    
                    print("Deleted phone details \n", node.item)                                               
                node.item = current.item                                                                       #replace the min value from right sub tree
                node.right,success = delete(node.right, current.item.name, current.item.price,display=False)   #delete the min value node from right sub tree
        return node, success
        
    _ , success = delete(bst.root, name, price)
    if success:
        bst.no_of_phones -= 1

    

def totalPhones (bst) :

    # This function should return a pair of integers, first being the total different types of Phones currently in the store, and the second integer being the total number of Phones currently in stock in the store i.e sum of quantity left in stock field of each Phone entry in the BST.
    def total_count_qty(node):
       

        if node is None:
            return 0, 0
        left_tree_count , left_tree_quantity = total_count_qty(node.left)
        right_tree_count , right_tree_quantity = total_count_qty(node.right)
        cnt = left_tree_count + right_tree_count + 1
        qty = left_tree_quantity + right_tree_quantity + node.item.quantity
        return cnt, qty
    
    count, quantity = total_count_qty(bst.root)
    return count, quantity
# Enum type of choices
class Input(Enum):
    RESTART = 0
    FILE_INPUT = 1
    COMMAND_INPUT = 2
    SEARCH_COST = 3
    FIND_MAX = 4
    FIND_SECOND_MAX = 5
    FIND_MIN = 6
    FIND_SECOND_MIN = 7
    DELETE_RECORD = 8
    UPDATE_STOCK = 9
    LIST_ALL_PRICE = 10
    PHONE_TYPE_AND_STOCK_PAIR = 11
    PRINT_ALL_PHONE = 12
    EXIT = 13


def get_input_from_user():
    print("\nPHONE RECORD MANAGER")
    print(" 0. Restart Freshly")
    print(" 1. File Input")
    print(" 2. Command line Input")
    print(" 3. Search Cost")
    print(" 4. Find max Price")
    print(" 5. Find second max Price")
    print(" 6. Find min Price")
    print(" 7. Find second min Price")
    print(" 8. Delete record")
    print(" 9. Update stock")
    print("10. List all the prices")
    print("11. Display number of phone type and stock pair")
    print("12. Print All the phones details")
    print("13. Exit")
    option = int(input("Enter your choice: "))
    return option


def command_prompt():
    # Get the choice from user

    # Initially, empty BST instance is created
    bst = createEmptyBST()

    while (True):
        # Handling invalid inputs
        success = True
        try:
            option = get_input_from_user()
        except Exception as error_message:
            print("ERROR: ", error_message)
            print("Please enter an integer value")
            success = False

        if success == False:
            continue

        if option == Input.RESTART.value:
            del(bst)
            bst = createEmptyBST()
            print("Operation successful")
        elif option == Input.FILE_INPUT.value:
            filename = input("Enter the name of the file: ")
            f = open(filename, "r")
            no_of_entries = int(f.readline().rstrip('\n'))
            unique = True
            for _ in range(no_of_entries):
                item = f.readline().rstrip('\n').split(", ")
                phone = Phone(item[0], int(item[1]), int(item[2]))
                bst, success = insertIntoBST(bst, phone)
                unique = unique and success
            f.close()
            if not unique:
                print("Duplicate records found, which are ignored.")
            print("Insertion operation complete.")
        elif option == Input.COMMAND_INPUT.value:
            no_of_entries = int(input("Enter the number of entries: "))
            print("Enter the details is below format:\n<PHONE_NAME>, <PRICE>, <QUANTITY>")
            for _ in range(no_of_entries):
                item = input("Enter the phone details: ").split(', ')
                phone = Phone(item[0], int(item[1]), int(item[2]))
                bst, success = insertIntoBST(bst, phone)
                if not success:
                    print("Duplicate records found, which are ignored.")
            print("Insertion operation complete.")
        elif option == Input.SEARCH_COST.value:
            cost = int(input("Enter the phone price to search: "))
            phone = findInBST(bst, cost)
            if not phone:
                print("Record not found")
            else:
                print(phone)
        elif option == Input.FIND_MAX.value:
            phone = findMaxPrice(bst)
            if phone:
                print(phone)
        elif option == Input.FIND_SECOND_MAX.value:
            phone = findSecondMaxPrice(bst)
            if phone:
                print(phone)
        elif option == Input.FIND_MIN.value:
            phone = findMinPrice(bst)
            if phone:
                print(phone)
        elif option == Input.FIND_SECOND_MIN.value:
            phone = findSecondMinPrice(bst)
            if phone:
                print(phone)
        elif option == Input.DELETE_RECORD.value:
            name = input("Enter the name of the phone to be deleted: ")
            cost = int(input("Enter the cost of the phone to be deleted: "))
            deleteFromBST(bst, name, cost)
        elif option == Input.UPDATE_STOCK.value:
            print("Update stock by entering the following information")
            name = input("Enter the name of the phone : ")
            price = int(input("Enter the cost : "))
            new_qty = int(input("Enter the new quantity : "))
            modifyQtyInStock(bst, name, price, new_qty)
        elif option == Input.LIST_ALL_PRICE.value:
            listAllPrices(bst)
        elif option == Input.PHONE_TYPE_AND_STOCK_PAIR.value:
            count, quantity = totalPhones (bst)
            print("Phone count and quantity is \n",count, quantity)
        elif option == Input.PRINT_ALL_PHONE.value:
            print("Printing all phones details of the BST")
            printAllPhoneDetails(bst)
        elif option == Input.EXIT.value:
            return
        else:
            print("Please enter the valid option")


if __name__ == "__main__":
    try:
        command_prompt()
    except Exception as error_message:
        print("\nFound error: ", error_message)
        print("Your previous contents are flushed...\nRestarting...")
        command_prompt()
    
    print("\nThank you...\nProgram terminated successfully...")
