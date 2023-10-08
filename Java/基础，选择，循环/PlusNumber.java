import java.util.Scanner;
public class PlusNumber {
    public static void main(String[] args){
        System.out.println("请输入一个1000以内的正整数:");
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        if(num >= 100){
            int ge = num % 10;
            int shi = (int)(num % 100 / 10);
            int bai = (int)(num / 100);
            System.out.println("各位数相加等于="+(ge + shi + bai));
        }else if(num >= 10 & num < 100){
            int ge = num % 10;
            int shi = (int)(num / 10);
            System.out.println("各位数相加等于="+(ge + shi));
        }else if(num < 10){
            System.out.println("各位数相加等于="+num);
        }
        input.close();
    }
}
