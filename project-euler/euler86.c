#include <stdio.h>
#include <stdlib.h>
#include <math.h>


#define BOUND 2000

/*
int *generate_primitive_triple()
{
	return triple;
}


int count_cuboid(int *primitive_triple, int bound)
{
	return count;
}
*/

int main(int argc, char *argv[])
{
	int count = 0;
	int i;
	for (i = 1; count <= BOUND; i++) {
		int j;
		for (j = 1; j <= 2*i; j++) {
			if (fmod(hypot(i, j), 1.0) == 0) {
				if (j - 1 > i) {
					count += j/2 - j + i + 1;
				} else {
					count += j/2;
				}
			}
		}
		//printf("The other_count is %d\n", other_count);
	}

	printf("The count is %d\n", count);
	printf("The M is %d\n", i);

	return 0;
}
