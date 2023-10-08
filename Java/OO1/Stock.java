import java.text.DecimalFormat;
import java.util.Scanner;
public class Stock {
    String symbol;
    String name;
    double previousPrice;
    double currentPrice;
    public Stock(String symbol, String name){
        this.symbol = symbol;
        this.name = name;
    }
    public void setPreviousPrice(double price){
        previousPrice = price;
    }
    public void setCurrentPrice(double price){
        currentPrice = price;
    }
    public void getChangePercent(){
        double percent = (currentPrice - previousPrice) / previousPrice;
        double after_percent = percent * 100;
        DecimalFormat convert = new DecimalFormat("#.##");
        String after_after_percent = convert.format(after_percent);
        System.out.println("股票 " + symbol + name + " 市值变化了 " + after_after_percent + "%");
    }

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("请输入股票的代码，名称，前一日收盘价，现价:");
        String symble = input.next();
        String name = input.next();
        double previousPrice = input.nextDouble();
        double currentPrice  = input.nextDouble();
        Stock stork = new Stock(symble, name);
        stork.setCurrentPrice(currentPrice);
        stork.setPreviousPrice(previousPrice);
        stork.getChangePercent();
        input.close();
    }
}
