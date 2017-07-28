#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "PID.h"

double PID(parameter K )
{
	double s;
	s=K.P+K.I+K.D;
	printf("%0.2f\n",s);
	return s;
}

