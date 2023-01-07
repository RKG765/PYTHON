seats = [1,2,3,4,5,6,7,8,9,10]
import random 

class Train:
    def __init__(self,name,date,fare,status):
        self.name = name
        self.date = date
        self.fare = fare
        self.status = status
    def getInfo(self):
        print(f"your train is {self.name}\n and it's fare is Rs {self.fare}")
        print(f'your date of travelling is {self.date}')
    def getStatus(self):
        print(f'Numbber of seats avaliable are {seats}')
    def booking(self):
        if 'seats > 0':
            print('your ticket has been booked \n Have a great journey')
            seatno = random.randint(1,10)
            print(f'Your seat nnumber is {seatno}')
            getStatus = seats.remove(seatno)
        else:
            print('Sorry,there are no seats avaliable.Kindly try tatkal')
    def canceling(self,seatno):
        if seatno not in seats:
            print('Sorry you are inputing some wrong details')
        elif seatno in seats:
            print(f'Your train{self.train} {seatno} ticket has been cancelled')
            self.status = seats.append(seatno)
            print(Train.getStatus(self))

bihar = Train('bihar/exp/1103' , '23.8.2021', '780 Non-A.C', seats)
bihar.getInfo()
bihar.getStatus()
bihar.booking()
bihar.getStatus()
bihar.canceling(4)

        
        