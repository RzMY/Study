public class Student {
    public int id;
    public String name;
    public int age;
    public String gender; // 实例变量
    public static int grade = 2022;  // 静态变量
    public Student(){}
    public Student(int id, String name, int age, String gender){
        this.id = id;
        this.name = name;
        this.age = age;
        this.gender = gender;
    }
    public void sayHello(){
        System.out.println("Hello, my name is " + name);
    }
    public int getAge(){
        return(age);
    }
    public void setAge(int age){
        this.age = age;
    }
    public int getID(){
        return(id);
    }
    public int getGrade(){
        return(grade);
    }
    public String getGender(){
        return(gender);
    }
    public static void main(String[] args){
        Student jack = new Student(202203802, "jack", 19, "男");
        Student bob = new Student(202203801, "bob", 19, "男");
        Student sophia = new Student(202203803, "sophia", 20, "女");
        Student student_null = new Student();
        jack.sayHello();
        bob.sayHello();
        sophia.sayHello();
        System.out.println("The grade of jack is " + jack.getGrade());
        System.out.println("The gender of jack is " + jack.getGender());
        System.out.println("The grade of jack is " + jack.getGrade());
        System.out.println("The gender of bob is " + bob.getGender());
        grade = 2020;
        bob.gender = "女";
        System.out.println("The grade of jack is " + jack.getGrade());
        System.out.println("The gender of jack is " + jack.getGender());
        System.out.println("The grade of jack is " + jack.getGrade());
        System.out.println("The gender of bob is " + bob.getGender());

        // 成员变量的初值
        System.out.println("The grade of null is " + student_null.getGrade());
        System.out.println("The gender of null is " + student_null.getGender());
        System.out.println("The ID of null is " + student_null.getID());
        System.out.println("The age of null is " + student_null.getAge());
    }
}
