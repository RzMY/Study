import java.util.Scanner;

class Person{
    private String name;
    private boolean gender;
    private int age;
    private int id;
    private static int counter;

    {
        id = counter++;
        System.out.println("This is initialization block, id is " + id);
    }
    
    static{
            counter = 0;
            System.out.println("This is static initialization block");
    }
    
    public Person(){
        System.out.println("This is constructor");
    }
    public Person(String name, boolean gender, int age){
        this.name = name;
        this.gender = gender;
        this.age = age;
    }

    public String getName(){
        return this.name;
    }
    public boolean getGender(){
        return this.gender;
    }
    public int getAge(){
        return this.age;
    }
    public int getId(){
        return this.id;
    }
    public String toString(){
        String s = "Person " + "[name=" + this.name + ", age=" + this.age + ", gender=" + this.gender + ", id=" + this.id + "]";
        return s;
    }
}

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        Person[] people = new Person[n];
        for(int i = 0; i < n; i++){
            String name = input.next();
            int age = input.nextInt();
            boolean gender = input.nextBoolean();
            people[i] = new Person(name, gender, age);
        }
        String s;
        for(int i = n-1; i >= 0; i--){
            s = people[i].toString();
            System.out.println(s);
        }
        Person init = new Person();
        System.out.println(init.getName() + "," + init.getAge() + "," + init.getGender() + "," + init.getId());
        s = init.toString();
        System.out.println(s);
        input.close();
    }
}