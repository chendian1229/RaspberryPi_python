#ifndef __PID_H__
#define __PID_H__

typedef struct parameter
{
	float P;
	float I;
	float D;
}parameter;

float PID(parameter K);

#endif