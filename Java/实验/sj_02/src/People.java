public class People {
    protected String name;
    protected String gender;
    protected int age;

    public void eat(){
        System.out.println("我是人，我爱吃饭！");
    }
    public void speak(){
        System.out.println("我是人，我爱说话！");
    }
    public String getName(){
        return name;
    }
    public String getGender(){
        return gender;
    }
    public int getAge(){
        return age;
    }

    public People(String name, String gender, int age){
        this.name = name;
        this.gender = gender;
        this.age = age;
    }
}
