#ifndef ACCOUNT_H
#define ACCOUNT_H
#include "date.h"
#include <iostream>
using namespace std;

class SavingsAccount
{
private:
    int id;  // 账号
    double balance;  // 余额
    double rate;  // 年利率
    Date lastDate;  // 上次变更余额的日期
    double accumulation;  // 余额按日利息累加之和
    // 获得到指定日期为止的存款金额按日累积值
    double accumulate(Date date);

public:
    SavingsAccount(Date date, int id, double rate);
    void deposit(Date date, double amount);// 存入现金，date为日期，amount为金额
    void withdraw(Date date, double amount);// 取出现金
    void settle(Date date);// 结算利息，每年1月1日调用一次该函数
    void show() const;// 输出账户信息
    int getId() const { return id; }// 获取账号
    double getBalance() const { return balance; }// 获取余额
    double getRate() const { return rate; }// 获取年利率
};

#endif