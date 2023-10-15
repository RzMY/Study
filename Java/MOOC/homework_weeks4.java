import java.util.Arrays;
public class homework_weeks4{
    public static void main(String[] args){
        Teacher jack = new Teacher("jack", "001", "123456");
        jack.loginIn("001", "123456");
        jack.setClass("Java", "001", "周一", "jack", new String[]{"101", "102", "103"});
        jack.setClass("C++", "002", "周二", "jack", new String[]{"201", "202", "203"});
        jack.loginOut();
        Student tom = new Student("tom", "101", "123456");
        tom.loginIn("101", "123456");
        tom.chooseClass("C++", "002", "周二", "jack");
        tom.loginOut();
    }
}

interface loginable{
    boolean loginIn(String id, String pwd);
    boolean loginOut();
}

class Course{
    public String name;
    public String id;
    public String time;
    public String teacher;
    public String[] students;
    public void setClass(String name, String id, String time, String teacher, String[] students){
        this.name = name;
        this.id = id;
        this.time = time;
        this.teacher = teacher;
        this.students = students;
        System.out.println("课程创建成功，课程名称：" + name + "，课程编号：" + id + "，上课时间：" + time + "，授课老师：" + teacher + "，学生名单：" + Arrays.toString(students));
    }
}

abstract class User implements loginable{
    protected String name;
    protected String id;
    protected String pwd;
    protected String identity;

    public User(String name, String id, String pwd, String identity) {
        this.name = name;
        this.id = id;
        this.pwd = pwd;
        this.identity = identity;
    }

    @Override
    public boolean loginIn(String id, String pwd){
        if(!id.equals(this.id) || !pwd.equals(this.pwd)){
            System.out.println("用户名或密码错误！");
            return false;
        }
        System.out.println("你好，" + identity + name + "，欢迎回来！");
        return true;
    }

    @Override
    public boolean loginOut(){
        System.out.println("你已成功退出！");
        return true;
    }
}

class Teacher extends User{
    public Teacher(String name, String id, String pwd) {
        super(name, id, pwd, "教师");
    }
    public void setClass(String name, String id, String time, String teacher, String[] students){
        Course course = new Course();
        course.setClass(name, id, time, teacher, students);
    }
    {
        identity = "教师";
    }
}

class Student extends User{
    public Student(String name, String id, String pwd) {
        super(name, id, pwd, "学生");
    }
    public void chooseClass(String name, String id, String time, String teacher){
        System.out.println("你已成功选课，课程名称：" + name + "，课程编号：" + id + "，上课时间：" + time + "，授课老师：" + teacher);
    }
}

