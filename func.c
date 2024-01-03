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





// standard functions
int sum(int a, int b) {
        return a + b;
}
int product(int a, int b) {
        return a * b;
}

// higher order functions
void filter(bool (*f)(int), int *A, int *B, size_t length) {
        // preconditions:
        //      length is same for A and B
        //      A is the values to filter
        //      B is the filtered results ending with a null terminator
        int i = 0;
        while (i < length) {
                if ((*f)(A[i])) {
                        B[i] = A[i];
                        i++;
                }
        }
}
void map(int (*f)(int, int), int *A, int *B, int *C, size_t length) {
        // take a func f and 2 arrays A and B and map result into C
        for (size_t i = 0; i < length; i++)
                C[i] = (*f)(A[i], B[i]);
}
int reduce(int (*f)(int, int), int *A, size_t length) {
        // take a func f applied to A and return the accumulated result
        accumulator = A[0];
        for (size_t i = 1; i < length; i++)
                accumulator = (*f)(accumulator, A[i]);
        return accumulator;
}





// demo of ADT's
typedef struct {
        char *id;
        unsigned health;
        int speed;
        int x, y;
} player;
player move(player p, int delta) {
        // the power of pass-by-value
        p.speed += delta;
        return p;
}
player damage(player p, int points) {
        if (points > p.health)
                p.health = 0;
        p.health -= points;
        return p;
}
typedef struct {
        char *name;
        int total;
} score;
score tally(const score user, int *points, size_t length) {
        score s = {user.name, 0};
        s.total = reduce(&sum, points, length);
        return s;
}





int main(void) {
        // demo higher order functions
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


        // demo game with player
        player a = {"AE13", 10, 0, 1, 1};
        player b = move(a, 10);
        printf("a: %s %u %i %i %i\n", a.id, a.health, a.speed, a.x, a.y);
        printf("b: %s %u %i %i %i\n", b.id, b.health, b.speed, b.x, b.y);
        b = move(b, 2);
        b = damage(b, 3);
        printf("a: %s %u %i %i %i\n", a.id, a.health, a.speed, a.x, a.y);
        printf("b: %s %u %i %i %i\n\n", b.id, b.health, b.speed, b.x, b.y);

        // demo scorekeeping with higher order functions
        score user = {"Jay", 0};
        user = tally(user, A, 5);
        printf("score of user %s: %i\n", user.name, user.total);
}
