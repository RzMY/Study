#include <stdio.h>

int main()
{
    char c1='a',c2='b',c3='c',c4='\101',c5='\116';
    printf("123456789\n");
    printf("a%c b%c\tabc\n",c1,c2,c3);/*除了格式符和转义字符其他字符原样输出 */
    printf("\t\b%c %c",c4,c5);
}