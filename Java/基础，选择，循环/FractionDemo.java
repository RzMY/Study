import java.util.Scanner;
public class FractionDemo {
    public static void main(String[] args){
        System.out.println("请输入一个浮点数:");
        Scanner sc = new Scanner(System.in);
        double d = sc.nextDouble();
        System.out.println("整数部分:"+(int)d);
        System.out.println("小数部分:"+(d - (int)d));
        sc.close();
    }
}
