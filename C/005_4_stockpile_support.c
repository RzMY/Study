#include <stdio.h>

extern int count;

void write_extern(void)
{
    printf("count in %d\n",count);
}