#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int
main(int argc, char **argv)
{
	int i;
	srand(time(NULL));
	for (i=0; i < 10; i++)
		printf("%d\n", rand()%100);
	return 0;
}
