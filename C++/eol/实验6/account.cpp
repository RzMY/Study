#include "account.h"

Account::Account(int id, double balance) {
    this->id = id;
    this->balance = balance;
}

int Account::getId() const {
    return id;
}

double Account::getBalance() const {
    return balance;
}

void Account::show() const {
    cout << "#" << id << "\tBalance: " << balance << endl;
}

double SavingsAccount::accumulate(Date date) {
    return accumulation + balance * (date - lastDate) * (rate/365);
}

SavingsAccount::SavingsAccount(Date date, int id, double rate) : Account(id, 0), rate(rate), lastDate(date), accumulation(0) {
    cout << date << "\t#" << id << " is created" << endl;
}

void SavingsAccount::deposit(Date date, double amount) {
    accumulation = accumulate(date);
    balance += amount;
    lastDate = date;
    cout << date << "\t#" << id << " deposits " << amount << ", balance: " << balance << endl;
}

void SavingsAccount::withdraw(Date date, double amount) {
    accumulation = accumulate(date);
    balance -= amount;
    lastDate = date;
    cout << date << "\t#" << id << " withdraws " << amount << ", balance: " << balance << endl;
}

void SavingsAccount::settle(Date date) {
    accumulation = accumulate(date);
    lastDate = date;
    balance += accumulation;
    accumulation = 0;
    cout << date << "\t#" << id << " settle, balance: " << balance << endl;
}

double SavingsAccount::getRate() const {
    return rate;
}

double CreditAccount::accumulate(Date date) {
    return accumulation + (credit - balance) * (date - lastDate) * rate;
}
    
double CreditAccount::getDebt() const {
    return credit - balance + accumulation;
}

CreditAccount::CreditAccount(Date date, int id, double credit, double rate, double fee) : Account(id, credit), credit(credit), rate(rate), fee(fee), accumulation(0), createDate(date), lastDate(date) {
    cout << date << "\t#" << id << " is created" << endl;
}

double CreditAccount::getAvailableCredit() const {
    return balance;
}

void CreditAccount::withdraw(Date date, double amount) {
    if(balance < amount){
        cout << "Payment Failed: insufficient balance" << endl;
    }else{
        accumulation = accumulate(date);
        balance -= amount;
        lastDate = date;
        cout << date << "\t#" << id << " withdraws " << amount << ", balance: " << balance << endl;
    }
}

void CreditAccount::payFee(Date date) {
    balance -= fee;
    cout << date << "\t#" << id << " pay fee, balance: " << balance << endl;
}

void CreditAccount::payOff(Date date) {
    accumulation = accumulate(date);
    cout << date << "\t#" << id << " pay off, debt: " << getDebt() << endl;
    balance = credit;
    lastDate = date;
}