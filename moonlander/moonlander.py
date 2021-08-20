# Project 1 - Moonlander
#
# Author: Kelly Mok
# Instructor: Mork

from landerFuncs import * 

def main():
   showWelcome()
   altitude = getAltitude()
   fuelAmount = getFuel() 
   
   print('\nLM state at retrorocket cutoff')
   elapsedTime = 0
   fuelRate = 0
   velocity = 0.00
   displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
   print('\n', end="")
   fuelRate = getFuelRate(fuelAmount)
   while altitude > 0:
     elapsedTime += 1
     fuelAmount = updateFuel(fuelAmount, fuelRate)
     gravity = 1.62
     acceleration = updateAcceleration(gravity, fuelRate)
     altitude = updateAltitude(altitude, velocity, acceleration)
     velocity = updateVelocity(velocity, acceleration)
       
     if fuelAmount == 0 and altitude > 0:
       fuelRate = 0 
       print('OUT OF FUEL - Elapsed Time:    %4.0d' %elapsedTime + ' Altitude:  %9.2f' %altitude + ' Velocity: %6.2f' %velocity)
     elif altitude > 0: 
       displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
       print("\n") 
       fuelRate = getFuelRate(fuelAmount)
     if altitude < 0:
        altitude = 0 
        
   print('\nLM state at landing/impact')
   displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
   print('\n', end='')
   displayLMLandingStatus(velocity)


if __name__ == '__main__':
   main()
   
