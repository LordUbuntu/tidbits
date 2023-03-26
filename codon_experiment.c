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
   {C, T, G, A} == {0b00, 0b01, 0b10, 0b11}
    A T G| A T C| A C C| C T G
    3 1 2| 3 1 0| 3 0 0| 0 1 2
   110110|110100|110000|000110


   Thanks to T for inspiring the idea to represent each codon with
   a binary value.

   The design I've improved on is to have 4 bases represented as
   a set of 4 2bit numbers packed in a single uint8 byte. Then, we
   can represent 4 times the number of bases that a string would
   be able to represent, and then DNA is an array of these packed
   4-base nucleotide subsequences.
 */


// macro functions to manipulate packed 2bit words of each byte of bases
#define set_base(bases, value, offset) \
        bases |= ((uint8_t)value << (2 * offset))
#define get_base(bases, offset) \
        ((uint8_t)0b11 << (2 * offset)) >> (2 * offset)
#define clr_base(bases, offset) \
        bases &= ~((uint8_t)0b11 << (2 * offset))
// helper types
typedef uint8_t fbase;      // each byte of 4 bases
typedef fbase *dna;         // a sequence of bytes of 4 bases each

// helper functions

// function to pack 4 char substring into a four-base byte
fbase pack(const char string[4]) {
        static fbase bases = 0b00000000;
        for (size_t i = 0; i < 4; i++) {
                switch (string[i]) {
                        case 'C':
                                set_base(bases, 0b00, i);
                                break;
                        case 'T':
                                set_base(bases, 0b01, i);
                                break;
                        case 'G':
                                set_base(bases, 0b10, i);
                                break;
                        case 'A':
                                set_base(bases, 0b11, i);
                                break;
                }
        }
        return bases;
}

// function to unpack 4 char substring from a four-base byte
char *unpack(const fbase bases) {
        static char string[4] = "____";
        for (size_t i = 0; i < 4; i++) {
                switch (get_base(bases, i)) {
                        case 0b00:
                                string[i] = 'C';
                                break;
                        case 0b01:
                                string[i] = 'T';
                                break;
                        case 0b10:
                                string[i] = 'G';
                                break;
                        case 0b11:
                                string[i] = 'A';
                                break;
                }
        }
        return string;
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
                                return 1;
                }
        }
        return 0;
}


int main(void) {
        char *string = "CATG";
        size_t length = 4;

        base seq;
        int status = nucleotide(string, seq, length);
        status = print_sequence(seq, length);
        return status;
}
