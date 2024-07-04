// Jacobus Burger (2024-07-04)
// A basic program that appends "achu" onto a word. To commemorate getting sick from 2024-07-02 to 2024-07-05. Written in C because I haven't done a lot in C recently.
#include <stdio.h>

int main(int argc, char *argv[])
{
        if (argc < 1) {
                puts("~ACHU~");
        }
        for (int i = 0; i < argc; i++) {
                printf("i: %i, w: %s", i, argv[i]);
        }
}
