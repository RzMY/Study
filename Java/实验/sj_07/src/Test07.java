import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.BufferedWriter;

public class Test07 {
    public static void main(String[] args) throws IOException {
        File f1 = new File("../test1.txt");
        File f2 = new File("../test2.txt");
        BufferedWriter out = new BufferedWriter(new FileWriter(f1));
        out.write("Hello!");
        out.newLine();
        out.write("Hello, nice to meet you!");
        out.newLine();
        out.close();

        FileInputStream fis = new FileInputStream(f1);
        InputStreamReader isr = new InputStreamReader(fis);
        BufferedReader in = new BufferedReader(isr);
        BufferedWriter out2 = new BufferedWriter(new FileWriter(f2));
        out2.write(in.readLine());
        out2.newLine();
        out2.write(in.readLine());
        out2.newLine();
        out2.close();
        in.close();
    }
}