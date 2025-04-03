#include "account.h"

SavingsAccount::SavingsAccount(Date date, int id, double rate):id(id), balance(0), rate(rate), lastDate(date), accumulation(0) 
{
    cout << date << "\t#" << id << " is created" << endl;
}


void SavingsAccount::deposit(Date date, double amount)
{
    accumulation = accumulate(date);
    balance += amount;
    lastDate = date;
    cout << date << "\t#" << id << " deposits " << amount << ", balance: " << balance << endl;
}

void SavingsAccount::withdraw(Date date, double amount)
{
    accumulation = accumulate(date);
    balance -= amount;
    lastDate = date;
    cout << date << "\t#" << id << " withdraws " << amount << ", balance: " << balance << endl;
}

double SavingsAccount::accumulate(Date date)
{
    return accumulation + balance * (date - lastDate) * (rate/365);
}

void SavingsAccount::settle(Date date)
{
    accumulation = accumulate(date);
    lastDate = date;
    balance += accumulation;
    accumulation = 0;
    cout << date << "\t#" << id << " settle, balance: " << balance << endl;
}

void SavingsAccount::show() const
{
    cout << "#" << id << "\tBalance: " << balance << endl;
}
