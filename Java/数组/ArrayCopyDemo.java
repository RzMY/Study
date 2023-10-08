public class ArrayCopyDemo {
    public static void main(String[] args){
        int a[] = {1,2,3,4};
        int b[] = {8,7,6,5,4,3,2,1};
        int c[] = {10,20};
        try{
            System.arraycopy(a,0,b,0,a.length);
            System.arraycopy(a,0,c,0,a.length);
        }catch(ArrayIndexOutOfBoundsException e){
            System.out.println(e);
        }
        for(int elem:b){
            System.out.println(elem);
        }
    }
}
