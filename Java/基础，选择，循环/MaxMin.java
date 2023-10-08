import java.util.Scanner;
public class MaxMin {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("请依次输入4个整数:");
        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();
        int d = input.nextInt();
        int max = 0, min = 0;
        if(a <= b){
            min = a;
            max = b;
        }else{
            min = b;
            max = a;
        }
        if(c >= max){
            max = c;
        }else if(c <= min){
            min = c;
        }
        if(d >= max){
            max = d;
        }else if(d <= min){
            min = d;
        }
        System.out.println("max=" + max + " min=" + min);
        input.close();
    }
}
