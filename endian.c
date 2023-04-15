// Jacobus Burger (2023)
// Determine endianess of system using value of byte order
#include <stdio.h>


int main(void) {
        /* Explanation:
         *      Knowing how big and little endianness work in a register,
         *      we can assign i to some non-zero byte value (such as 1, or
         *      0x0D) and it will occupy the last byte (from left to right)
         *      if it is little endian. Thus, if we get the address of
         *      the variable i, and then point to it with a char pointer,
         *      we can reference the value at that register in a single
         *      byte, which will truncate the value stored at the register
         *      to the "rightmost" byte of the register. In big endian,
         *      that would mean a value of 0. In little endian, that would
         *      mean whatever value we assigned to that first byte (to i).
         */
        unsigned int i = 0x0D;
        if ((char*)&i)
                puts("Little Endian!");
        else
                puts("Biggle Endian!");
}
