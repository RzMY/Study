//为了消除歧义，我们可以在 m_a 的前面指明它具体来自哪个类：
//这样表示使用 B 类的 m_a。
void seta(int a){ B::m_a = a; }
//当然也可以使用 C 类的：
void seta(int a){ C::m_a = a; }


