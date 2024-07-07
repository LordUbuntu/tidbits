// Jacobus Burger (2024-07-04)
// A basic program that appends "achu" onto a sound. To commemorate getting sick from 2024-07-02 to 2024-07-05. Written in C because I haven't done a lot in C recently.
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


void help_info() {
        puts("Usage: sick [OPTION] ... [soundS] ...");
        puts("Adds sneezing sounds to the end of a sentence or each sound.");
        puts("");
        puts("With no OPTION, will only add an 'achu' at the end of sentence.");
        puts("  -e, --every     adds a sneeze to the end of every sound");
        puts("  -s, --sound     define the sneeze sound at the end of sounds");
}

int main(int argc, char *argv[])
{
        // show help info
        if (argc <= 1 || strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0) {
                help_info();
                return 1;
        }
        // process args
        bool every = false;
        char sound[2048] = "achu"; // temp solution because I fear alloc
        for (int i = 1; i < argc; i++) {
                if (strcmp(argv[i], "--every") == 0 || strcmp(argv[i], "-e") == 0)
                        every = true;
                // set new sound if defined
                if (strcmp(argv[i], "--sound") == 0 || strcmp(argv[i], "-s") == 0) {
                        if (i + 1 < argc)
                                strcpy(sound, argv[i + 1]);
                        else
                                strcpy(sound, "");
                }
                if (strcmp(sound, "") == 0) {
                        help_info();
                        return 1;
                }
        }
        if (every) {
                for (int i = 2; i < argc; i++)
                        printf("%s%s ", argv[i], sound);
        } else {
                for (int i = 1; i < argc - 1; i++)
                        printf("%s ", argv[i]);
                printf("%s%s ", argv[argc - 1], sound);
        }
        puts("*sniffle*");
        return 0;
}
