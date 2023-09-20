import java.util.Scanner;
public class HandGame {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("你出什么？石头:2 剪刀:1 布:0");
        int UserChoice = input.nextInt();
        int ComputerChoice =(int)(Math.random()*3);
        String UserChoiceCN = "";
        switch(UserChoice){
            case 2:
                UserChoiceCN = "石头";
                break;
            case 1:
                UserChoiceCN = "剪刀";
                break;
            case 0:
                UserChoiceCN = "布";
                break;
        }
        String ComputerChoiceCN = "";
        switch(ComputerChoice){
            case 2:
                ComputerChoiceCN = "石头";
                break;
            case 1:
                ComputerChoiceCN = "剪刀";
                break;
            case 0:
                ComputerChoiceCN = "布";
                break;
        }
        if(UserChoice == (ComputerChoice + 1) | (UserChoice == 0 & ComputerChoice == 2)){
            System.out.println("你赢了" + " 我出的是：" + ComputerChoiceCN + " 你出的是:" + UserChoiceCN);
        }else if(UserChoice == ComputerChoice){
            System.out.println("平局 我们出的都是" + ComputerChoiceCN);
        }else{
            System.out.println("你输了" + " 我出的是：" + ComputerChoiceCN + " 你出的是:" + UserChoiceCN);
        }
        input.close();
    }
}
