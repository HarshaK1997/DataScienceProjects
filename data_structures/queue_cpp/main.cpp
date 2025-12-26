#include "main.h"

int get_and_validate_integer_input()
{
    string input_string;
    // Regex pattern for integer
    regex pattern("^-?\\d+$");

    cin >> input_string;
    // Loop till user gives an integer input
    while (!regex_match(input_string, pattern))
    {
        cout << "Enter only integer input: ";
        cin >> input_string;
    }

    return stoi(input_string);
}

bool get_input_from_user(int &input)
{
    cout << "\nQueue implementation using Array and Linked List:" << endl;
    cout << "===== ============== ===== ===== === ====== =====\n"
         << endl;
    cout << " 1. Enqueue elements from file(s) to Array" << endl;
    cout << " 2. Enqueue elements from file(s) to Linked List" << endl;
    cout << " 3. Enqueue elements from file(s) to Sorted List" << endl;
    cout << " 4. Enqueue element from command line to Array" << endl;
    cout << " 5. Enqueue element from command line to Linked List" << endl;
    cout << " 6. Enqueue element from command line to Sorted List" << endl;
    cout << " 7. Dequeue element from Array" << endl;
    cout << " 8. Dequeue element from Linked List" << endl;
    cout << " 9. Dequeue element from Sorted List" << endl;
    cout << "10. Search given element from Sorted List" << endl;
    cout << "11. Display Array elements" << endl;
    cout << "12. Display Linked List elements" << endl;
    cout << "13. Display Sorted List elements" << endl;
    cout << "14. Exit" << endl;
    cout << "Enter your choice: ";
    input = get_and_validate_integer_input();

    if (input < ENQUEUE_FILE_ARRAY || input > EXIT)
    {
        cout << "\n*** Invalid option entered, try again ***" << endl;
        return false;
    }

    return true;
}

void command_prompt()
{
    // Get the choice from user
    int input = -1;
    int element = -1;
    int num_of_elements = -1;
    string filename = "";
    queue_using_array q_arr;
    queue_using_unsorted_linked_list q_list;
    queue_using_sorted_linked_list q_sorted_list;
    // system_clock::time_point start;
    // steady_clock::time_point stop;
    // steady_clock::duration duration;

    while (true)
    {
        // Loop till the user enters valid input
        while (!get_input_from_user(input))
            ;
        auto start = high_resolution_clock::now();

        switch (input)
        {

        case ENQUEUE_FILE_ARRAY:
            cout << "Enter the filename to enqueue its elements: ";
            cin >> filename;
            if (q_arr.enqueue_input_file(filename))
                cout << "File contents enqueued to array queue successfully" << endl;
            else
                cout << "Operation failed" << endl;
            break;
        case ENQUEUE_FILE_LIST:
            cout << "Enter the filename to enqueue its elements: ";
            cin >> filename;
            if (q_list.enqueue_input_file(filename))
                cout << "File contents enqueued to linked list queue successfully" << endl;
            else
                cout << "Operation failed" << endl;
            break;
        case ENQUEUE_FILE_SORTED_LIST:
            cout << "Enter the filename to enqueue its elements: ";
            cin >> filename;
            if (q_sorted_list.enqueue_input_file(filename))
                cout << "File contents enqueued to sorted linked list queue successfully" << endl;
            else
                cout << "Operation failed" << endl;
            break;
        case ENQUEUE_ELEMENT_ARRAY:
            cout << "Enter the element to Enqueue: ";
            element = get_and_validate_integer_input();
            if (q_arr.enqueue_command_line(element))
                cout << "Element inserted successfully" << endl;
            else
                cout << "Operation failed" << endl;
            break;
        case ENQUEUE_ELEMENT_LIST:
            cout << "Enter the element to Enqueue: ";
            element = get_and_validate_integer_input();
            if (q_list.enqueue_command_line(element))
                cout << "Element inserted successfully" << endl;
            else
                cout << "Operation failed" << endl;
            break;
        case ENQUEUE_ELEMENT_SORTED_LIST:
            cout << "Enter the element to Enqueue: ";
            element = get_and_validate_integer_input();
            if (q_sorted_list.enqueue_command_line(element))
                cout << "Element inserted successfully" << endl;
            else
                cout << "Operation failed" << endl;
            break;
        case DEQUEUE_ELEMENT_ARRAY:
            if (q_arr.dequeue(element))
                cout << "Element " << element << " is deleted successfully" << endl;
            else
                cout << "Operation failed" << endl;
            break;
        case DEQUEUE_ELEMENT_LIST:
            if (q_list.dequeue(element))
                cout << "Element " << element << " is deleted successfully" << endl;
            else
                cout << "Operation failed" << endl;
            break;
        case DEQUEUE_ELEMENT_SORTED_LIST:
            if (q_sorted_list.dequeue(element))
                cout << "Element " << element << " is deleted successfully" << endl;
            else
                cout << "Operation failed" << endl;
            break;
        case SEARCH_ELEMENT_SORTED_LIST:
            cout << "Enter the element to search in sorted queue: ";
            element = get_and_validate_integer_input();
            if (q_sorted_list.search(element))
                cout << "Given element " << element << " is found in the list" << endl;
            else
                cout << "Element not found in the queue" << endl;
            break;
        case DISPLAY_ARRAY:
            cout << "Enter number of elements to display: ";
            num_of_elements = get_and_validate_integer_input();
            q_arr.display_queue_elements(num_of_elements);
            break;
        case DISPLAY_LIST:
            cout << "Enter number of elements to display: ";
            num_of_elements = get_and_validate_integer_input();
            q_list.display_queue_elements(num_of_elements);
            break;
        case DISPLAY_SORTED_LIST:
            cout << "Enter number of elements to display: ";
            num_of_elements = get_and_validate_integer_input();
            q_sorted_list.display_queue_elements(num_of_elements);
            break;
        case EXIT:
            cout << "Thank you!" << endl;
            return;
        default:
            cout << "Unknown error occurred" << endl;
            return;
        }
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<nanoseconds>(stop - start);
        cout << "Time taken by the operation: " << duration.count() << " nanoseconds" << endl;
    }
}

int main()
{
    // Command Prompt GUI
    command_prompt();
    return 0;
}
