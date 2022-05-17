//验证Goldbach猜想: 任何一个不小于6的偶数均可表示为两个质数之和.

#include <stdio.h>

//判断整数n是否为质数 
int isPrime(int n)
{
    int k;
    if(n == 1)			return 0;
    if(n == 2)			return 1;
    if(n % 2 == 0)		return 0;
    for(k = 3; k * k <= n; k += 2)
        if(n % k == 0)  return 0;
    return 1;
}

int main()
{
    int n, x, y, m, count = 0;

    printf("请输入一个不小于6的偶数: ");
    scanf("%d", &m);

    for(n = 6; n <= m; n += 2)
	{
        for(x = 3; x <= n/2; x += 2)
        	//若x和y都是质数
            if(isPrime(x) && isPrime(y = n - x))  
                printf("%d = %d + %d\t", n, x, y);
		printf("\n");
	}
    printf("\n");
    
    return 0;
}
