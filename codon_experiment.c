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
// functions to deal with bit packing
typedef uint8_t BASE;
#define set_base(codon, value, offset) \
        codon |= ((uint8_t)value << (2 * offset))

// some neat tricks that are realized is that by taking the nand or xor we can
// determine mismatches of the entire sequence in one operation.

// codon data structure
typedef struct BASE { unsigned char b : 2; }__attribute__((packed)) base;

typedef base *codon;

// convert a string into the packed bit nucleotide representation (PBNR)
int nucleotide(char *string, base *dest, size_t length) {
        for (size_t i = 0; i < length; i++) {
                switch (string[i]) {
                        case 'C':
                                dest[i] = (base){0};
                                break;
                        case 'T':
                                dest[i] = (base){1};
                                break;
                        case 'G':
                                dest[i] = (base){2};
                                break;
                        case 'A':
                                dest[i] = (base){3};
                                break;
                        default:
                                return 1;
                }
        }
        return 0;
}


int main(void) {
/*
        char *string;
        scanf("%ms", &string);
        size_t length = strlen(string);

        base seq[length];
        nucleotide(string, seq, length);

        printf("str: %s %ul %ul.\nseq: %ul %ul\n", string, sizeof(string), sizeof(char), sizeof(seq), sizeof(base));
        for (int i = 0; i < length; i++)
                printf("%i %c, ", seq[i], string[i]);
        puts("");
*/
}
