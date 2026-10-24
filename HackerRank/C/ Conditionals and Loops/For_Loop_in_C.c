#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int a, b;
	scanf("%d\n%d", &a, &b);
	// Complete the code.
	for (int i = a; i <= b; i++)
		printf("%s\n", (i >= 1 && i <= 9) ? (char *[]){"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}[i - 1] : (i % 2 ? "odd" : "even"));

	return 0;
}
