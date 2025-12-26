#include "queue.cpp"
#include <limits>
#include <regex>

void command_prompt();
// Get the valid choice from the user
bool get_input_from_user(int &input);
// Loop till the user gives a valid integer
int get_and_validate_integer_input();

// Enum type of choices
enum input_type
{
    ENQUEUE_FILE_ARRAY = 1,
    ENQUEUE_FILE_LIST,
    ENQUEUE_FILE_SORTED_LIST,
    ENQUEUE_ELEMENT_ARRAY,
    ENQUEUE_ELEMENT_LIST,
    ENQUEUE_ELEMENT_SORTED_LIST,
    DEQUEUE_ELEMENT_ARRAY,
    DEQUEUE_ELEMENT_LIST,
    DEQUEUE_ELEMENT_SORTED_LIST,
    SEARCH_ELEMENT_SORTED_LIST,
    DISPLAY_ARRAY,
    DISPLAY_LIST,
    DISPLAY_SORTED_LIST,
    EXIT,
};
