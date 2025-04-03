#include <iostream>
#include <string>
using namespace std;

class Student {
    private:
        string id;
        string name;
        double score;
        static int count;
        static double total;
    public:
        Student(string id, string name, double score) {
            this->id = id;
            this->name = name;
            this->score = score;
            count++;
            total += score;
        }
        void display() {
            cout << "id: " << id << ", name: " << name << ", score: " << score << endl;
        }
        static void displayCount() {
            cout << "count: " << count << ", average: " << total / count << endl;
        }
};

int Student::count = 0;
double Student::total = 0;

int main() {
    Student s1("1", "张三", 90);
    Student s2("2", "李四", 80);
    Student s3("3", "王五", 70);
    Student s4("4", "赵六", 60);
    s1.display();
    s2.display();
    s3.display();
    s4.display();
    Student::displayCount();
    return 0;
}