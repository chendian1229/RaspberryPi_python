#include <math.h>
#include <stdio.h>
#include "PID.h"

float PID(parameter K )
{
	float s;
	s=K.P+K.I+K.D;
	printf("%f\n",s);
	return s;
}

