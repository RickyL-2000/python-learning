//验证Goldbach猜想: 任何一个不小于6的偶数均可表示为两个质数之和.

1) #include <stdio.h>

//判断整数n是否为质数 
2) int isPrime(int n)
3) {
4)     int k;
5)     if(n == 1)			return 0;
6)     if(n == 2)			return 1;
7)     if(n % 2 == 0)		return 0;
8)     for(k = 3; k * k <= n; k += 2)
9)         if(n % k == 0)  return 0;
10)     return 1;
11) }

12) int main()
13) {
14)     int n, x, y, m, count = 0;

15)     printf("请输入一个不小于6的偶数: ");
16)     scanf("%d", &m);

17)     for(n = 6; n <= m; n += 2)
18) 	{
19)         for(x = 3; x <= n/2; x += 2)
        	//若x和y都是质数
20)             if(isPrime(x) && isPrime(y = n - x))  
21)                 printf("%d = %d + %d\t", n, x, y);
22) 		printf("\n");
23) 	}
24)     printf("\n");
    
25)     return 0;
26) }
