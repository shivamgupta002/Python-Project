import phonenumbers
from phonenumbers import timezone,geocoder,carrier

# Taking Phone number from users
number=input("Enter your Phone Number with Country Code: ")

# Getting Phone Number
phone=phonenumbers.parse(number)

#getting TimeZone of PhoneNumber
time=timezone.time_zones_for_number(phone)

# Getting Sim Name
car=carrier.name_for_number(phone,'en')

# Getting Region
reg=geocoder.description_for_number(phone,'en')

print(phone)
print(time)
print(car)
print(reg)