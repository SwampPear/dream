.text               // this section contains code
.global _start      // identifies '_start' as the entry point
.align 2
_start:
    /*
    system exit
    system calls made through register 0
    SYS_EXIT = 1
    mov can be used to move small numbers into registers under 255
     */
    mov X0, #1

    adr X1, helloworld // string to print
    mov X2, #13     // length of our string
    mov X16, #4     // MacOS write system call

    /*
    software interrupt
     */
    svc #0

    // Setup the parameters to exit the program
    // and then call Linux to do it.

    mov X0, #0      // Use 0 return code
    mov X16, #1     // Service command code 1 terminates this program
    svc #0          // Call MacOS to terminate the program

helloworld: .ascii  "Hello World!\n"