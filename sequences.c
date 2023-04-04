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

   Note that with this current packing scheme the estimated byte to base pair ratio would be 4bp:1byte. So that means roughly 4kbp in 1kb (not bad).
 */


// macro functions to manipulate packed 2bit words of each byte of bases
#define set_base(bases, value, offset) \
        bases = bases | ((uint8_t)value << (2 * offset))
#define get_base(bases, offset) \
        (bases & ((uint8_t)0b11 << (2 * offset))) >> (2 * offset)
// helper types
typedef uint8_t fbase;      // each byte of 4 bases
enum base { C, T, G, A };

// function to pack 4 char substring into a four-base byte
fbase pack(const char string[4]) {
        static fbase bases = 0b00000000;
        for (size_t i = 0; i < 4; i++) {
                switch (string[i]) {
                        case 'C':
                                set_base(bases, C, i);
                                break;
                        case 'T':
                                set_base(bases, T, i);
                                break;
                        case 'G':
                                set_base(bases, G, i);
                                break;
                        case 'A':
                                set_base(bases, A, i);
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
                        case C:
                                string[i] = 'C';
                                break;
                        case T:
                                string[i] = 'T';
                                break;
                        case G:
                                string[i] = 'G';
                                break;
                        case A:
                                string[i] = 'A';
                                break;
                }
        }
        return string;
}

// function to convert a string to a dna sequence
void string_to_sequence(const char *string, fbase *sequence, size_t sequence_length) {
        char substring[5] = "____\0";
        for (size_t i = 0; i < sequence_length; i++) {
                // copy substring from string
                memcpy(substring, (string + (4 * i)), 3);
                // for (size_t j = 0; j < 4; j++) substring[j] = string[4 * i + j];
                substring[4] = '\0';  // terminate string
                // pack substring into sequence byte
                sequence[i] = pack(substring);
        }
}

// function to convert a dna sequence to a string
void sequence_to_string(const fbase *sequence, char *string, size_t sequence_length) {
        char substring[5] = "____\0";
        for (size_t i = 0; i < sequence_length; i++) {
                // unpack sequence byte into substring
                memcpy(substring, unpack(sequence[i]), 3);
                // copy substring into string
                memcpy((string + (4 * i)), substring, 3);
                // for (size_t j = 0; j < 4; j++) string[(4 * i) + j] = substring[j];
                string[4 * sequence_length + 1] = '\0';  // terminate string
        }
}





// I suspect that memcpy is causing trouble through pointer stuff
void show_addr(const char *array, size_t length) {
        for (size_t i = 0; i < length; i++) {
                printf("|%u %x|", *(array + i), (array + i));
        }
        puts("");
}







int main(void) {
        fbase sequence[2];
        char start[8] = "CTGAAGTC";
        char test[8] = "________";

        show_addr(sequence, 2);
        show_addr(start, 8);
        show_addr(test, 8);

        string_to_sequence(start, sequence, 2);
        printf("%s %lu %lu -> %i %i %lu %lu\n", start, sizeof(char), sizeof(start), sequence[0], sequence[1], sizeof(fbase), sizeof(sequence));
        sequence_to_string(sequence, start, 2);
        printf("%i %i %lu %lu -> %s %s\n", sequence[0], sequence[1], sizeof(fbase), sizeof(sequence), start, test);

        show_addr(sequence, 2);
        show_addr(start, 8);
        show_addr(test, 8);
}
