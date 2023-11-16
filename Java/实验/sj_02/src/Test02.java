public class Test02 {
    public static void main(String[] args){
        Employee employee = new Employee("张三", "男", 25, 13000000);
        System.out.println("这是一名员工:");
        System.out.println("姓名：" + employee.getName());
        System.out.println("性别：" + employee.getGender());
        System.out.println("年龄：" + employee.getAge());
        System.out.println("员工号：" + employee.getEmpNo());
        employee.eat();
        employee.speak();
        employee.work();
        System.out.println();
        People people = new People("丽丝", "女", 16);
        System.out.println("这是一个普通的人:");
        System.out.println("姓名：" + people.getName());
        System.out.println("性别：" + people.getGender());
        System.out.println("年龄：" + people.getAge());
        people.eat();
        people.speak();
    }
}
