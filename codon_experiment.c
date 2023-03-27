/* Created by Jacobus Burger (2017)
 *
 * Info:
 *   A small experiment I wanted to try with representing CATG in a
 *   space-efficient manner.
 */
#include <stdio.h>
#include <stdlib.h>
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
        bases = bases | ((uint8_t)value << (2 * offset))
#define get_base(bases, offset) \
        (bases & ((uint8_t)0b11 << (2 * offset))) >> (2 * offset)
// helper types
typedef uint8_t fbase;      // each byte of 4 bases

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

// function to convert a string to a dna sequence
void string_to_sequence(char *string, fbase *sequence, size_t length) {
        char substring[4];
        for (size_t i = 0; i < length; i++) {
                // go 4 chars at a time to pack into each sequence element
                memcpy(substring, string + (4 * i), 4);
                sequence[i] = pack(substring);
                printf("%s %s %i", substring, string, sequence[i]);
        }
        puts("\n\n");
}

char *sequence_to_string(fbase *sequence, char *string, size_t length);


int main(void) {
        // TODO - write functions to operate on packed dna sequences
        fbase sequence[2];
        // dna sequence = (dna) calloc(2, sizeof(fbase));
        char string[8] = "CTGACTGA";    // CTGA CTGA
        string_to_sequence(string, sequence, 2);
        printf("%lu %lu, %lu %lu\n", sizeof(char), sizeof(string), sizeof(fbase), sizeof(sequence));
}
