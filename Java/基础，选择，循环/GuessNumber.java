import java.util.Scanner;
public class GuessNumber {
    public static void main(String[] args){
        int magic = (int)(Math.random()*101) + 100;
        Scanner input = new Scanner(System.in);
        System.out.println("请输入你想猜的数:");
        int guess_num = input.nextInt();
        while(magic != guess_num){
            if(guess_num < magic){
                System.out.println("太小了");
            }else{
                System.out.println("太大了");
            }
            guess_num = input.nextInt();
        }
        System.out.println("恭喜你，猜对了！这个数是"+magic);
        input.close();
    }
}
