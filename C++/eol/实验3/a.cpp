#include <iostream>
using namespace std;

/*
    为了简便，类中所有日期均用一个整数来表示，该整数是一个以日为单位的相对日期。例如如果以开户日为1，那么开户日后的第3天就用4来表示，这样通过将两个日期相减就可得到两个日期相差的天数。
    定义两个账户s0和s1，年利率都是1.5%，随后分别在第5天和第45天向账户s0存入5千元和5500元，在第25天向账户s1存入1万元，在第60天从账户s1取出4千元。账户开户后第90天是银行的计息日。分别输出s0和s1两个账户的信息(账号、余额)。
*/

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
        int getId() {return id;}
        double  getBalance () { return balance;}
        double  getRate() {return rate;} 
};

SavingsAccount::SavingsAccount(int date, int id, double rate):id(id), balance(0), rate(rate), lastDate(date), accumulation(0) 
{
    cout << date << "\t#" << id << " is created" << endl;
}


void SavingsAccount::deposit(int date, double amount)
{
    accumulation = accumulate(date);
    balance += amount;
    lastDate = date;
    cout << date << "\t#" << id << " deposits " << amount << ", balance: " << balance << endl;
}

void SavingsAccount::withdraw(int date, double amount)
{
    accumulation = accumulate(date);
    balance -= amount;
    lastDate = date;
    cout << date << "\t#" << id << " withdraws " << amount << ", balance: " << balance << endl;
}

double SavingsAccount::accumulate(int date)
{
    return accumulation + balance * (date - lastDate) * (rate/365);
}

void SavingsAccount::settle(int date)
{
    accumulation = accumulate(date);
    lastDate = date;
    balance += accumulation;
    accumulation = 0;
    cout << date << "\t#" << id << " settle, balance: " << balance << endl;
}

void SavingsAccount::show()
{
    cout << "#" << id << "\tBalance: " << balance << endl;
}

//定义两个账户s0和s1，年利率都是1.5%，随后分别在第5天和第45天向账户s0存入5千元和5500元，在第25天向账户s1存入1万元，在第60天从账户s1取出4千元。账户开户后第90天是银行的计息日。分别输出s0和s1两个账户的信息(账号、余额)。

int main()
{
    SavingsAccount s0(1, 111111, 0.015);
    SavingsAccount s1(1, 222222, 0.015);
    s0.deposit(5, 5000);
    s0.deposit(45, 5500);
    s1.deposit(25, 10000);
    s1.withdraw(60, 4000);
    s0.settle(90);
    s1.settle(90);
    s0.show();
    s1.show();
    return 0;
}