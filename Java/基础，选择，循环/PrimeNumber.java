public class PrimeNumber {
    public static void main(String[] args){
        start:
        for(int count = 0, i = 2; count < 50; i++){
            for(int j = 2; j < i; j++){
                if(i % j == 0){
                    continue start;
                }
            }
            System.out.print(i + " ");
            count++;
            if(count % 10 == 0){
                System.out.println();
            }
        }
    }
}
