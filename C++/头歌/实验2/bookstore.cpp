#include <string>
#include <iostream>
using namespace std;

class User
{
    public:
        static int UserCount;
        static int BookCount;
        string Name;
        int Books;
        User(string name,int books);
        ~User();
        static void GetState();
};

int User::UserCount=0;
int User::BookCount=0;

User::User(string name,int books):Name(name),Books(books)
{
    UserCount++;
    cout<<Name<<" "<<Books<<" "<<"进入"<<endl;
    BookCount += Books;
}

User::~User()
{
    UserCount --;
    cout<<Name<<" "<<Books<<" "<<"离开"<<endl;
    BookCount -= Books;
}

void User::GetState()
{
    cout<<"书店人数:"<<User::UserCount<<"，书店共享书数量:"<<User::BookCount<<"，人均共享数量:"<< User::BookCount/User::UserCount <<endl;
}