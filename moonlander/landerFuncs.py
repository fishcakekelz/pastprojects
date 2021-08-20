# Project 1 - Moonlander
#
# Author: Kelly Mok 
# Instructor: Mork 

def showWelcome():
   print("\nWelcome aboard the Lunar Module Flight Simulator\n\n   To begin you must specify the LM's initial altitude\n   and fuel level.  To simulate the actual LM use\n   values of 1300 meters and 500 liters, respectively.\n\n   Good luck and may the force be with you!\n")

def getFuel():  
   currentFuel = int(input('Enter the initial amount of fuel on board the LM (in liters): '))
   while currentFuel <= 0:
     print("ERROR: Amount of fuel must be positive, please try again")
     currentFuel = int(input('Enter the initial amount of fuel on board the LM (in liters): '))
   return currentFuel

def getAltitude():
   z = int(input('Enter the initial altitude of the LM (in meters): '))
   while z<1 or z>9999: 
     print('ERROR: Altitude must be between 1 and 9999, inclusive, please try again')
     z = int(input('Enter the initial altitude of the LM (in meters): '))
   return z

def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   print('Elapsed Time: %4.0d' % elapsedTime + ' s')
   print('        Fuel: %4.0d' % fuelAmount + ' l')
   print('        Rate: %4.0d' % fuelRate + ' l/s')
   print('    Altitude: %6.2f' % altitude + ' m')
   print('    Velocity:  %6.2f' % velocity + ' m/s')
   return 

def getFuelRate(currentFuel):
   fuelBaby = int(input('Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): '))
   while fuelBaby > 9 or fuelBaby < 0:
     print('ERROR: Fuel rate must be between 0 and 9, inclusive')
     fuelBaby = int(input('Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): '))
   return min(fuelBaby, currentFuel)

def updateAcceleration(gravity, fuelRate):
   acceleration = gravity * ((fuelRate / 5) - 1)
   return acceleration
	
def updateAltitude(altitude, velocity, acceleration):
   alt = altitude + velocity + (acceleration / 2)
   return alt 

def updateVelocity(velocity, acceleration):
   vel = velocity + acceleration
   return vel 

def updateFuel(fuel, fuelRate):
   fuelNow = fuel - fuelRate
   return fuelNow

def displayLMLandingStatus(velocity):
   if velocity >= -1 and velocity <= 0: 
     print('Status at landing - The eagle has landed!')
   elif velocity < -1 and velocity > -10: 
     print('Status at landing - Enjoy your oxygen while it lasts!') 
   elif velocity <= -10: 
     print('Status at landing - Ouch - that hurt!') 

