import socket

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        age = currentYear - self.year
        print("Your age is " + str(age))

    def listAnniversaries(self):
        currentYear = 2024
        anniversaries = []
        birthYear = self.year
        decade = 0
        while birthYear < currentYear:
            birthYear += 10
            decade += 10
            if birthYear <= currentYear:
                anniversaries.append(decade)
            
        
        return anniversaries
       
    def modifyYear(self, n):
        intToString = str(self.year)
        firstTwo = (intToString[0] + intToString[1]) * n
        oddInts = []

        for index in range(1, len(intToString), 2):
            if index % 2 != 0:
                value = intToString[index] 
                oddInts.append(value )                               
        newString = "".join(oddInts)
        
        return firstTwo + str(int(newString) * int(n))
    
    @staticmethod
    def checkGoodString(string):
        if len(string) >= 9 and string[0].islower():
            count = 0
            for i in string:
                if i.isdigit():
                    count += 1

            return count == 1

        return False
    
    @staticmethod
    def connectTcp(host, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
                return True
        except socket.error as err:
            return False

