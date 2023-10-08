public class homework_weeks2{
    public static void main(String[] args){
        if(3*3*3 + 4*4*4 + 5*5*5 == 6*6*6){
            System.out.println("3^3+4^3+5^3 = 6^3 成立");
        }else{
            System.out.println("3^3+4^3+5^3 = 6^3 不成立");
        }
        int sum = 0;
        for(int i = 6; i <= 69; i++){
            sum = sum + i*i*i;    
        }
        if(sum == 180*180*180){
            System.out.println("6^3+7^3+.....+69^3 = 180^3 成立");
        }else{
            System.out.println("6^3+7^3+.....+69^3 = 180^3 不成立");
        }
        System.out.println("1000以内这样的关系有:");
        for(int i = 0; i <= 1000; i++){
            for(int j = i - 1; j >= 1; j--){
                sum = 0;
                for(int k = j; k >= 1; k--){
                    sum = sum + k*k*k;
                    if(sum == i*i*i){
                        System.out.printf("%d^3+.....+%d^3 = %d^3%n",k,j,i);
                    }
                }
            }
        }
    }
}
