#include <stdio.h>

void main( )
{
    int x,y,sub ;
    scanf("%d%d",&x,&y); // 改为&x,&y
    sub=x*x-y*y ;// 改为=
    printf("%c,%c,%d\n",x,y,sub);
}
