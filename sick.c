// Jacobus Burger (2024-07-04)
// A basic program that appends "achu" onto a word. To commemorate getting sick from 2024-07-02 to 2024-07-05. Written in C because I haven't done a lot in C recently.
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


void help_info() {
        puts("Usage: sick [OPTION] ... [WORDS] ...");
        puts("Adds sneezing sounds to the end of a sentence or each word.");
        puts("");
        puts("With no OPTION, will only add an 'achu' at the end of sentence.");
        puts("  -e, --every     adds a sneeze to the end of every word");
        return;
}

int main(int argc, char *argv[])
{
        // show help info
        if (argc <= 1 || strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0) {
                help_info();
        }
        // process args
        bool every = false;
        string word = "achu";
        for (int i = 1; i < argc; i++) {
                if (strcmp(argv[1], "--every") == 0 || strcmp(argv[1], "-e") == 0)
                        every = true;
        }
        if (every) {
                for (int i = 2; i < argc; i++)
                        printf("%s%s ", argv[i], word);
        } else {
                for (int i = 1; i < argc - 1; i++)
                        printf("%s ", argv[i]);
                printf("%s%s ", argv[argc - 1], word);
        }
        puts("*sniffle*");
}
