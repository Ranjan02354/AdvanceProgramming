#include <stdio.h>
#include <time.h>
#include <stdlib.h>

volatile int sink = 0;

void constant_time(int n)
{
    int a = 10;
    int b = 20;

    sink += a + b;
}

void linear_time(int n)
{
    int *arr = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        arr[i] = i;
        sink += arr[i];
    }

    free(arr);
}

void quadratic_time(int n)
{
    int **matrix = (int **)malloc(n * sizeof(int *));

    for (int i = 0; i < n; i++)
    {
        matrix[i] = (int *)malloc(n * sizeof(int));
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            matrix[i][j] = i + j;
            sink += matrix[i][j];
        }
    }

    for (int i = 0; i < n; i++)
    {
        free(matrix[i]);
    }

    free(matrix);
}

double measure(void (*func)(int), int n, int repeat)
{
    clock_t start = clock();

    for (int i = 0; i < repeat; i++)
    {
        func(n);
    }

    clock_t end = clock();

    return (double)(end - start) / CLOCKS_PER_SEC;
}

int main()
{
    int sizes[] = {100, 500, 1000, 2000, 4000};
    int repeat = 1000;

    printf("Input Size\tO(1)\t\tO(n)\t\tO(n^2)\n");

    for (int i = 0; i < 5; i++)
    {
        int n = sizes[i];

        double t1 = measure(constant_time, n, repeat);
        double t2 = measure(linear_time, n, repeat);
        double t3 = measure(quadratic_time, n, repeat);

        printf("%d\t\t%f\t%f\t%f\n", n, t1, t2, t3);
    }

    return 0;
}