amt=int(raw_input("Enter Your Amount:::"))
totamt=0
if(amt%10!=0):
    print "Invalid Amount"
else:
    if(amt>=1000):
        res=amt/1000;
        temp=res*1000;
        amt=amt-temp;
        totamt=totamt+temp
        print "1000 * ",res," = ",temp
    if(amt>=500):
        res=amt/500
        temp=res*500;
        amt=amt-temp;
        totamt=totamt+temp
        print "500  * ",res," = ",temp
    if(amt>=100):
        res=amt/100
        temp=res*100
        amt=amt-temp
        totamt=totamt+temp
        print "100  * ",res," = ",temp
    if(amt>=50):
        res=amt/50
        temp=res*50
        amt=amt-temp
        totamt=totamt+temp
        print "50   * ",res," = ",temp
    if(amt>=20):
        res=amt/20
        temp=res*20
        amt=amt-temp
        totamt=totamt+temp
        print "20   * ",res," = ",temp
    if(amt>=10):
        res=amt/10
        temp=res*10
        amt=amt-temp
        totamt=totamt+temp
        print "10   * ",res," = ",temp
    print "=====================\nTotal Amount :: ",totamt
