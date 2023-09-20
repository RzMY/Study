import java.util.Scanner;
public class Noun {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("请输入你的出生年份:");
        int year = input.nextInt();
        switch((year - 1900) % 12){
            case 0:
                System.out.println("鼠");
                break;
            case 1:
                System.out.println("牛");
                break;
            case 2:
                System.out.println("虎");
                break;
            case 3:
                System.out.println("兔");
                break;
            case 4:
                System.out.println("龙");
                break;
            case 5:
                System.out.println("蛇");
                break;
            case 6:
                System.out.println("马");
                break;
            case 7:
                System.out.println("羊");
                break;
            case 8:
                System.out.println("猴");
                break;
            case 9:
                System.out.println("鸡");
                break;
            case 10:
                System.out.println("狗");
                break;
            case 11:
                System.out.println("猪");
                break;
        }
        input.close();
    }
}
