#include "Arduino.h"
#include <avr/io.h>
#include <avr/interrupt.h>
#include "interrupt.h"

void initPeriodicISR() {
  // clear
  DDRE = 0;
  TCCR3A = 0;
  TCCR3B = 0;
  TIMSK3 = 0;

  // set arduino pin 11 (PBE3/OC3A) as output
  DDRE |= (1 << PE3);

  TIMSK3 |= (1 << OCIE3A); 


  // set fast PWM mode, non-inverting, and prescalar 64 on timer 3
  // TCCR3A |= (1 << WGM31) | (1 << WGM30) | (1 << COM3A0);
  // TCCR3B |= (1 << WGM33) | (1 << WGM32) | (1 << CS31) | (1 << CS30);

  // set fast PWM mode, non-inverting, and prescalar 64 on timer 3
  TCCR3A |= (1 << WGM31) | (1 << WGM30) | (1 << COM3A0);
  TCCR3B |= (1 << WGM33) | (1 << WGM32) | (1 << CS30);

  // set TOP
  OCR3A = BIT_RATE_TOP;
}
