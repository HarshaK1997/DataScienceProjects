#include <iostream>
#include <fstream>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Validate if the given string can be converted to integer or not.
bool is_number(string text, int &value);

struct node
{
    // Data to be stored
    int element;

    // Pointer to store next link
    node *next;

    // Parameterised Constructor
    node(int element)
    {
        this->element = element;
        this->next = NULL;
    }
};

// Circular Queue implementation using Array
class queue_using_array
{
private:
    // Front pointer
    int front;

    // Rear pointer
    int rear;

    // Number of elements in array_queue
    int size;

    // Maximum elements an array_queue can store
    int capacity;

    // Array to store elements
    int *array_queue;

public:
    // Contructor
    queue_using_array();

    // Destructor
    ~queue_using_array();

    // Enqueues elements into the array Queue from the specified file and returns true if success.
    bool enqueue_input_file(string filename);

    // Enqueues element into the array Queue from the command line and returns true if success.
    bool enqueue_command_line(int element);

    // Dequeues the element from the Array Queue and returns true if success.
    bool dequeue(int &element);

    // Print given number of elements from the Queue and returns true if success.
    void display_queue_elements(int num_of_elements);
};

class linked_list_queue
{
public:
    // Traverses the Queue and returns true if given element is found.
    // O(N)
    bool search(node *front, int element);

    // Delete given element from the Queue and returns true if success.
    // O(1)
    bool dequeue(node **front, node **rear, int &element);

    // Print given number of elements from the Queue.
    // O(N), where N is num_of_elements to display
    void print_linked_list_elements(node *front, int num_of_elements);

    // Destroy all nodes from front to rear in the queue.
    // theta(N)
    void destroy_nodes(node **front, node **rear);
};

// Queue implementation using Singly Linked list (Unsorted)
class queue_using_unsorted_linked_list : private linked_list_queue
{
private:
    // Front/Head pointer
    node *front;

    // Rear/Tail pointer
    node *rear;

public:
    // Constructor
    // theta(1)
    queue_using_unsorted_linked_list();

    // Destructor
    // theta(N)
    ~queue_using_unsorted_linked_list();

    // Insert elements into the Queue from given file and returns true if success.
    // Search + Insert = O(N) + O(M) = O(MN), where N is number of elements in the queue and M is number of elements in the file.
    // Detailed:
    // If N is number of elements in teh queue and M is number of elements in the file.
    // For 1st element insert: N searches + 1 insert = N + 1
    // For 2nd element insert: N+1 searches + 1 insert = (N+1) + 1
    // For 3rd element insert: N+2 searches + 1 insert = (N+2) + 1
    // For Mth element insert: N+(M-1) searches + 1 insert = (N+M-1) + 1
    // Total time = N+1 + N+2 + N+3 + ... + N+M
    // = MN + (1+2+3+...+M)
    // = MN + M(M+1)/2
    // = O(MN) + O(M^2 + M)
    bool enqueue_input_file(string filename);

    // Insert given element into the Queue from command line and returns true if success.
    // Search + Insert = O(N) + O(1) = O(N)
    bool enqueue_command_line(int element);

    // Delete given element from the Queue and returns true if success.
    // O(1)
    bool dequeue(int &element);

    // Print given number of elements from the Queue.
    // O(N), where N is num_of_elements to display
    void display_queue_elements(int num_of_elements);
};

// Queue implementation using Singly Linked list (Sorted: Ascending order)
class queue_using_sorted_linked_list : private linked_list_queue
{
private:
    // Front/Head pointer
    node *front;

    // Rear/Tail pointer
    node *rear;

public:
    // Constructor
    // theta(1)
    queue_using_sorted_linked_list();

    // Destructor
    // theta(N)
    ~queue_using_sorted_linked_list();

    // Insert elements into the Queue from given file and returns true if success.
    // Search + Insert = O(N) + O(M) = O(MN), where N is number of elements in the queue and M is number of elements in the file.
    // Detailed:
    // If N is number of elements in teh queue and M is number of elements in the file.
    // For 1st element insert: N searches + 1 insert = N + 1
    // For 2nd element insert: N+1 searches + 1 insert = (N+1) + 1
    // For 3rd element insert: N+2 searches + 1 insert = (N+2) + 1
    // For Mth element insert: N+(M-1) searches + 1 insert = (N+M-1) + 1
    // Total time = N+1 + N+2 + N+3 + ... + N+M
    // = MN + (1+2+3+...+M)
    // = MN + M(M+1)/2
    // = O(MN) + O(M^2 + M)
    bool enqueue_input_file(string filename);

    // Insert given element into the Queue from command line and returns true if success.
    // O(N)
    bool enqueue_command_line(int element);

    // Traverses the Queue and returns true if given element is found.
    // O(N)
    bool search(int element);

    // Delete given element from the Queue and returns true if success.
    // O(1)
    bool dequeue(int &element);

    // Print given number of elements from the Queue.
    // O(N), where N is num_of_elements to display
    void display_queue_elements(int num_of_elements);
};
