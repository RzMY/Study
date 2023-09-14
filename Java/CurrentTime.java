public class CurrentTime {
    public static void main(String[] args){
        long ms = System.currentTimeMillis();
        long s = ms / 1000;
        int day_s = (int)s % (24 * 60 * 60);
        int hours = (int)(day_s / (60 * 60));
        int minutes = (int)((day_s % (60 * 60)) / 60);
        int seconds = (int)(day_s % 60);
        System.out.println("现在时间为:"+(hours + 8)+":"+minutes+":"+seconds+" GMT+8");
    }
}
