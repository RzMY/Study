public class InitDemo {
    // 初值初始化
    int x = 100; 
    static int y = 100;
    // 初始化块
    {
        x = 60;
        System.out.println("x in initial block = " + x);
    }
    // 静态初始化块中只能使用静态变量
    static{
        y = 60;
    }
    // 构造方法初始化
    public InitDemo(){
        x = 58;
        System.out.println("x in constructor = " + x);
    }
    public static void main(String[] args){
        InitDemo demo = new InitDemo();
        System.out.println("after constructor x = " + demo.x);
        System.out.println("after constructor y = " + y);
        demo = null;// 删除引用
        System.gc();// 运行垃圾回收器
    }
}
