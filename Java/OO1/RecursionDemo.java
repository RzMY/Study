import java.util.Scanner;

public class RecursionDemo {
    public static long factor(int n){
        if(n == 0){
            return 1;
        }else{
            return n * factor(n - 1);
        }
    }
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("请输入n: \n");
        int n = input.nextInt();
        System.out.println(n + "! = " + factor(n));
        System.out.println("Max of long = " + Long.MAX_VALUE);
        input.close();
    }
}
