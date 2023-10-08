import java.util.Scanner;
public class Fibonacci {
    public Fibonacci(){}
    public long calculateFibonacci(int n){
        if(n == 1){
            return 1;
        }else if(n == 2){
            return 1;
        }else{
            return(calculateFibonacci(n-1) + calculateFibonacci(n-2));
        }
    }
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("请输入n的值:");
        int n = input.nextInt();
        Fibonacci fibonacci = new Fibonacci();
        long result = fibonacci.calculateFibonacci(n);
        System.out.println(result);
        input.close();
        for(int i = 1; i <= 20; i++){
            System.out.print(fibonacci.calculateFibonacci(i));
            System.out.print(" ");
        }
    }
}
