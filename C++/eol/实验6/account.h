#ifndef ACCOUNT_H
#define ACCOUNT_H
#include "date.h"

class Account {
    public:
        int id;
        double balance;
        Account(int id, double balance);
        int getId() const;
        double getBalance() const;
        void show() const;
};

class SavingsAccount : public Account {
    private:
        double rate; // 年利率
        Date lastDate;
        double accumulation;
        double accumulate(Date date);
    public:
        SavingsAccount(Date date, int id, double rate);
        void deposit(Date date, double amount);
        void withdraw(Date date, double amount);
        void settle(Date date);
        double getRate() const;
};

class CreditAccount : public Account {
    private:
        double credit;
        double rate; // 日利率
        double fee; // 年费，假设每年1月1日收取
        double accumulation;
        Date createDate;
        Date lastDate;
        double accumulate(Date date);
        double getDebt() const;  
    public:
        CreditAccount(Date date, int id, double credit, double rate, double fee);
        double getAvailableCredit() const;
        void withdraw(Date date, double amount);
        void payFee(Date date);
        void payOff(Date date);
};

#endif