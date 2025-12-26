#include "queue.h"

using namespace std;

queue_using_array::queue_using_array()
{
	front = rear = -1;
	capacity = 3;
	array_queue = new int[capacity];
}

queue_using_array::~queue_using_array()
{

	delete[] array_queue;
}

bool queue_using_array::enqueue_input_file(string filename)
{
	ifstream in(filename);

	// Check if file exists
	if (!in.good())
	{
		return false;
	}

	string text;
	int value;

	while (!in.eof())
	{
		// Get data from file
		getline(in, text);
		// If the text can be converted to integer type, then store it in unsorted linked list
		if (is_number(text, value))
		{
			queue_using_array::enqueue_command_line(value);
		}
	}
	return true;
}

bool queue_using_array::enqueue_command_line(int element)
{
	// Condition to check if circular queue is empty
	if (front == -1 && rear == -1)
	{
		front = 0;
		size = 0;
	}

	int j = -1;
	if (size != 0)
	{
		for (j = front; j != rear; j = (j + 1) % (capacity)) // Looping through the elements
		{
			if (array_queue[j] == element)
			{ // Check if element is already present
				cout << "Element already present, add unique element : " << array_queue[j] << endl;
				return false;
			}
		}
		if (array_queue[j] == element)
		{
			cout << "Element already present, add unique element : " << array_queue[j] << endl;
			return false;
		}
	}

	// Implementing circular queue
	if (front != 0 && size < capacity)
	{
		rear = (rear + 1) % capacity; // rear is incremented to add the element
		array_queue[rear] = element;
		size++;
		return true;
	}

	if (size == capacity) // Check for the overflow condition
	{
		capacity = 2 * capacity;
		int *array_queue_new = new int[capacity];
		int i;
		int new_rear = 0;
		for (i = front; i != rear; i = (i + 1) % (capacity / 2))
		{
			array_queue_new[new_rear++] = array_queue[i];
		}
		array_queue_new[new_rear] = array_queue[i];
		delete[] array_queue;		   // Delete old memory
		array_queue = array_queue_new; // Change the array name
		array_queue_new = NULL;		   // Delete the new array name
		front = 0;
		rear = new_rear;
	}

	rear = (rear + 1) % capacity; // rear is incremented to add the element
	array_queue[rear] = element;  // Add the element at the end of the queue
	size++;

	return true;
}

bool queue_using_array::dequeue(int &element)
{

	if (front == -1 && rear == -1) // Check if queue is empty
		return false;

	else if (front == rear) // Check if queue has only one element
	{
		element = array_queue[front]; // Assign the front element to be deleted to element
		front = -1;
		rear = -1;
		size--;
		return true;
	}

	else
	{
		element = array_queue[front]; // Assign the front element to be deleted to element
		front = (front + 1);		  // Increment the front by 1 for circular queue
		size--;
		return true;
	}
}
void queue_using_array::display_queue_elements(int num_of_elements)
{
	int current = front; // assigning front value to current variable
	int temp = 0;

	if (front == -1 && rear == -1)
		cout << "Queue is empty"; // Check if queue is empty

	else
	{
		cout << "Elements in the Queue are " << endl; // Display the elements
		int i = -1;
		for (i = front; i != rear; i = (i + 1) % capacity)
		{
			if (temp == num_of_elements)
			{
				return;
			}
			temp++;
			cout << array_queue[i] << endl;
		}
		if (temp == num_of_elements)
			cout << array_queue[i] << endl;
	}
	cout << endl;
	return;
}

queue_using_unsorted_linked_list::queue_using_unsorted_linked_list()
{
	front = rear = NULL;
}

queue_using_unsorted_linked_list::~queue_using_unsorted_linked_list()
{
	linked_list_queue::destroy_nodes(&front, &rear);
}

bool queue_using_unsorted_linked_list::enqueue_input_file(string filename)
{
	ifstream in(filename);

	// Check if file exists
	if (!in.good())
	{
		return false;
	}

	string text;
	int value;

	while (!in.eof())
	{
		// Get data from file
		getline(in, text);
		// If the text can be converted to integer type, then store it in unsorted linked list
		if (is_number(text, value))
		{
			queue_using_unsorted_linked_list::enqueue_command_line(value);
		}
	}
	return true;
}

bool queue_using_unsorted_linked_list::enqueue_command_line(int element)
{
	// Create a new node
	if (linked_list_queue::search(front, element))
	{
		// duplicate
		cout << "Duplicate element " << element << " exists" << endl;
		return false;
	}
	node *new_node = new node(element);

	// If queue is empty, then front and rear = new node
	if (rear == NULL)
	{
		front = rear = new_node;
		return true;
	}

	// Add the new node at the end of queue and change rear
	rear->next = new_node;
	rear = new_node;
	return true;
}

bool queue_using_unsorted_linked_list::dequeue(int &element)
{
	return linked_list_queue::dequeue(&front, &rear, element);
}

void queue_using_unsorted_linked_list::display_queue_elements(int num_of_elements)
{
	linked_list_queue::print_linked_list_elements(front, num_of_elements);
	return;
}

queue_using_sorted_linked_list::queue_using_sorted_linked_list()
{
	front = rear = NULL;
}

queue_using_sorted_linked_list::~queue_using_sorted_linked_list()
{
	linked_list_queue::destroy_nodes(&front, &rear);
}

bool queue_using_sorted_linked_list::enqueue_input_file(string filename)
{
	ifstream in(filename);

	// Check if file exists
	if (!in.good())
	{
		return false;
	}

	string text;
	int value;

	while (!in.eof())
	{
		// Get data from file
		getline(in, text);
		// If the text can be converted to integer type, then store it in unsorted linked list
		if (is_number(text, value))
		{
			queue_using_sorted_linked_list::enqueue_command_line(value);
		}
	}
	return true;
}

bool queue_using_sorted_linked_list::enqueue_command_line(int element)
{
	// Create a new node
	node *new_node = new node(element);

	// If linked list is empty or first element in queue is greater than given element, put new_node at front
	if (front == NULL || front->element > new_node->element)
	{
		new_node->next = front;
		front = new_node;
		return true;
	}
	if (front->element == new_node->element)
	{
		// Duplicate
		cout << "Duplicate element " << element << " exists" << endl;
		return false;
	}

	node *current = front;
	// Traverse the current node till its next nodes element is greater than given element.
	// So that we can place the new_node after current node.
	while (current->next != NULL && current->next->element < new_node->element)
		current = current->next;

	if (current->element == new_node->element)
	{
		// Duplicate
		cout << "Duplicate element " << element << " exists" << endl;
		return false;
	}

	// Placing new_node after current node.
	new_node->next = current->next;
	current->next = new_node;

	return true;
}

bool queue_using_sorted_linked_list::search(int element)
{
	node *current = front;
	while (current)
	{
		// If current node element is greater than the given element in sorted queue, then given element is not present.
		if (current->element > element)
		{
			return false;
		}
		if (current->element == element)
		{
			return true;
		}
		current = current->next;
	}
	return false;
}

bool queue_using_sorted_linked_list::dequeue(int &element)
{
	return linked_list_queue::dequeue(&front, &rear, element);
}

void queue_using_sorted_linked_list::display_queue_elements(int num_of_elements)
{
	linked_list_queue::print_linked_list_elements(front, num_of_elements);
	return;
}

void linked_list_queue::print_linked_list_elements(node *front, int num_of_elements)
{
	int n = num_of_elements;
	node *temp = front;

	// Traverse the node n times and print the elements
	while (n-- && (temp != NULL))
	{
		cout << temp->element << " ";
		temp = temp->next;
	}

	// Still elements are present
	if (temp != NULL)
	{
		cout << "...";
	}

	cout << endl;
	return;
}

bool linked_list_queue::search(node *front, int element)
{
	node *current = front;

	while (current)
	{
		if (current->element == element)
		{
			// duplicate element is present
			return true;
		}
		current = current->next;
	}
	return false;
}

bool linked_list_queue::dequeue(node **front, node **rear, int &element)
{
	// Underflow check
	if ((*front) == NULL)
		return false;

	// Store the front and move front one node ahead
	node *del_node = (*front);
	(*front) = (*front)->next;

	// Get the popped element to return and delete the node
	element = del_node->element;
	delete (del_node);

	// If front is NULL, then the queue is empty. Hence update the rear also as NULL
	if ((*front) == NULL)
		(*rear) = NULL;

	return true;
}

void linked_list_queue::destroy_nodes(node **front, node **rear)
{
	node *current = (*front);
	node *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		delete (current);
		current = next;
	}

	(*front) = (*rear) = NULL;
}

bool is_number(string text, int &value)
{
	size_t pos;
	try
	{
		value = stoi(text, &pos);
		// Check if the entire string is converted to an integer
		if (pos == text.length())
		{
			// Text is an integer
			return true;
		}
	}
	catch (...)
	{
		// The text is not integer
	}
	return false;
}
