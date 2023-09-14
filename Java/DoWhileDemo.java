import java.util.Scanner;
public class DoWhileDemo {
    public static void main(String[] args){
        double sum = 0;
        int n = 0;
        double number;
        Scanner input = new Scanner(System.in);
        do{
            System.out.println("请输入一个数(输入0结束):");
            number = input.nextDouble();
            if(number != 0){
                sum += number;
                n++;
            }
        }while(number != 0);
        System.out.println("sum="+sum);
        System.out.println("avg="+sum/n);
        input.close();
    }
}
