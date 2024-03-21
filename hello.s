.text               // this section contains code
.global _start      // identifies '_main' as the entry point
.balign 4
_start:
mov X0, #1
adr X1, testdir // string to print
mov X2, #45    // length of our string // mov used for small numbers < 255
mov X16, #4     // MacOS write system call
//adr X0, #1
//adr X1, testdir
//mov X2, 0x777
//mov X16, #34
svc #0          // software interrupt // call to make system call
mov X0, #0      // Use SYS_EXIT = 0 return code // X0 for system calls
mov X16, #1     // Service command code 1 terminates this program
svc #0          // Call MacOS to terminate the program
helloworld: .ascii  "Hello World!\n"
testdir: .ascii  "/Users/michaelvaden/Desktop/dev/dream/testdir"