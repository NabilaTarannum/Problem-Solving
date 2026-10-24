#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	char ch, s[20], sen[100];
	scanf("%c %s %[^\n]", &ch, s, sen);
	printf("%c\n%s\n%s\n", ch, s, sen);

	return 0;
}
