#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

	int n;
	scanf("%d", &n);
	// Complete the code to calculate the sum of the five digits on n.
	printf("%d", (n == 0) ? 0 : ({ int temp = n; int res = 0; while (temp > 0) res += temp % 10, temp /= 10; res; }));

	return 0;
}
