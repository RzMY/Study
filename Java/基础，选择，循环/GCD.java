import java.util.Scanner;
public class GCD {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("请依次输入两个数");
        int a = input.nextInt();
        int b = input.nextInt();
        int m = a;
        int n = b;
        if(a < b){
            int helper;
            helper = a;
            a = b;
            b = helper;
        }
        do{
            int helper = b;
            b = a % b;
            a = helper;
        }while(a % b != 0);
        System.out.println("The GCD of" + m + "and" + n + "is" + b);
        input.close();
    }
}
