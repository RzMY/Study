/*
在C++中，友元是一个可以访问类的私有和保护成员的函数或类。它破坏了类的封装性，因此应谨慎使用。友元可以是一个函数，也可以是一个类。
*/


/*
友元函数：如果一个函数被声明为类的友元，那么这个函数就可以访问类的所有成员，无论它们是公有的、保护的还是私有的。
*/

class MyClass {
        private:
                int secretValue;
        public:
                friend void friendFunction(MyClass &mc);
};

void friendFunction(MyClass &mc) {
        mc.secretValue = 42;  // 可以访问私有成员
}

/*
友元类：如果一个类被声明为另一个类的友元，那么这个类的所有成员函数都可以访问另一个类的所有成员。
*/

class MyClass {
        private:
                int secretValue;
        public:
                friend class FriendClass;
};

class FriendClass {
        public:
                void changeSecretValue(MyClass &mc, int newValue) {
                        mc.secretValue = newValue;  // 可以访问私有成员
                }
};