import java.time.LocalDate;

public class Account {
    int id;
    double balance;
    double annuRate;
    LocalDate dataCreated;
    public Account(){}
    public Account(int id,double balance){
        this.id = id;
        this.balance = balance;
    }
    public int getId(){
        return id;
    }
    public void setId(int id){
        this.id = id;
    }
    public double getBalance(){
        return balance;
    }
    public void setbalance(double balance){
        this.balance = balance;
    }
    public double getAnnuRate(){
        return annuRate;
    }
    public void setAnnuRate(double annuRate){
        this.annuRate = annuRate;
    }
    public LocalDate getDataCreted(){
        return dataCreated;
    }
    public double getMonthlyRate(){
        return annuRate/12;
    }
    public void withdraw(double money){
        balance -= money;
    }
    public void deposit(double money){
        balance += money;
    }
}
