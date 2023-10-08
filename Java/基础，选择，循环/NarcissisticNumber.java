public class NarcissisticNumber {
    public static void main(String[] args){
        for(int i = 100;i < 1000;i++){
            int OnesPlace = i % 10;
            int TensPlace = (i / 10) % 10;
            int HundredsPlace = i / 100;
            if(Math.pow(OnesPlace,3) + Math.pow(TensPlace,3) + Math.pow(HundredsPlace,3) == i){
                System.out.print(i + " ");
            }
        }
    }
}
