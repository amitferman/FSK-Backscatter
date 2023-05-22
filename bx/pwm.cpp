#include "Arduino.h"
#include <avr/io.h>
#include "pwm.h"

void initPWM() {
  // clear
  DDRH = 0;
  TCCR4A = 0;
  TCCR4B = 0;

  // set arduino pin 6 (PH3/OC4A) as output
  DDRH |= (1 << PH3);

  // set fast PWM mode, non-inverting, and no prescalar on timer 4
  TCCR4A |= (1 << WGM41) | (1 << WGM40) | (1 << COM4A0);
  TCCR4B |= (1 << WGM43) | (1 << WGM42) | (1 << CS40);
}
