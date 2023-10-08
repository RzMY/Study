import java.util.Scanner;
public class ComputeArea {
    public static void main(String[] args){
        double radius;
        double area;
        Scanner input = new Scanner(System.in);
        System.out.println("请输入r:");
        radius = input.nextDouble();
        area = Math.PI * radius * radius;
        System.out.println("圆的面积为:" + area);
        input.close();
    }
}
