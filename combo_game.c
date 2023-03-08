// Jacobus Burger (2023)
// A simple colour combination guessing game
// and my experiment in bit packing and bit magic
// note that the answer can be a combination of colours (order doesn't matter)
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>


int
main(void)
{
        char input[6];
        unsigned char answer = rand() % 16;
        unsigned char player = 0b0000; // 0bRGBW
        for (int i = 0; i < 8; i++)
        {
                // print prompt
                printf("toggle what color [red/green/blue/white]\n");
                // get input
                scanf("%s", input);
                // decide what to do
                if (strcmp("quit", input) == 0)
                        // end early
                        break;
                else if (strcmp("red", input) == 0)
                {
                        // toggle red bit
                        player = 0b1000 ^ player;
                        printf("toggled red\n");
                }
                else if (strcmp("green", input) == 0)
                {
                        // toggle green bit
                        player = 0b0100 ^ player;
                        printf("toggled green\n");
                }
                else if (strcmp("blue", input) == 0)
                {
                        // toggle blue bit
                        player = 0b0010 ^ player;
                        printf("toggled blue\n");
                }
                else if (strcmp("white", input) == 0)
                {
                        // toggle white bit
                        player = 0b0001 ^ player;
                        printf("toggled white\n");
                }
                else
                        printf("invalid input, try again!\n");
                if (player == answer)
                {
                        printf("You won!!!\n");
                        break;
                }
        }
}
