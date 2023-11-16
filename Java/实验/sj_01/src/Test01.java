public class Test01 {
    public static void main(String[] args){
        String name = "zhangsan", sex = "nan";
        int age = 10, id = 1;
        Employee employee_demo = new Employee(id, name, sex, age);
        String s;
        s = employee_demo.toString();
        System.out.println(s);
    }
}