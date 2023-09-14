import java.util.Scanner;
public class QuadraticFormula {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("请依次输入a,b,c");
        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();
        double x = (-b + Math.sqrt(Math.pow(b,2) - 4 * a * c)) / (2 * a);
        System.out.println("x="+x);
        input.close();
    }
}
