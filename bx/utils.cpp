#include "Arduino.h"
#include "utils.h"

#define CLOCK_HZ 16000000.0

uint16_t frequencyToTOP(uint16_t freq, uint16_t prescalar) {
    return CLOCK_HZ / prescalar / freq - 1;
}
