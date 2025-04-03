#include "account.h"

int main() {
    SavingsAccount s0(Date(2020, 11, 1), 111111, 0.015);
    SavingsAccount s1(Date(2020, 11, 1), 222222, 0.015);
    CreditAccount c0(Date(2020, 11, 1), 333333, 10000, 0.0005, 50);
    s0.deposit(Date(2020, 11, 5), 5000);
    s0.deposit(Date(2020, 12, 5), 5500);
    s1.deposit(Date(2020, 11, 25), 10000);
    s1.withdraw(Date(2020, 12, 20), 4000);
    c0.withdraw(Date(2020, 11, 15), 2000);
    c0.payOff(Date(2020, 12, 1));
    c0.payFee(Date(2021, 1, 1));
    s0.settle(Date(2021, 1, 1));
    s1.settle(Date(2021, 1, 1));
    s0.show();
    s1.show();
    c0.show();
    return 0;
}