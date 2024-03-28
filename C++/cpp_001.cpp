#include <iostream>
using namespace std;
#include <string.h>
#include <stdlib.h>
class CStrtemp
{    char *str;
public:
    CStrtemp(char *s);
    CStrtemp(const CStrtemp &);
    ~ CStrtemp();
     void set(char *s);
      void show() { cout<<str<<endl;  }
};
CStrtemp:: CStrtemp(char *s)
{   str=new char[strlen(s)+1];
    if(!str)  {   cout<<"Allocation Error\n";  exit(-1);   }
    strcpy(str,s);
    cout<<"CS"<<endl;
}
CStrtemp:: CStrtemp(const CStrtemp &temp)
{  str=new char[strlen(temp.str)+1];
    if(!str)  {  cout<<"申请内存错误\n"; exit(-1);  }
   strcpy(str,temp.str);
   cout<<"Copy CS"<<endl;
}
CStrtemp:: ~ CStrtemp( )
{  if(str!=NULL)   delete [ ]str; 
   cout<<"~CS"<<endl;
}
void CStrtemp::set(char *s)
{   delete [ ]str;
    str=new char[strlen(s)+1];
    if(!str){ cout<<"Allocation Error\n";   exit(-1);  }
    strcpy(str,s);
     cout<<"set"<<endl;
}
CStrtemp Input(CStrtemp temp)
{  char s[20];
    cin>>s;
    temp.set(s);    return temp;
}
int main()
{   CStrtemp a("hello");
    a.show( );
    CStrtemp b=Input(a);
    a.show( );
    b.show( );
    return 0;
}