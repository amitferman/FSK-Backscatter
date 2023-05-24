#ifndef _PWM_H_
#define _PWM_H_

#include "Arduino.h"
#include <avr/io.h>

#define TOP0  15 // 1000 kHz
#define TOP1  12 // 1230 kHz

#define pwm(x) if (x == 0) { TCNT4 = 0; OCR4A = TOP0; } else { TCNT4 = 0; OCR4A = TOP1; }

void initPWM();

#endif // _PWM_H_
