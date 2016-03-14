#include <msp430g2553.h>

/* Delay function */
delay(unsigned int d) 
{
  int i;
  for (i = 0; i<d; i++) 
  {
    nop();
  }
}

int main(void) 
{
  WDTCTL = WDTPW | WDTHOLD;
  P1DIR = 0xFF;
  P1OUT = 0x01;

  for (;;) {
    /* LED on and off */
    P1OUT = ~P1OUT;
    delay(0x4fff);
  }
}