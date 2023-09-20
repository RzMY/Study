import java.util.Scanner;
public class GradeLevel {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("请输入你的成绩");
        int grade = input.nextInt();
        switch(grade){
            case 100: case 99: case 98: case 97: case 96: case 95:
                System.out.println("优秀");
                break;
            case 94: case 93: case 92: case 91: case 90: case 89: case 88: case 87: case 86: case 85:
                System.out.println("良好");
                break;
            case 84: case 83: case 82: case 81: case 80: case 79: case 78: case 77: case 76: case 75:
                System.out.println("中等");
                break;
            case 74: case 73: case 72: case 71: case 70: case 69: case 68: case 67: case 66: case 65:
                System.out.println("及格");
                break;
            default:
                System.out.println("不及格");
        }
        input.close();
    }
}
