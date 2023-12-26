import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.File;

public class Test06 {
    public static void main(String[] args) throws IOException {
        File f = new File("../test.txt");
        BufferedWriter out = new BufferedWriter(new FileWriter(f));

        out.write("This is test");
        out.newLine();
        out.write("这是一个写入测试");
        out.close();
    }
}