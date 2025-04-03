#include "date.h"
#include "account.h"

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