#include <math.h>
#include <stdio.h>
#include "PID.h"

float PID(parameter K )
{
	float s=0;
	s=K.P+K.I+K.D;
	printf("%0.2f\n",s);
	return s;
}

