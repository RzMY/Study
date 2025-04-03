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
        virtual void show() const;
        virtual void deposit(Date date, double amount) = 0;
        virtual void withdraw(Date date, double amount) = 0;
        virtual void settle(Date date) = 0;
};

class SavingsAccount : public Account {
    private:
        double rate; // 年利率
        Date lastDate;
        double accumulation;
        double accumulate(Date date);
    public:
        SavingsAccount(Date date, int id, double rate);
        virtual void deposit(Date date, double amount);
        virtual void withdraw(Date date, double amount);
        virtual void settle(Date date);
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
        void payFee(Date date);
        virtual void deposit(Date date, double amount);
        virtual void withdraw(Date date, double amount);
        virtual void settle(Date date);
};

#endif