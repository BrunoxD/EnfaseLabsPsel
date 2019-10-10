#include <stdio.h>
#include <stdlib.h>

/*
Case 1:
	a = 0, b = 2, dist = abs(a - b) = 2;
	dist/2 = 1;
	a and b moves one time.

Case 2:
	a = 0, b = 3, dist = abs(a - b) = 3;	
	dist%2 = 1;
	a moves two times and b moves one time.
*/

int main(int argc, char const *argv[]) {
	int a, b, dist, total_cost;

	/* Read user inputs. */
	scanf("%d", &a);
	scanf("%d", &b);

	/* Calculate the distance between the friends. */
	dist = abs(a - b);

	/* Calculate the individual cost. */
	int i, cost = 0;
	for (i = 0; i < (dist / 2 + dist % 2); i++) 
		cost += i + 1;		

	/* Reduce cost once if distance is odd. */
	total_cost = dist % 2 ? cost * 2 - i : cost * 2;

	printf("%d\n", total_cost);

	return 0;
}