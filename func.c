#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* functional(ish) C programming demo
 *
 * These principles are applied:
 * + Pure functions over impure functions
 * + Stateless and immutable over global state and mutable
 * + Static typing and type conversions over type coercions
 *
 * This is still C though, so these principles while followed carefully depend
 * on what is being done and why. For instance, functions are pure, but memory
 * may be modified rather than copied under the hood.
 *
 * By applying the preferences and designs for pure functions and minimized
 * state the code will be more predictable and maintainable.
 */

typedef struct {
        char *name;
        int total;
} score;


// sum of two integers
int sum(int a, int b) {
        return a + b;
}


// product of two integers
int product(int a, int b) {
        return a * b;
}


// higher order function
// assumes both A and B are length long and stores result in C
void map(int (*f)(int, int), int *A, int *B, int *C, size_t length) {
        for (size_t i = 0; i < length; i++)
                C[i] = (*f)(A[i], B[i]);
}

int reduce(int (*f)(int, int), int *A, size_t length) {
        static int accumulator = -1;
        if (length == 0)
                return accumulator;
        accumulator = A[0];
        for (size_t i = 1; i < length; i++)
                accumulator = (*f)(accumulator, A[i]);
        return accumulator;
}


score tally(const score user, int *points, size_t length) {
        score s = {user.name, 0};
        s.total = reduce(&sum, points, length);
        return s;
}



int main(void) {
        int A[5] = {1, 2, 3, 4, 5};
        int B[5] = {2, 2, 2, 2, 2};
        int C[5] = {0};

        puts("original lists:");
        printf("%c: %i %i %i %i %i\n", 'A', A[0], A[1], A[2], A[3], A[4]);
        printf("%c: %i %i %i %i %i\n", 'B', B[0], B[1], B[2], B[3], B[4]);
        printf("%c: %i %i %i %i %i\n\n", 'C', C[0], C[1], C[2], C[3], C[4]);

        map(&sum, A, B, C, 5);

        puts("lists with sum function:");
        printf("%c: %i %i %i %i %i\n", 'A', A[0], A[1], A[2], A[3], A[4]);
        printf("%c: %i %i %i %i %i\n", 'B', B[0], B[1], B[2], B[3], B[4]);
        printf("%c: %i %i %i %i %i\n\n", 'C', C[0], C[1], C[2], C[3], C[4]);

        map(&product, A, B, C, 5);

        puts("lists with product function:");
        printf("%c: %i %i %i %i %i\n", 'A', A[0], A[1], A[2], A[3], A[4]);
        printf("%c: %i %i %i %i %i\n", 'B', B[0], B[1], B[2], B[3], B[4]);
        printf("%c: %i %i %i %i %i\n\n", 'C', C[0], C[1], C[2], C[3], C[4]);

        printf("reduce sum of A: %i\n\n", reduce(&sum, A, 5));

        score user = {"Jay", 0};
        user = tally(user, A, 5);
        printf("score of user %s: %i\n", user.name, user.total);
}
