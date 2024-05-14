#include <iostream>
using namespace std;

class Car
{
    public:
        string door;
        string light;
        int speed;
        void openDoor();
        void closeDoor();
        void openLight();
        void closeLight();
        void speedUp();
        void speedDown();
        void printStatus();
        Car();
};

Car::Car()
{
    door = "close";
    light = "close";
    speed = 0;
}

void Car::openDoor()
{
    door = "ON";
}

void Car::closeDoor()
{
    door = "OFF";
}

void Car::openLight()
{
    light = "ON";
}

void Car::closeLight()
{
    light = "OFF";
}

void Car::speedUp()
{
    speed += 10;
}

void Car::speedDown()
{
    speed -= 10;
}

void Car::printStatus()
{
    cout << "车门：" << door << endl;
    cout << "车灯：" << light << endl;
    cout << "速度：" << speed << endl;
}

int main()
{
    Car car;
    char cmd[20];
    cin >> cmd;
    int i = 0;
    while(cmd[i] != '\0')
    {
        switch (cmd[i])
        {
        case '1':
            car.openDoor();
            break;
        case '2':
            car.closeDoor();
            break;
        case '3':
            car.openLight();
            break;
        case '4':
            car.closeLight();
            break;
        case '5':
            car.speedUp();
            break;
        default:
            car.speedDown();
            break;
        }
        i++;
    }
    car.printStatus();
    return 0;
}