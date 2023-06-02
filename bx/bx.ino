/*
University of Washington
CSE 493W: Wireless Communication, Spring 2023
Author: Amit Ferman

Entry point for subcarrier Frequency-Shift-Keying (FSK) modulation.
Initializes pulse-width-modulation (pwm) for modulating an RF switch
and periodic interrupts for shifting the PWM frequency based on whether
we want to transmit a 0 or 1.
*/

#include "Arduino.h"
#include "pwm.h"
#include "interrupt.h"

// hard-coded bits to modulate
static const byte bits[] = {1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0};
static volatile uint16_t idx = 0;       // current bit index
static volatile byte next = bits[0];    // next bit to transmit

// interrupt service routine for periodically modulating the next bit
PERIODIC_ISR {
    pwm(next);                          // update pwm frequency
    idx = (idx + 1) % sizeof(bits);     // update idx
    next = bits[idx];                   // prepare next bit for next interrupt
}

void setup() {
    initPWM();
    initPeriodicISR();
}

void loop() {
    // test code
    // pwm(0)
    // delay(1);
    // pwm(1)
    // delay(1);
}
