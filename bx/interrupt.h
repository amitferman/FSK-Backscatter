#ifndef _INTERRUPT_H_
#define _INTERRUPT_H_

#include "Arduino.h"

#define BIT_RATE 1000000 // 1 MHz

#define PERIODIC_ISR ISR(TIMER3_COMPA_vect)

void schedulePeriodicISR(uint16_t freq);

#endif // _INTERRUPT_H_
