/*
University of Washington
CSE 493W: Wireless Communication, Spring 2023
Author: Amit Ferman

Defines an API for periodic interrupts.

Interrupt frequency = 16e6 / (BIT_RATE_TOP + 1)

See Fast PWM docs in Atmel ATmega datasheet, p.146: https://ww1.microchip.com/downloads/en/devicedoc/atmel-2549-8-bit-avr-microcontroller-atmega640-1280-1281-2560-2561_datasheet.pdf
*/

#ifndef _INTERRUPT_H_
#define _INTERRUPT_H_

#include "Arduino.h"

#define BIT_RATE_TOP 199 // 80kHz
// #define BIT_RATE_TOP 399 // 40kHz
// #define BIT_RATE_TOP 799 // 20 kHz 
// #define BIT_RATE_TOP 1599 // 10kHz
// #define BIT_RATE_TOP 3199 // 5kHz
// #define BIT_RATE_TOP 15999 // 1kHz


#define PERIODIC_ISR ISR(TIMER3_COMPA_vect)

void initPeriodicISR();

#endif // _INTERRUPT_H_
