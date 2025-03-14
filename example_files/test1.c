#include <stdio.h>

int main() {
    int numbers[] = {3, 7, 15, 2, 9};
    int sum = 0;

    for (int i = 0; i < 5; i++) {
        process(numbers[i]);
        sum += numbers[i];
    }

    printf("Total Sum: %d\n", sum);
    return 0;
}
