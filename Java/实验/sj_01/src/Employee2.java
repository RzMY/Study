public class Employee2 {
    private String name, sex;
    int age, id;
    Employee2 (int id, String name, String sex, int age){
        this.id = id;
        this.name = name;
        this.sex = sex;
        this.age = age;
    }
    int getId(){
        return id;
    }
    String getName(){
        return name;
    }
    String getSex(){
        return sex;
    }
    int getAge(){
        return age;
    }
    public String toString(){
        String s;
        s = "id: " + id + " name: " + name + " sex: " + sex + " age: " + age;
        return s;
    }
}