#include <stdio.h>
#include <math.h>

int main( )
{
    double a,b,c,d;
    printf("Enter a,b,c:");
    scanf("%lf%lf%lf",&a,&b,&c);
    d=b*b-4*a*c; //断点 1 求b2-4ac
    if (a==0)
    {
        if (b==0)
        {
            if (c==0)
                printf("参数都为零，方程无意义！\n");
            else
                printf("a 和 b 为 0，c 不为 0，方程不成立！\n");
        }
        else
            printf("x=%0.2f\n",-c/b);
    }
    else
        if (d>=0) //断点 2
        {
            printf("x1=%0.2f\n",(-b+sqrt(d))/(2*a));//sqrt为求平方根函数
            printf("x2=%0.2f\n",(-b-sqrt(d))/(2*a));
        }
        else //断点 3
        {
            printf("x1=%0.2f+%0.2fi\n",-b/(2*a),sqrt(d)/(2*a));
            printf("x2=%0.2f-%0.2fi\n",-b/(2*a),sqrt(d)/(2*a));
        }
}