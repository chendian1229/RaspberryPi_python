#ifndef __PID_H__
#define __PID_H__

typedef struct parameter
{
	double P;
	double I;
	double D;
}parameter;

double PID(parameter K);

#endif