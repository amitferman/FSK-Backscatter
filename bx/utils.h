/*
University of Washington
CSE 493W: Wireless Communication, Spring 2023
Author: Amit Ferman

Defines API for misc utils.

See Fast PWM docs in Atmel ATmega datasheet, p.146: https://ww1.microchip.com/downloads/en/devicedoc/atmel-2549-8-bit-avr-microcontroller-atmega640-1280-1281-2560-2561_datasheet.pdf
*/

#ifndef _UTILS_H_
#define _UTILS_H_

#include "Arduino.h"

/* 
uint16_t frequencyToTOP(uint16_t freq)
    freq      - desired frequency
    prescalar - timer prescalar

Returns TOP for given frequency and timer prescalar in Fast PWM mode.
*/
uint16_t frequencyToTOP(uint16_t freq, uint16_t prescalar);

#endif // _UTILS_H_
