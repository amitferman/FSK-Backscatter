#ifndef _PWM_H_
#define _PWM_H_

#define TOP0 3 // 2000 kHz
#define TOP1 2 // 2667 kHz

#define pwm(x) (x == 0 ? (TCNT4 = 0; OCR4A = TOP0;) : (TCNT4 = 0; OCR4A = TOP1;))

void initPWM();

#endif // _PWM_H_
