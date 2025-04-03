#include "account.h"

int main() {
    SavingsAccount s0(Date(2020, 11, 1), 111111, 0.015);
    SavingsAccount s1(Date(2020, 11, 1), 222222, 0.015);
    CreditAccount c0(Date(2020, 11, 1), 333333, 10000, 0.0005, 50);
    Account *accounts[] = {&s0, &s1, &c0};
    accounts[0]->deposit(Date(2020, 11, 5), 5000);
    accounts[0]->deposit(Date(2020, 12, 5), 5500);
    accounts[1]->deposit(Date(2020, 11, 25), 10000);
    accounts[1]->withdraw(Date(2020, 12, 20), 4000);
    accounts[2]->withdraw(Date(2020, 11, 15), 2000);
    accounts[2]->settle(Date(2020, 11, 30)); // 提前尝试结算还款
    accounts[2]->settle(Date(2020, 12, 1));
    c0.payFee(Date(2021, 1, 1));
    accounts[0]->settle(Date(2020, 12, 30)); // 提前尝试结算利息
    accounts[0]->settle(Date(2021, 1, 1));
    accounts[1]->settle(Date(2021, 1, 1));
    for (int i = 0; i < 3; i++) {
        accounts[i]->show();
    }
    return 0;
}