#include "date.h"
#include "account.h"

/*
定义两个账户s0和s1，年利率都是1.5%，都在2020年11月1日创建账户，
随后s0在2020年11月5日和2020年12月5日分别存入5000元和5500元，
s1在2020年11月25日和2020年12月20日分别存入10000元和取出4000元。
2021年1月1日是银行的计息日。
分别输出s0和s1两个账户的信息(账号、余额)及所有账户的总额。*/

int main()
{
    SavingsAccount s0(Date(2020,11,1), 111111, 0.015);
    SavingsAccount s1(Date(2020,11,1), 222222, 0.015);
    s0.deposit(Date(2020,11,5), 5000);
    s0.deposit(Date(2020,12,5), 5500);
    s1.deposit(Date(2020,11,25), 10000);
    s1.withdraw(Date(2020,12,20), 4000);
    s0.settle(Date(2021,1,1));
    s1.settle(Date(2021,1,1));
    s0.show();
    s1.show();
    return 0;
}