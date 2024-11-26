#PRANAV V RAJ-P1-12A-27
import pickle
import os
from datetime import datetime
def valdate(date):
   while True:
    try:
         dateObject=datetime.strptime(date,'%d/%m/%Y')
         print('TRUE')
         break
    except ValueError:
        print('FALSE')
        print('THE FOLLOWING DATA MUST NOT BE INPUTTED!!')
        break
fn='AIRCRAFT.DAT'
fr='FLIGHT.DAT'
fp='PASSENGER.DAT'
menu='''
The program consists of three files:
1.Details of aircraft
2.Details of flight
3.Details of passenger
This program gives information about the records of the passenger,airplane
and the flight.
'''
menu1='''
1.enter the aricraft details as follows:
   • Flight Number
   • Aircraft name
   • Capacity
   • Starting Place
   • Destination Place
   • Arrival Time
   • Departure Time
   • Travel Expenses

2.Print the records

3. Validations
i) Check for sequence of flight number 
ii) Time validations for Deptime and Arrtime
iii) Modification of all the fields will be possible except Fl_No and Aircraft
'''
menu2='''
1.File name should consist of the depature date of the aircraft

2.Enter the follow details
   • Flight Number
   • Seats occupied
   
3.print the records

4. Validation
i) The entries in this file will be done automatically i.e. at the time of reservation Occupied should be incremented and at the 
time of cancellation Occupied should be decremented 
ii) The Occupied field will not exceed the capacity of the aircraft
'''
menu3='''
1.Enter the follow details:
 • Flight Number 
 • PNR Number
 • Seat Number
 • Departure
 • Arrival
 • Name of the passenger
 • Age
 • Sex
 • Address
 • Phone
 • Amount Paid
 Status of reservation (W waiting of C confirmed)

2.Print the output
'''
def aircraft():
   while True:
    print(menu1)
    rn=int(input('enter the option:'))
    if rn==1:
       f=open(fn,'ab')
       F1_NO=str(input('enter flight number:'))
       Aircraft=str(input('enter aircraft name:'))
       Capacity=str(input('enter the capacity:'))
       Splace=str(input('enter the starting point:'))
       Dplace=str(input('enter the destination point:'))
       Dtime=str(input('enter the departure time:'))
       Atime=str(input('enter the arrival time:'))
       Texpense=str(input('enter the travel expense(enter in rupees):'))
       if Dplace!=Splace:
          print('valid input')
       else:
          print('invalid input')
          break
       rec=[F1_NO,Aircraft,Capacity,Splace,Dplace,Dtime,Atime,Texpense]
       pickle.dump(rec,f)
       global b
       b=rec[1]
       f.close()
    elif rn==2:
       f=open(fn,'rb')
       while True:
            print('SAMPLE OUTPUT')
            airlst=[['F1_NO','Aircraft','Capacity','Splace','Dplace','Dtime','Atime','Texpense'],
                    ['HA101','AB2',215,'Delhi','Bangkok','6:00','00:50','22,000'],
                    ['HA102','AB7',295,'Delhi','Singapore','7:15','00:45','23,000']]
            gap=' '*3
            heading=f"{'F1_NO':8s}{gap}{'Aircraft':10s}{gap}{'Capacity':8s}\
            {gap}{'Splace':<8s}{gap}{'Dplace':<10s}{gap}{'Dtime':6s}{gap}{'Atime':6s}{gap}{'Texpense':6s}"
            print('='*100)
            print(heading)
            print('-'*100)
            for data in airlst[1:]:
                rec=f"{data[0]:8s}{gap}{data[1]:10s}{gap}{data[2]:<8d}\
            {gap}{data[3]:8s}{gap}{data[4]:<10s}{gap}{ data[5]:6s}{gap}{data[6]:6s}{gap}{data[7]:7s}"
                print(rec)
            print('-'*100)
            break
       f.close()
    elif rn==3:
         f=open(fn,'rb')
         airlst=[['F1_NO','Aircraft','Capacity','Splace','Dplace','Dtime','Atime','Texpense'],
                    ['HA101','AB2',215,'Delhi','Bangkok','6:00','00:50','22,000'],
                    ['HA102','AB7',295,'Delhi','Singapore','7:15','00:45','23,000']]
         gap=' '*3
         heading=f"{'F1_NO':8s}{gap}{'Aircraft':8s}{gap}{'Capacity':9s}\
            {gap}{'Splace':<8s}{gap}{'Dplace':8s}{gap}{'Dtime':6s}{gap}{'Atime':6s}{gap}{'Texpense':6s}"
         print('='*100)
         print(heading)
         print('-'*100)
         while True:
          try:
                r=pickle.load(f)
                re=f"{r[0]:8s}{gap}{r[1]:10s}{gap}{r[2]:<5s}\
                {gap}{r[3]:8s}{gap}{r[4]:<7s}{gap}{ r[5]:<6s}{gap}{r[6]:<6s}{gap}{r[7]:7s}"
                print(re)
                print('-'*100)
          except EOFError:
                break
         f.close()
    elif rn==4:
      f=open(fn,'rb')
      while True:
         try:
            rec=pickle.load(f)
            lst=[]
            print('The sequence of the flight number:')
            while True:
               lst+=[rec[0]]
               print(lst)
               break
         except EOFError:
            break
      f.close()
    elif rn==5:
       f=open(fn,'rb')
       h=open('EXAMPLE1.dat','wb')
       found=False
       while True:
           try:
            rec=pickle.load(f)
            while True:
                print(rec[5],rec[6])
                if rec[5]>rec[6]:
                   print('invalid data')
                   break
                else:
                   pickle.dump(rec,h)
                   break
           except EOFError:
                f.close()
                h.close()
                break
       if not found:
          print('TIME IS VALID FOR DEPARTURE TIME AND ARRIVAL TIME')
       os.remove(fn)
       os.rename('EXAMPLE1.dat',fn)
    elif rn==6:
        f=open(fn,'rb')
        rn=str(input('enter the field which should be updated:'))
        found=False
        while True:
            try:
             rec=pickle.load(f)
             while True:
               if rec[0]==rn or rec[1]==rn:
                    print('record cannot be inputted')
                    found=True
                    break
               elif  rec[2]==rn or rec[3]==rn or rec[4]==rn or rec[5]==rn or rec[6]==rn or rec[7]==rn:
                    print('Record can be updated')
                    found=True
                    break
            except EOFError:
                pass
        if not found:
           print('record not found')
        f.close()
    elif op==0:
       break
    else:
       print('invalid option')
def flight():
    print(menu2)
    while True:
       ch=int(input('enter the option:'))
       if ch==1:
         while True:
            try:
             fo=open(fr,'ab')
             date=str(input('enter the date(dd/mm/yyyy):'))
             print(valdate(date))
             str1=''.join(date)
             v='F'+str1
             fk=str(input('Enter the flight number:'))
             so=int(input('enter the seats occupied:'))
             st=str(input('Enter the status of ticket:'))
             sr=int(input('enter the seats reserved:'))
             rec=[fk,so,st,sr]
             pickle.dump(rec,fo)
             print('The file name changes to',v)
             break
             fo.close()
             os.rename(fr,v)
            except FileNotFoundError:
              pass
       elif ch==2:
         fo=open(fr,'rb')
         fhtlst=['FL_NO','SEATS OCCUPIED','STATUS','SEATS RESERVED']
         gap=' '*3
         heading=f"{'F1_NO':16s}{gap}{'SEATS OCCUPIED':<8s}{gap}{'STATUS':10s}{gap}{'SEATS RESERVED':5s}"
         print(heading)
         while True:
          try:
                r=pickle.load(fo)
                re=f"{r[0]:15s}{gap}{r[1]:<18d}{gap}{r[2]:10s}{gap}{r[3]:5d}"
                print(re)
          except EOFError:
              break
         fo.close()
       elif ch==3:
          fo=open(fr,'rb')
          c=0
          d=0
          while True:
             try:
                rec=pickle.load(fo)
                if rec[3]=='RESERVED':
                  rec[3]+=1
                  c+=1
                  print('INCREMENTED')
                elif rec[3]=='CANCELLED':
                   rec[3]-=1
                   d+=1
                   print('DECREMENTED')
             except EOFError:
                break
                fo.close()
          print('no of records incremented',c)
          print('no of records decremented',d)
          fo.close()
       elif ch==4:
          fo=open(fr,'rb')
          c=0
          d=0
          while True:
             try:
                rec=pickle.load(fo)
                if rec[1]>=rec[3]:
                   print('Valid capacity')
                   c+=1
                else:
                   d+=1
                   print('Invalid capacity')
             except EOFError:
                break
                fo.close()
          print('records which are valid ',c)
          print('records which are invalid',d)     
          fo.close()
       elif ch==4:
         fo=open(fr,'rb')
         t=0
         while True:
            try:
               rec=pickle.load(fo)
               if rec[3]-rec[1]>=1:
                  print('Seats are available on this flight')
                  t+=rec[3]-rec[1]
               else:
                  print('seats are not available')
            except EOFError:
               pass
               fo.close()
         print('no of seats available',t)
       elif ch==0:
        break
       else:
        print('invalid output')
def passenger():
   print(menu3)
   while True:
       hr=int(input('enter the favourable option:'))
       if hr==1:
           fd=open(fp,'ab')
           F1_No=str(input('Enter the flight number:'))
           PNR=int(input('enter the PNR number:'))
           Seat=int(input('Enter the seat number:'))
           Depart=str(input('enter the depature location:'))
           Arriv=str(input('enter the arrival location:'))
           Name=str(input('enter the  name of the passenger:'))
           Age=int(input('enter the age of the passenger:'))
           Sex=str(input('enter the sex of the passenger:'))
           Address=str(input('enter the address of the passenger:'))
           Phone=int(input('enter the phone number:'))
           Amt=str(input('enter the amount paid:'))
           ST=str(input('enter the status of reservation:'))
           Date=str(input('enter the date(dd/mm/yyyy):'))
           Ticketno=int(input('enter the ticket number:'))
           Aircf=str(input('enter the aircraft:'))
           Deptime=str(input('enter the depature time:'))
           Datiss=str(input('enter the date of issue:'))
           valdate(date)
           str1=''.join(date)
           t='P'+str1
           valdate(datiss)
           str2=''.join(datiss)
           if Depart!=Arriv:
              print('valid input')
           else:
              print('invalid input')
              break
           if Age>0:
              print('valid age')
           else:
              print('invalid age')
              print('reinput the age')
              break
           tun=[F1_No,PNR,Seat,Depart,Arriv,Name,Age,Sex,Address,Phone,Amt,ST,Date,Ticketno,Aircf,
                Deptime,Datiss]
           print(tun)
           pickle.dump(tun,fd)
           print('The file name changes to',t)
           break
           fd.close()
       elif hr==2:
        fd=open(fp,'rb')
        passenger=[['F1_NO','PNR','Seat','Depart','Arriv','Name','Age','Sex','Address','Phone',
                     'Amt','ST','Date','Ticketno','Aircf','Deptime','Datiss']]
        gap=' '*1
        pas='-'*101
        heading=f"{'F1_NO':6s}{gap}{'PNR':8s}{gap}{'Seat':<6s}{gap}{'Depart':15s}{gap}{'Arriv':20s}\
{gap}{'Name':15s}{'Age':4s}{gap}{'Sex':^5s}{gap}{'Address':15s}{pas}{'Phone':<14s}{gap}{'Amt':<8s}\
{gap}{'ST':<4s}{gap}{'Date':9s}{gap}{'Ticketno':10s}{gap}{'Aircf':8s}{gap}{'Deptime':13s}\
{gap}{'Datiss':3s}"
        print('='*100)
        print(heading)
        print('='*100)
        while True:
          try:
                r=pickle.load(fd)
                re=f"{r[0]:4s}{gap}{r[1]:5d}{gap}{r[2]:^7d}{gap}{r[3]:<15s}{gap}{r[4]:10s}{gap}{r[5]:25s}\
{gap}{r[6]:<4d}{gap}{r[7]:^3s}{gap}{r[8]:<16s}{pas}{r[9]:<4d}{gap}{r[10]:>8s}{gap}{r[11]:^7s}\
{gap}{r[12]:2s}{gap}{r[13]:<10d}{gap}{r[14]:8s}{gap}{r[15]:12s}{gap}{r[16]:10s}"
                print(re)
                print('='*100)
          except EOFError:
                break
        break
        fd.close()
       elif hr==10:
        fd=open(fp,'rb')
        h=open('EXAMPLE1.dat','wb')
        found=False
        while True:
           try:
            rec=pickle.load(fd)
            while True:
                if rec[0]=='SNW304':
                    pickle.dump(rec,h)
                else:
                   pass
                   break
           except EOFError:
                fd.close()
                h.close()
                break
        os.remove(fp)
        os.rename('EXAMPLE1.DAT',fp)
       elif hr==3:
          fd=open(fp,'rb')
          print('Reservation slip')
          while True:
             try:
                rec=pickle.load(fd)
                print('                               AIR-GOES INTERNATIONAL AIRLINES           ')
                print('Reservation slip')
                gap=''*20
                print('-'*100)
                print('PNR number:',rec[1],end='                                 ')
                print('Flight number:',rec[0])
                print('Status:',rec[11],end='                                        ')
                print('Seat Number:',rec[2])
                print('Date of journey:',rec[12],end='                        ')  
                print('From:',rec[3])
                print('To:',rec[4],end='                                            ')
                print('Name:',rec[5])
                print('Age:',rec[6],end='                                           ')
                print('Sex:',rec[7])
                print('Contact No:',rec[9],end='                                  ')
                print('Fare:',rec[10])
                print('-'*90)
                break
             except EOFError:
                pass
          fd .close()
       elif hr==4:
            fd=open(fp,'rb')
            print('Passenger Ticket')
            print('-'*90)
            while True:
                try:
                    rec=pickle.load(fd)
                    print('                               AIR-GOES INTERNATIONAL AIRLINES           ')
                    print('Passenger Ticket')
                    print('-'*100)
                    print('Ticket No:',rec[13],end='                              ')
                    print('Date of issue:',rec[1])
                    print('From:',rec[6],end='                                      ')
                    print('To:',rec[2])
                    print('Name:',rec[12],end='                              ')  
                    print('Fare(in rs):',rec[3])
                    print('-'*90)
                except EOFError:
                    break
       elif hr==5:
           fd=open(fp,'rb')
           print('Reservation Chart')
           print('-'*100)
           while True:
               try:
                   r=pickle.load(fd)
                   print('                               AIR-GOES INTERNATIONAL AIRLINES        ')
                   print('Reservation Chart')
                   print('-'*100)
                   print('Flight number:',r[0],end='                ')
                   print('Date of journey:',r[12])
                   print('Aircraft:',r[14],end='                     ')
                   print('Depature Time:',r[15])
                   print('-'*95)
                   passenger=[['Seat No','Name','Age','Destination','PNR','Status']]
                   gap=' '*5
                   heading=f"{'Seat No':3s}{gap}{'Name':15s}{gap}{'Age':3s}{gap}{'Destination':10s}\
               {'PNR':8s}{gap}{'Status':2s}"
                   print(heading)
                   print(''*90)
                   while True:
                    try:
                     re=f"{r[2]:<7d}{gap}{r[5]:15s}{gap}{r[6]:<4d}{gap}{r[4]:15s}{gap}{r[1]:10d}\
         {r[11]:<2s}"
                     print(re)
                     print('-'*100)
                     break
                    except EOFError:
                     break
               except EOFError:
                break
           fd.close()
       elif hr==0:
          break
       else:
          print('invalid option')
while True:
   print(menu)
    op=int(input('enter a valid option:'))
    if op==1:
        print('the details about the aircraft are given as follows:',end=' ')
        aircraft()
    elif op==2:
        print('the details of flight are given as follows:',end=' ')
        flight()
    elif op==3:
        print('the details about the passenegers are given as follows:',end='')
        passenger()
    elif op==0:
        break
    else:
       print('invalid option')
    
