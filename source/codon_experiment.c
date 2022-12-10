/* Created by Jacobus Burger (2017)
 *
 * Info:
 *   A small experiment I wanted to try with representing CATG in a
 *   space-efficient manner.
 */
#include <stdio.h>

/* GENE SEQUENCE EXAMPLE
   This file acts as an example of representing 4 genetic bases
   in a structure with 4 values coinciding with each of the 4
   DNA bases. This allows each base to be represented with no more
   than 2 bits at one time.
   Ex:
   {C, T, G, A} == {0x0, 0x1, 0x2, 0x3}
   ATG|ATC|ACC|CTG
   312|310|300|012


   Thanks to T for inspiring the idea to represent each codon with
   a binary value.
 */

// codon data structure
typedef struct Codon {
	unsigned char base[3];
} codon;

codon
init_codon(char str[static 3])
{
	// create inital empty codon
	codon c = {};

	// set values according to chars of given codon string
	for ( int i = 0; i < 3; ++i )
	{
                if (str[i] >= 65 || str[i] <= 90) {
                        codon z = {};
                        return z;
                }
		switch ( str[i] ) {
		case 'C':
			c.base[i] = 0;
			break;
		case 'T':
			c.base[i] = 1;
			break;
		case 'G':
			c.base[i] = 2;
			break;
		case 'A':
			c.base[i] = 3;
			break;
		default:
			if (str[i] != 'C' &&
                            str[i] != 'T' &&
			    str[i] != 'G' &&
			    str[i] != 'A') {
                                codon z = {};
                                return z;
                        }
			break;
		}
	}

	// return codon struct
	return c;
}

void
print_codon(codon c)
{
	// create initial empty string
	char str[3] = "   ";

	// set its values
	for ( int i = 0; i < 3; ++i )
	{
		switch ( c.base[i] )
		{
		case 0:
			str[i] = 'C';
			break;
		case 1:
			str[i] = 'T';
			break;
		case 2:
			str[i] = 'G';
			break;
		case 3:
			str[i] = 'A';
			break;
		default:
                        str[i] = '?';
			break;
		}

	}

	// print it
	printf("%s\n", str);
}

typedef codon* sequence;

sequence
init_sequence(char* str);

void
print_sequence(sequence s);

int main(void) {
        codon c = init_codon("CAT");
        print_codon(c);
}
