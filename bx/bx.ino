#include "Arduino.h"
#include "pwm.h"
#include "interrupt.h"

static volatile uint16_t idx = 0;
static const byte bits[] = {0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0};

PERIODIC_ISR {
    // pwm(idx);
    // idx = (idx + 1) % sizeof(bits);
}

void setup() {
    initPWM();
    // initPeriodicISR();
}

void loop() {
    pwm(0)
    delay(100);
    pwm(1)
    delay(100);
}