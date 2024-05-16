#Imports
import EGN_EN
from random import*
from math import *
#!This is where the calculations happen, UI is in EGN_EN and EGN_BG depending on language
#^Utility

#* Setting local variables to the values of variables in EGN_EN, done for ease of coding
Year = EGN_EN.year
Month = EGN_EN.month
Day = EGN_EN.day
Male = EGN_EN.Male
Female = EGN_EN.Female
Province = EGN_EN.Province
#?Random = EGN_EN.Random

#!Debug print statements
print(f"year variable from EGN_EN is {Year}")
print(f"month variable from EGN_EN is {Month}")
print(f"day variable from EGN_EN is {Day}")
print(f"Male variable from EGN_EN is {Male}")
print(f"Female variable from EGN_EN is {Female}")
print(f"Province variable from EGN_EN is {Province}")
#?print(f"Random variable from EGN_EN is {Random}")

#*Additional Variables
EGN = 0
LowerBound = 0
HigherBound = 0

#&Calculating the first 6 numbers
#^Calculating the year

#*Taking off the first two numbers
ShortYear = Year[2:]

#*Converting the year to a number
Year = int(Year)

#!Debug print statement
print(f"The shortened Year is now {ShortYear}")

#^Calculating the Month
#*Converting into Int
Month = int(Month)

#*Changing the value depending on the provided year data
if Year > 2000 and Year < 2100:
    Month = Month + 40
elif Year < 1900:
    Month = Month + 20
else:
    Month = Month

#^Converting back to string for concatenation later
Month = str(Month)
ShortYear = str(ShortYear)

#^Concatenating the first 6 numbers
EGN = ShortYear + Month + EGN_EN.day
#!Debug print statement
print(f"The EGN is now {EGN}")

#& Calculating the next 3 numbers
#^ Converting the province to a Int 
#* setting variable
ProvinceInt = 0
#*Setting the ProvinceInt to values respective to the province numbers
if Province == "Blagoevgrad" or "blagoevgrad" or "Благоевград" or "благоевград":
    ProvinceInt = 1
elif Province == "Burgas" or "burgas" or "Бургас" or "бургас":
    ProvinceInt = 2
elif Province == "Varna" or "varna" or "Варна" or "varna":
    ProvinceInt = 3
elif Province == "Veliko Tarnovo" or "Veliko tarnovo" or "veliko tarnovo" or "Велико Търново" or "Велико търново" or "велико търново":
    ProvinceInt = 4
elif Province == "Vidin" or "vidin" or "Видин" or "видин":
    ProvinceInt = 5
elif Province == "Vraca" or "vraca" or "Враца" or "враца":
    ProvinceInt = 6
elif Province == "Gabrovo" or "gabrovo" or "Габрово" or "габрово":
    ProvinceInt = 7
elif Province == "Kardzhali" or "kardzhali" or "Кърджали" or "кърджали":
    ProvinceInt = 8
elif Province == "Kyustendil" or "kyustendil" or "Кюстендил" or "кюстендил"
    ProvinceInt = 9
elif Province == "Lovech" or "lovech" or "Ловеч" or "ловеч":
    ProvinceInt = 10
elif Province == "Montana" or "montana" or "Монтана" or "монтана":
    ProvinceInt = 11
elif Province == "Pazardzhik" or "pazardzhik" or "Пазарджик" or "пазарджик":
    ProvinceInt = 12
elif Province == "Pernik" or "pernik" or "Перник" or "перник":
    ProvinceInt = 13
elif Province == "Pleven" or "pleven" or "Плевен" or "плевен":
    ProvinceInt = 14
elif Province == "Plovdiv" or "plovdiv" or "Пловдив" or "пловдив":
    ProvinceInt = 15
elif Province == "Razgrad" or "razgrad" or "Разград" or "разград":
    ProvinceInt = 16
elif Province == "Ruse" or "ruse" or "Русе" or "русе":
    ProvinceInt = 17
elif Province == "Silistra" or "silistra" or "Ruse" or "ruse":
    ProvinceInt = 18












#!Debug print command
print(f"Province int is {ProvinceInt}")

