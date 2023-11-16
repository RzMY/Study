public class Employee extends People{
    protected long EmpNo;
    public void eat(){
        System.out.println("我是员工，我爱吃饭！");
    }
    public void speak(){
        System.out.println("我是员工，我爱说话！");
    }
    public void work(){
        System.out.println("我是员工，我的工作内容很简单！");
    }
    public long getEmpNo(){
        return EmpNo;
    }

    public Employee(String name, String gender, int age, long EmpNo){
        super(name, gender, age);
        this.EmpNo = EmpNo;
    }
}
