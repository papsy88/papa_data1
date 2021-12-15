hrs=input('Enter hours')
rate=input('Enter rate')
#floated variables
fh=float(hrs)
fr=float(rate)
#pay function where a=fr and b=fh
def computepay(a,b):
    if b>40:
        gross=(a*(b-5))+(a*1.5*(b-40))
    return gross
Grosspay=computepay(fr,fh)
print('Pay',Grosspay)
