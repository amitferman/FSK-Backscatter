#include "Arduino.h"
#include "pwm.h"
#include "interrupt.h"

static volatile uint16_t idx = 0;
static const byte bits[] = {0,1,0,1};

PERIODIC_ISR {
    pwm(idx);
    idx = (idx + 1) % sizeof(bits);
}

void setup() {
    initPWM();
    schedulePeriodicISR(BIT_RATE);
}

void loop() {

}