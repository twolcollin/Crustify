	#include <stdio.h> // NOLINT

		int main() { // NOLINT
	int numbers[] = {3, 7, 15, 2, 9}; // NOLINT
		int sum = 0; // NOLINT

		for (int i = 0; i < 5; i++) {
        process(numbers[i]);
		sum += numbers[i]; // NOLINT
		}

     printf("Total Sum: %d\n", sum); // NOLINT
			return 0; // NOLINT
       }
