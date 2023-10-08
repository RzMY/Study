public class ArrayDemo {
    public static void main(String[] args){
        double marks[] = new double[5];
        marks[0] = 79;
        marks[1] = 80;
        marks[2] = 81;
        marks[3] = 85;
        System.out.println(marks[3]);
        System.out.println(marks.length);
        for(int i = 0; i < marks.length; i++){
            System.out.println(marks[i]);
        }
    }
}
