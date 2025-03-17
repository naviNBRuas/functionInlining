#include <stdio.h>
#include <stdbool.h>

// Function prototypes
bool is_even(int number);
void check_and_print(int number);

int main() {
    int number = 4; // Example number
    check_and_print(number);
    return 0;
}

// Function definitions
bool is_even(int number) {
    return number % 2 == 0;
}

void check_and_print(int number) {
    if (is_even(number)) {
        printf("%d is even\n", number);
    } else {
        printf("%d is odd\n", number);
    }
}
