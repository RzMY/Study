import static java.lang.Math.*;
import static java.lang.System.*;

public class ImportStaticDemo {
    public static void main(String[] args){
        double d = random(); // 不需要加类名前缀
        double pi = PI;
        // out是System类的一个静态成员
        out.println("d = " + d);
        out.println("pi = " + pi);
    }
}
