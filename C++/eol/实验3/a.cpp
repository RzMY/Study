#include <iostream>
using namespace std;

class SavingsAccount
{
    int  id;  //帐号
    double  balance;  //余额
    double  rate;   //年利率
    int  lastDate; //上次变更余额的日期
    double  accumulation; //余额按日利息累加之和
    double  accumulate(int date);//获得到指定日期为止的存款金额按日累积值
    public:
        SavingsAccount (int date, int id, double rate);  //构造函数
        void  deposit(int date, double amount);  //存入现金，date为日期，amount为金额
        void  withdraw(int date, double amount);  //取出现金
        void  settle(int date); //结算利息，每年1月1日调用一次该函数 
        void  show();   //输出账户信息
        int getId() {return id;} //获取用户ID
        double  getBalance () { return balance;}//获取余额
        double  getRate() {return rate;} //获取利率
};

SavingsAccount::SavingsAccount(int date, int id, double rate):id(id), balance(0), rate(rate), lastDate(date), accumulation(0) 
{
    cout << date << "\t#" << id << " is created" << endl;
}

// 存款
void SavingsAccount::deposit(int date, double amount)
{
    accumulation = accumulate(date);
    balance += amount;
    lastDate = date;
    cout << date << "\t#" << id << " deposits " << amount << ", balance: " << balance << endl;
}

// 取款
void SavingsAccount::withdraw(int date, double amount)
{
    accumulation = accumulate(date);
    balance -= amount;
    lastDate = date;
    cout << date << "\t#" << id << " withdraws " << amount << ", balance: " << balance << endl;
}
// 计算到指定日期为止的存款金额按日累积值
double SavingsAccount::accumulate(int date)
{
    return accumulation + balance * (date - lastDate) * (rate/365);
}

// 结算利息
void SavingsAccount::settle(int date)
{
    accumulation = accumulate(date);
    lastDate = date;
    balance += accumulation;
    accumulation = 0;
    cout << date << "\t#" << id << " settle, balance: " << balance << endl;
}

// 输出账户信息
void SavingsAccount::show()
{
    cout << "#" << id << "\tBalance: " << balance << endl;
}

int main()
{
    SavingsAccount s0(1, 111111, 0.015);
    SavingsAccount s1(1, 222222, 0.015);// 定义两个账户s0和s1，年利率都是1.5%，都在1日创建账户
    s0.deposit(5, 5000);// s0在5日存入5000元
    s0.deposit(45, 5500);// s0在45日存入5500元
    s1.deposit(25, 10000);// s1在25日存入10000元
    s1.withdraw(60, 4000);// s1在60日取出4000元
    s0.settle(90);// 90日结算利息
    s1.settle(90);// 90日结算利息
    s0.show();// 输出s0账户信息
    s1.show();// 输出s1账户信息
    return 0;
}