#include <msp430g2553.h>

int main(void)
{
    WDTCTL = WDTPW + WDTHOLD;
    P1DIR |= 0x01;
    for (;;)
    {
        volatile unsigned long i;
        P1OUT ^= 0x01;
        i = 99999;
        do
        {
            i--;
        } while (i != 0);
    }
}
