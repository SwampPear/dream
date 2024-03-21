.write
mov X0, #1      // fd
adr X1, testdir // string to print
mov X2, #13,    // length of our string // mov used for small numbers < 255
mov X16, #4     // MacOS write system call
ret