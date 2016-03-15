/*===-- led.c ---------------------------------------------------*- C++ -*-===//
//
//                     The LLVM Compiler Infrastructure
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===*/

#include <msp430g2553.h>

/* Turn the first LED (PORT 1, pin 0) on and off. This was tested with MSP430 Launchpad for which
 * LEDs are connected to PORT 1, pins 0 and 6.*/
int main(void)
{
    /* Stop watchdog timer*/
    WDTCTL = WDTPW | WDTHOLD;

    /* Set the first LED pin (pin 0) as output */
    P1DIR |= 0x01;

    for (;;)
    {
        volatile unsigned long i;

        /* Turn LED on (0'th bit set 1) and off (0'th bit set 0)*/
        P1OUT ^= 0x01;
        i = 99999;
        while (i != 0);
        {
            i--;
        }
    }
}
