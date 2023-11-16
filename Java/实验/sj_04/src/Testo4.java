import java.io.*;
public class Testo4 {
    public static void main(String[] args) throws WeekExcotion, IOException{
        Week w = new Week();
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        try{
            System.out.println("请输入要查询的编号(1-7):");
            w.number = in.readLine();
            if(Integer.parseInt(w.number) < 1||Integer.parseInt(w.number) > 7)
                throw new WeekExcotion();
        } catch (WeekExcotion e){
                e.printStackTrace();
            }
        for(int i = 0; i < 7; i++){
            if(i == Integer.parseInt(w.number)-1){
                System.out.println(w.days[i]);
                break;
            }
    
        }
    }
}
