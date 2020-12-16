#include <cstdio>

int sum(int x, int y)
{
    return x + y;
}

int main()
{
    int my_x = 520;
    int my_y = 1845;
    printf("The sum of %d and %d is %d.\n", my_x, my_y, sum(my_x, my_y));
}
