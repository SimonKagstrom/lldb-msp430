NOTE: Please note that the history of commits is currently missing. It will be fixed and updated as soon as possible.

MSP430 LLDB Debugger
====================
This is an LLDB-based MSP430 debugger which has been developed to work with the mspdebug gdb-server (note that mspdebug can be used as a standalone debugger).

Check out the slides from the tutorial given at Euro LLVM Developers' Conference 2016, Barcelona:
    ... (to follow after the conference)

In Codeplay/examples, you will find source code for the examples that we use in our presentation. Use them at your own risk.

Deepak Panickal and Andrzej Warzynski, Codeplay Software

Getting Started
===============

The MSP430-LLDB repository is based on LLDB release 3.8. Note that LLVM 3.8 is also required.
It can be obtained from here: https://github.com/llvm-mirror

Tried & tested build systems:
*  CMake
Tried & tested compilers:
*  gcc 4.8.5
*  clang 3.8
Tried & tested platforms:
*  Linux
Tried & tested hardware:
* mspdebug simulator
* MSP-EXP430G2 LaunchPad development tool

Building with make
-------------------

    mkdir build && cd build
    cmake -G "Unix Makefiles" -DLLVM_TARGETS_TO_BUILD=MSP430 <llvm_root_directory>
    make lldb


Compiling MSP430 examples
-------------------------
    Step 1: Obtain the cross-compiler and binutils. 
    
    On Debian-based Linux distributions:
    > sudo apt-get install binutils-msp430 gcc-msp430 msp430-libc mspdebug

    Downloading from the vendor:
    > http://www.ti.com/tool/msp430-gcc-opensource
    > http://dlbeer.co.nz/mspdebug/

    Step 2: Compilation
    > cd lldb-msp430/Codeplay/examples
    > msp430-gcc -mmcu=msp430g2553 -O0 -g led.c

Debugging with MSP430-LLDB
--------------------------

    Step 1: Start mspdebug in gdb-server mode
    > mspdebug sim
    (mspdebug) prog led.elf
    (mspdebug) gdb

    Step 2: Start lldb and connect to mspdebug (by default uses port 2000)
    > lldb
    (lldb) file led.elf
    (lldb) settings set plugin.process.gdb-remote.target-definition-file <lldb_root>/examples/msp430_target_definition.py
    (lldb) gdb-remote 2000
    (lldb) b main
    (lldb) continue
