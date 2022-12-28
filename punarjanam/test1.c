#include <stdio.h>
#include <stdbool.h>

#define MAX_N 100

// Function to check if it is possible to find two 
// matrices such that when there corresponding 
// elements are combined in the form of (x,y), 
// the resulting matrix yield all n x n pairs 
bool findMatrices(int n, int A[][MAX_N], int B[][MAX_N])
{
    // initialize the array C to store the resulting matrix
    int C[MAX_N][MAX_N];

    // combine the corresponding elements of A and B
    // and store the result in C
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            C[i][j] = (A[i][j], B[i][j]);

    // check if C contains all n x n pairs
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            if (C[i - 1][j - 1] != (i, j))
                return false;

    return true;
}

int main(void)
{
    // test the function with an example
    int n = 3;
    int A[][MAX_N] = { { 1, 2, 3 }, { 3, 1, 2 }, { 2, 3, 1 } };
    int B[][MAX_N] = { { 1, 2, 3 }, { 2, 3, 1 }, { 3, 1, 2 } };

    if (findMatrices(n, A, B))
        printf("Yes\n");
    else
        printf("No\n");

    return 0;
}
