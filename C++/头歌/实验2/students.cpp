/**
//测试输入：0 厉宏富 96 1 冷欣荣 85 2 鲍俊民 76

预期输出：

0 厉宏富 96
1 冷欣荣 85
2 鲍俊民 76
平均成绩 85.6667

*/
#include <iostream>
#include <sstream>
using namespace std;


class Student
{
    public:
        int SID;
        string Name;
        float Score;
        Student(){SID = 1, Name = "王小明", Score = 100;};
        Student(int sid,string name,float sco)
        {
            SID = sid;
            Name = name;
            Score = sco;
        };

};

class Students
{
    private:
        Student Student_List[5];
        int count;
    public:
        Students(){count = 0;}
        void Add(int sid,string name,float sco)
        {
            Student_List[count] = Student(sid,name,sco);
            count++;
        }
        void PrintAll()
        {
            for(int i = 0; i < count; i++)
            {
                cout << Student_List[i].SID << " " << Student_List[i].Name << " " << Student_List[i].Score << endl;
            }
        }
        void Average()
        {
            float sum = 0;
            for(int i = 0; i < count; i++)
            {
                sum += Student_List[i].Score;
            }
            cout << "平均成绩 " << sum/count << endl;
        }
};

int main()
{
    Students students;
    string inputLine;
    int sid;
    string name;
    float score;

    getline(cin, inputLine);
    istringstream iss(inputLine);

    while (iss >> sid >> name >> score)
    {
        students.Add(sid, name, score);
    }

    students.PrintAll();
    students.Average();
}