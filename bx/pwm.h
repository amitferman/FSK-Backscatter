#ifndef _PWM_H_
#define _PWM_H_

#include "Arduino.h"
#include <avr/io.h>

// #define TOP0  15 // 1000 kHz
// #define TOP1  9  // 1600 kHz
#define TOP0  7  // 2.000 MHz
#define TOP1  5  // 2.666 MHz

#define pwm(x) if (x == 0) { TCNT4 = 0; OCR4A = TOP0; } else { TCNT4 = 0; OCR4A = TOP1; }

void initPWM();

#endif // _PWM_H_
