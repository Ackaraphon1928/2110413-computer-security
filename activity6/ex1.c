#include <stdio.h>
#include <stdint.h>

void myfunction(int i);

char *p;

int main(void) {
    printf("&main = %p\n", (void *)main);
    printf("&myfunction = %p\n", (void *)myfunction);
    printf("&&ret_addr = %p\n", &&ret_addr);

    myfunction(12);

ret_addr:
    printf("... end\n");
    return 0;
}

void myfunction(int i) {
    char buf[20] = "0123456789012345678";

    printf("&i = %p\n", (void *)&i);
    printf("sizeof(pointer) is %zu\n", sizeof(p));
    printf("&buf[0] = %p\n", (void *)buf);

    for (p = (char *)&i + 64;
         (uintptr_t)p >= (uintptr_t)buf;
         p--) {

        printf("%p: 0x%02x\t",
               (void *)p,
               *(unsigned char *)p);

        if (((uintptr_t)p % 4) == 0) {
            printf("\n");
        }
    }
    printf("\n");
}
