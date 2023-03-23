/* Created by Jacobus Burger (2017)
 *
 * Info:
 *   A small experiment I wanted to try with representing CATG in a
 *   space-efficient manner.
 */
#include <stdio.h>
#include <stdint.h>
#include <string.h>

/* GENE SEQUENCE EXAMPLE
   This file acts as an example of representing 4 genetic bases
   in a structure with 4 values coinciding with each of the 4
   DNA bases. This allows each base to be represented with no more
   than 2 bits at one time.
   Ex:
   {C, T, G, A} == {0x0, 0x1, 0x2, 0x3}
    A T G| A T C| A C C| C T G
    3 1 2| 3 1 0| 3 0 0| 0 1 2
   110110|110100|110000|000110


   Thanks to T for inspiring the idea to represent each codon with
   a binary value.
 */

// imagine each codon as a byte with 4 2bit packed numbers representing CATG
// these definitions help with bit pairs and bit packing action
typedef uint8_t base;
typedef base *dna;
#define set_base(sequence, value, offset) \
        sequence |= ((uint8_t)value << (2 * offset))
#define get_base(sequence, offset) \
        ((uint8_t)0b11 << (2 * offset)) >> (2 * offset)
#define clr_base(sequence, offset) \
        sequence &= ~((uint8_t)0b11 << (2 * offset))

// convert a string into the packed bit nucleotide representation (PBNR)
int nucleotide(char *string, base sequence, size_t length) {
        return 0;
}

// show a representation of the current sequence
// note: if sequence == CAT (001101), length == 3
int print_sequence(base sequence, size_t length) {
        for (size_t i = 0; i < length; i++) {
                switch (get_base(sequence, i)) {
                        case 0:
                                printf("C");
                                break;
                        case 1:
                                printf("T");
                                break;
                        case 2:
                                printf("G");
                                break;
                        case 3:
                                printf("A");
                                break;
                        default:
                                return -1;
                }
        }
        return 0;
}


int main(void) {
        char *string;
        scanf("%ms", &string);
        size_t length = strlen(string);
}
