#include<stdio.h>
void main()
{ 
    int i = 1, password1 = 4567, password2;
    do
    {
        printf("\n请输入密码：");
        scanf("%d", &password2);
        if(password2 == password1)
        { 
            printf("\n口令正确~_~  ");
            break;                  //当口令正确就结束循环，
        }
        else 
        {
            if(i == 3)
            {
                printf("\n口令错误！您已经3次输入错误，系统将自动退出！");
                break;              //当输入错误3次就结束循环，
            }
            else
            {
                printf("\n口令错误！还有%d次机会！", 3-i);
                i++;                //输入错误次数加1，
            }
        }
    }while(i<=3); 
}
