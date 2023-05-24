#ifndef _INTERRUPT_H_
#define _INTERRUPT_H_

#include "Arduino.h"

#define BIT_RATE_TOP 249 // 1 kHz // 8 // 1 MHz

#define PERIODIC_ISR ISR(TIMER3_COMPA_vect)

void initPeriodicISR();

#endif // _INTERRUPT_H_
