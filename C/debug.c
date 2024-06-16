#include <string.h>
#include <stdio.h>

int main(){
	char b[30];
	strcpy(&b[0], "CH");
	strcpy(&b[2], "DEF");
	strcpy(&b[5], "ABC");
	printf("%s\n", b);
	return 0;
}