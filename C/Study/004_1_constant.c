/*
212 //合法的
215u //合法的
0xFeel //不合法的 0x或0X开头的十六进制整数
078 //不合法的 0开头的八进制整数
032UU //不合法的 后缀不能重复

85 //十进制
0213 //八进制
0x4b //十六进制
30 //整数
30u //无符号整数
30l //长整数
30ul //无符号长整数

int myInt = 10;
long myLong = 100000L;//L是long的后缀
unsigned int myUnsignedInt = 100000u;//u是unsigned int的后缀

3.1415926 //合法的
3.12159E-6L //合法的 e或E前缀表示指数形式
510E //不合法的 缺少指数的整数
210f //不合法的 缺少小数或整数的小数点
.e55 //不合法的 缺少整数或分数

float myFloat = 3.14f;//f是float的后缀
double myDouble = 3.14159;

\\ // \字符
\' // '字符
\" // "字符
\? // ?字符
\a // 警报铃声
\b // 退格键
\f // 换页符
\n // 换行符
\r // 回车
\t // 水平制表符
\v // 垂直制表符
\ooo //一到三位的八进制数
\xhh //一个或多个数字的十六进制数
*/