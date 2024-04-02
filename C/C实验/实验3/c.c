#include <stdio.h>

int main() {
    int year, month, days;
    
    printf("请输入年 月:");
    scanf("%d%d", &year, &month);
    
    switch (month) {
        case 1:  
        case 3:  
        case 5:  
        case 7:
        case 8:  
        case 10:  
        case 12:  /*处理"大"月*/
            days = 31;
            break;
        case 4:  
        case 6:  
        case 9:  
        case 11:  /*处理"小"月*/
            days = 30;
            break;
        case 2:  /*处理"平"月*/
            if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0)
                days = 29;  /*如果是闰年，注意体会此判断表达式！！*/
            else 
                days = 28;  /*不是闰年*/
            break;
        default:  
            printf("Input error!  \n");  /*月份输入错误*/
            days = 0;
    }
    
    if (days != 0) 
        printf("%d年%d月有 %d 天\n", year, month, days);
}