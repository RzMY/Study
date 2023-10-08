public final class Sun {
    private static final Sun INSTANCE = new Sun();
    private int a = 0;
    private Sun(){} // private : 外部不能直接通过构造方法创建Sun的实例，必须通过getInstance()方法或者INSTANCE常量返回唯一实例
    public static synchronized Sun getInstance(){
        return INSTANCE;
    }
    public void methodA(){
        a ++;
        System.out.println("a = " + a);
    }
    public static void main(String[] args){
        Sun sun1 = Sun.getInstance();
        Sun sun2 = Sun.getInstance();
        Sun sun3 = INSTANCE;
        sun1.methodA();
        sun2.methodA();
        sun3.methodA();
        System.out.println(sun1 == sun2 && sun1 == sun3); // sun1 sun2引用同一实例
    }
}
