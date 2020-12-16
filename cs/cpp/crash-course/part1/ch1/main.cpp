#include <cstdio>

int step(int x)
{
    int stepped = 0;
    if (x > 0)
        stepped = 1;
    else if (x < 0)
        stepped = -1;
    return stepped;
}

int main()
{
    int num1 = 92;
    int result1 = step(92);
    printf("Num1: %d; Step: %d\n", num1, result1);

    return 0;
}
