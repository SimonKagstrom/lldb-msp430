/*===-- led_funcition_call.c -------------------------------------*- C++ -*-===//
//
//                     The LLVM Compiler Infrastructure
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===*/

#include <msp430g2553.h>

/* Delay function */
delay(unsigned int d) 
{
  unsigned int i;
  for (i = 0; i<d; i++) 
  {
    nop();
  }
}

/* Switch between green and red LED. This was tested with MSP430 Launchpad for which
 * LEDs are connected to PORT 1, pins 0 and 6*/
int main(void) 
{
  /* Stop watchdog timer*/
  WDTCTL = WDTPW | WDTHOLD;

  /* Set both LED pins (pin 0 and pin 6) as output */
  P1DIR = 0x41;

  /* Set LED connected to pin 0 as high/on */
  P1OUT = 0x01;

  for (;;) {
    /* Switch to the other LED*/
    P1OUT = ~P1OUT;
    delay(0x4fff);
  }
}
