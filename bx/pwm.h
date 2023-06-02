/*
University of Washington
CSE 493W: Wireless Communication, Spring 2023
Author: Amit Ferman

Defines API for pulse-width modulating pin 6 (PH3/OCRA).

PWM frequency for bit 0 = 16e6 / (TOP0 + 1)

PWM frequency for bit 1 = 16e6 / (TOP1 + 1)

See Fast PWM docs in Atmel ATmega datasheet, p.146: https://ww1.microchip.com/downloads/en/devicedoc/atmel-2549-8-bit-avr-microcontroller-atmega640-1280-1281-2560-2561_datasheet.pdf
*/

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
