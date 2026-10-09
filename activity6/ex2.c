#include <stdio.h>
#include <string.h>

void greeting(void) {
    printf("Welcome to exercise II\n");
    printf("I hope you enjoy it\n\n");
}

void concat_arguments(int argc, char **argv) {
    char buf[20] = "0123456789012345678";
    char *p = buf;
    int i;

    printf("&i = %p\n", (void *)&i);
    printf("&buf[0] = %p\n", (void *)buf);

    for (i = 1; i < argc; i++) {
        strcpy(p, argv[i]);
        p += strlen(argv[i]);

        if (i + 1 != argc) {
            *p++ = ' ';
        }
    }

    printf("%s\n", buf);
}

int main(int argc, char **argv) {
    printf("&main = %p\n", (void *)main);
    printf("&concat_arguments = %p\n",
           (void *)concat_arguments);
    printf("&greeting = %p\n", (void *)greeting);

    greeting();
    concat_arguments(argc, argv);

    return 0;
}
