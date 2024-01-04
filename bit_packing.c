// an experiment in bit-packing in C
// TODO: write tests
#include <stdio.h>


/* BIT PACKING - BOOLS
 * This first part, I packed booleans into an int.
 * This lets me store 64 different flags in the memory space of a single
 * int sized register.
 *
 * When compiled, this was __kb for 4 flags when compared to __kb when
 * using 4 seperate ints to represent 4 flags. This strategy can be
 * helpful is space is an important concern, but it does introduce some
 * esoteric boilerplate to be accomplished, so it may only find use in
 * some particular use-cases.
 */
#define set_base(bases, value, offset) \
        bases = bases | ((uint8_t)value << (2 * offset))

#define get_base(bases, offset) \
        (bases & ((uint8_t)0b11 << (2 * offset))) >> (2 * offset)

int get_bool(int offset, int pack)
{
        return (pack & (1 << offset)) >> offset;
}

void set_bool(int offset, int *pack, int value)
{
        // clear bit
        *pack = *pack ^ (1 << offset);
        // set bit
        *pack = *pack | (value << offset);
}

void toggle_bool(int offset, int *pack)
{
        *pack = *pack ^ (1 << offset);
}



int
main(void)
{
        ///// Test for bools bit-packing /////
        int A = 0b0000;  // Frendly, Human, Wise, Shrewd - bools
        set_bool(0, &A, 1);
        set_bool(3, &A, 1);
        printf("%x : %i%i%i%i\n", A, get_bool(3, A), get_bool(2, A), get_bool(1, A), get_bool(0, A));
}
