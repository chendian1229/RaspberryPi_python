import re

n=r'\d{4}\.\d{5}\,N'
e=r'\d{5}\.\d{5}\,E'
a='''$GPGGA,043913.000,3955.21267,N,11932.86772,E,1,05,3.5,30.9,M,,M,,0000*79
$GPGSA,A,3,21,14,32,31,29,,,,,,,,4.3,3.5,2.5*3A
$GPGSV,2,1,07,21,03,106,30,04,00,000,23,14,32,157,33,32,09,154,28*79
$GPGSV,2,2,07,31,52,081,33,29,24,046,23,27,19,184,*4C
$GPRMC,043913.000,A,3955.21267,N,11932.86772,E,0.00,0.00,160417,,,A*69
$GPVTG,0.00,T,,M,0.00,N,0.00,K,A*3D'''

def test(strs):
    strs=strs[0:10]
    strs=float(strs)
    print(strs)
    
m=re.search(n,a)
q=re.search(e,a)
print(m.group(0))
print(q.group(0))

test(m.group(0))
o=q.group(0)[0:11]
print(o)
