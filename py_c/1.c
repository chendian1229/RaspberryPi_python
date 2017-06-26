#include <stdio.h>
#include <stdlib.h>
float foo(float a,float b)
{
	static float s=0;
	printf("you input %.2f and %.2f==%.2f\n",a,b,s);
	s=a+b+s;
	return s;
}