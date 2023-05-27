#include "Arduino.h"
#include "pwm.h"
#include "interrupt.h"

static const byte bits[] = {0,1,1,1,0,1};
static volatile uint16_t idx = 0;
static volatile byte next = bits[0];

PERIODIC_ISR {
    pwm(next);
    idx = (idx + 1) % sizeof(bits);
    next = bits[idx];
}

void setup() {
    initPWM();
    initPeriodicISR();
}

void loop() {
    // pwm(0)
    // delay(1);
    // pwm(1)
    // delay(1);
}