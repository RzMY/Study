public class CharBoolDemo {
    public static void main(String[] args){
        boolean b;
        char ch1,ch2;
        ch1 = 'Y';
        ch2 = 65;// 字符型变量可以用单引号括起来的字符来初始化，也可以用整数来初始化，整数会被转换为对应的 ASCII 码字符
        System.out.println("ch1 = "+ch1+",ch2 = "+ch2);
        b = ch1==ch2;
        System.out.println(b);
        ch2 ++;
        System.out.println("ch2="+ch2);
    }
}
