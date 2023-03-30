#include<gpu.h>
#include<riscv.h>
#include<dbgif.h>

[[ noreturn ]] void main(){
    // clear screen
    while(ccsrdrct(0, 0, 800, 600, 0x000));
    
    while(ccsrdln(400, 0, 800, 0, 0xFFF));
    while(ccsrdln(400, 0, 800, 300, 0xFFF));
    while(ccsrdln(400, 0, 800, 600, 0xFFF));
    while(ccsrdln(400, 0, 600, 600, 0xFFF));
    while(ccsrdln(400, 0, 400, 600, 0xFFF));
    while(ccsrdln(400, 0, 200, 600, 0xFFF));
    while(ccsrdln(400, 0, 0, 600, 0xFFF));
    while(ccsrdln(400, 0, 0, 300, 0xFFF));
    while(ccsrdln(400, 0, 0, 0, 0xFFF));

    for(;;);
}
