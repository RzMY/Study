public class Test01 {
    public static void main(String[] args){
        String name = "zhangsan", sex = "nan";
        int age = 10, id = 1;
        Employee2 employee_demo = new Employee2(id, name, sex, age);
        String s;
        s = employee_demo.toString();
        System.out.println(s);
    }
}