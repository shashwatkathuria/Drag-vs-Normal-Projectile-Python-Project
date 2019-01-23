# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 20:53:22 2018

@author: Shashwat Kathuria
"""
import math
import pylab as plt


def main():

        # Initializing the coordinates and ranges to 0 and empty list respectively
        xAxisCoordinates = []
        yAxisCoordinates = []
        dragRange = 0.0
        normalRange = 0.0

        # Printing introduction to the user alongwith certain assumptions
        print("The following program illustrates the trajectory followed by a drag projectile")
        print("and normal projectile (when coefficient of restitution,drag coefficients,etc values are provided)")
        print("and the compares the two trajectories assuming the particle to be a point particle.")
        print("\n")

        # Prompting user for a value of angle between 0 and 90
        flag = True
        while flag:
            theta = float(input("Enter the initial angle(in degrees):  "))
            if theta > 0 and theta < 90:
                flag = False
            elif flag:
                print("Please enter a valid value of theta(between 0 and 90)")

        # Prompting user for value of initial velocity of particle
        initialVelocity = float( input("Enter the initial velocity(in m/s):  ") )

        # Prompting user for the value of coefficient of restitution between 0 and 1
        flag = True
        while flag:
            coefficientOfRestitution = float(input("Enter the value of the coefficient of restitution:  "))
            if coefficientOfRestitution > 0 and coefficientOfRestitution < 1:
                flag = False
            elif flag:
                print("Please enter a valid value of coefficient of restitution (between 0 and 1).")

        # Prompting user for the value of drag coefficient between 0 and 1
        flag = True
        while flag:
            dragCoefficient = float( input("Enter the value of the drag coefficient(in Ns/m):  ") )
            if dragCoefficient > 0 and dragCoefficient < 1:
                flag = False
            elif flag:
                print("Please enter a valid value of drag coefficient(bigger than 0 and less than 1:to avoid erroneous output).")

        # Prompting user for the value of mass of particle
        flag = True
        while flag:
            massOfParticle = float( input("Enter the value of mass of projectile(in kgs):  ") )
            if massOfParticle > 0:
                flag = False
            elif flag:
                print("Please enter a valid value of mass of particle (bigger than 0).")


        # Computing and storing x and y components of initial velocity
        yInitialVelocityComponent = initialVelocity * (math.sin( (theta * math.pi) / 180) )
        xInitialVelocityComponent = initialVelocity * (math.cos( (theta * math.pi) / 180) )

        # Calling normal projectile function and storing respective values
        (xAxisCoordinates, yAxisCoordinates, normalRange) = normalProjectile(yInitialVelocityComponent, xInitialVelocityComponent, coefficientOfRestitution)

        # Computing maximum height of the normal projectile
        normalMaxHeight = max(yAxisCoordinates)

        # Plotting the normal projectile by calling appropriate function
        plotNormalProjectile(xAxisCoordinates, yAxisCoordinates)

        # Setting coordinate lists to empty lists again to
        # compute the same for drag projectile
        xAxisCoordinates = []
        yAxisCoordinates = []

        # Calling drag projectile function and storing respective values
        (xAxisCoordinates, yAxisCoordinates, dragRange) = dragProjectile(yInitialVelocityComponent, xInitialVelocityComponent, coefficientOfRestitution, dragCoefficient, massOfParticle)

        # Computing maximum height of the drag projectile
        dragMaxHeight = max(yAxisCoordinates)

        # Plotting the drag projectile by calling appropriate function
        plotDragProjectile(xAxisCoordinates, yAxisCoordinates)

        # Printing the results
        print("\n\n")
        print("INITIAL VALUES:")
        print("Velocity                  :{}m/s".format( round(initialVelocity, 3) ))
        print("Velocity(along x axis)    :{}m/s".format( round(xInitialVelocityComponent, 3) ))
        print("Velocity(along y axis)    :{}m/s".format( round(yInitialVelocityComponent, 3) ))
        print("Coefficient Of Restitution:{}".format(coefficientOfRestitution))
        print("Mass of particle          :{}kg".format(massOfParticle))
        print("Drag Coefficient          :{}Ns/m".format(dragCoefficient))
        print("\n\n")
        print("RESULT:")
        print("Range(Normal Projectile)          :{}m".format( round(normalRange, 3) ))
        print("Range(Drag Projectile)            :{}m".format( round(dragRange, 3) ))
        print("Difference between Ranges         :{}m".format( round(normalRange - dragRange, 3) ))
        print("Maximum Height(Normal Projectile) :{}m".format( round(normalMaxHeight, 3) ))
        print("Maximum Height(Drag Projectile)   :{}m".format( round(dragMaxHeight, 3) ))
        print("Difference between Maximum Heights:{}m".format( round(normalMaxHeight - dragMaxHeight,3) ))

        # Showing the graphs
        showGraph()

def showGraph():
        """
            Function to show the graphs/plots.
        """

        plt.show()

def plotNormalProjectile(xAxisCoordinates, yAxisCoordinates):
             '''
               This function takes in two lists in which the x values and the
               corresponding y values are stored and then displays them separately
               and also displays their comparison with the trajectory of the normal projectile.

             '''

             # Naming figure, giving title and giving x and y axis labels
             plt.figure("Normal Projectile")
             plt.title("NORMAL PROJECTILE")
             plt.ylabel("Height(in metres)")
             plt.xlabel("Distance Travelled(in metres)")

             # Passing in the coordinates values of the trajectory of projectile
             plt.plot(xAxisCoordinates, yAxisCoordinates)

             # Naming new figure and plotting same values for comparison
             plt.figure("Comparison")
             plt.title("COMPARISON OF BOTH THE PROJECTILES")
             plt.plot(xAxisCoordinates, yAxisCoordinates)


def plotDragProjectile(xAxisCoordinates, yAxisCoordinates):
             '''
               This function takes in two lists in which the x values and the
               corresponding y values are stored and then displays them separately
               and also displays their comparison with the trajectory of the normal projectile.

             '''

             # Naming figure, giving title and giving x and y axis labels
             plt.figure("Drag Projectile")
             plt.title("DRAG PROJECTILE")
             plt.ylabel("Height(in metres)")
             plt.xlabel("Distance Travelled(in metres)")

             # Passing in the coordinates values of the trajectory of projectile
             plt.plot(xAxisCoordinates, yAxisCoordinates)

             # Naming new figure, giving it x and y labels and plotting same values for comparison
             plt.figure("Comparison")
             plt.title("COMPARISON OF BOTH THE PROJECTILES")
             plt.ylabel("Height(in metres)")
             plt.xlabel("Distance Travelled(in metres)")
             plt.plot(xAxisCoordinates, yAxisCoordinates)



def normalProjectile(yInitialVelocityComponent, xInitialVelocityComponent, coefficientOfRestitution):
            '''
               This function takes in the values of the vertical and horizontal
               components of the velocity alongwith the value of the coefficient of
               restitution and then computes the x and corresponding y values and stores them
               in separate lists until the trajectory tends to be very close to the ground.

            '''

            # Initializing values required to zeros and empty lists
            yInstantaneous = 0.0
            xInstantaneous = 0.0
            Range = 0.0
            xAxisCoordinates = []
            yAxisCoordinates = []
            originShift = 0.0

            # Running loop and storing trajectory coordinates until negligible

            while yInitialVelocityComponent > 0.001 and coefficientOfRestitution < 1:

                # Calculating the total time taken in the current bounce
                totalTimeOfOneBounce = ( 2 * yInitialVelocityComponent ) / 9.8

                # Setting time interval (dt) to be small enough
                timeInterval = totalTimeOfOneBounce / 10000

                # Running loop and calculating values for all time intervals of current bounce
                for i in range(10000):

                    # Calculating y value according to formula
                    yInstantaneous = yInitialVelocityComponent * i * timeInterval - ( (0.5) * (9.8) * ( (i * timeInterval) ** 2 ) )

                    # Calculating y value according to formula
                    xInstantaneous = ( xInitialVelocityComponent * i * timeInterval ) + originShift

                    # Appending coordinates to respective lists
                    xAxisCoordinates.append(xInstantaneous)
                    yAxisCoordinates.append(yInstantaneous)

                # Computing origin shift for next iteration, which is the range obtained till now
                originShift = xAxisCoordinates[-1]

                # Computing reduced y velocity component for next bounce
                yInitialVelocityComponent = coefficientOfRestitution * yInitialVelocityComponent

            # Range is the last (biggest) value of the x axis coordinates obtained
            Range = xAxisCoordinates[-1]
            # Returning values
            return (xAxisCoordinates, yAxisCoordinates, Range)



def dragProjectile(yInitialVelocityComponent, xInitialVelocityComponent, coefficientOfRestitution, dragCoefficient, massOfParticle):
            '''
               This function takes in the values of the vertical and horizontal
               components of the velocity alongwith the values of the coefficient of
               restitution,drag coefficient and mass of the particle and then computes
               the x and corresponding y values and stores them in separate lists until the
               trajectory tends to be very close to the ground.
            '''

            # Initializing values required to zeros and empty lists
            yInstantaneous = 0.0
            xInstantaneous = 0.0
            Range = 0.0
            xAxisCoordinates = []
            yAxisCoordinates = []
            currentBounceYAxisCoordinates = []

            # n = 1
            while yInitialVelocityComponent > 0.01 and xInitialVelocityComponent > 0.01 and coefficientOfRestitution <= 1:

                # Time interval number
                i = 1

                # Setting origin shift to be range
                originShift = Range

                # Setting y coordinates of current bouonce to be an empty list
                # To be used for terminating program when height obtained is negligible
                currentBounceYAxisCoordinates = []

                # Running loop and computing and storing information required
                while True:

                    # Setting time interval (dt) to be 0.001 seconds
                    dt = 0.001

                    # Calculating y value according to formula
                    yInstantaneous = ( (massOfParticle * yInitialVelocityComponent) / dragCoefficient ) * ( 1 - math.exp( - ( (dragCoefficient / massOfParticle) * (i * dt) ) ) ) - ( ( massOfParticle * 9.8) / dragCoefficient ) * ( (i * dt) - ( massOfParticle / dragCoefficient ) * ( 1 - math.exp( - ( ( dragCoefficient / massOfParticle ) * (i * dt ) ) ) ) )

                    # Calculating y value according to formula
                    xInstantaneous = ( (massOfParticle*xInitialVelocityComponent) / dragCoefficient) * (1 - math.exp( - ( (dragCoefficient * (i * dt)) / massOfParticle ) ) ) + Range

                    # Appending coordinates to respective lists
                    xAxisCoordinates.append(xInstantaneous)
                    yAxisCoordinates.append(yInstantaneous)
                    currentBounceYAxisCoordinates.append(yInstantaneous)

                    # Incrementing time interval to next time interval
                    i += 1

                    # Terminating if height obtained is negligible but only enough bounces
                    if max(currentBounceYAxisCoordinates) < 0.005 or (yInstantaneous < 0.005 and i > 100):
                        t = i * dt
                        Range += xInstantaneous
                        break

                # Computing modified x and y axis velocity components according to formulas
                yInitialVelocityComponent = math.fabs(coefficientOfRestitution * (   (( - ( (massOfParticle * 9.8) / dragCoefficient ) ) * (1 - math.exp( - ( (dragCoefficient / massOfParticle) * t ) ) )) + yInitialVelocityComponent * math.exp( - ( (dragCoefficient / massOfParticle) * t ) ) )   )
                xInitialVelocityComponent = xInitialVelocityComponent * math.exp( -( (dragCoefficient / massOfParticle) * t) )

                # Updating origin shift
                Range -= originShift
                originShift = Range

            # Range is the last (biggest) value of the x axis coordinates obtained
            dragRange = xAxisCoordinates[-1]

            # Returning values
            return (xAxisCoordinates, yAxisCoordinates, dragRange)


if __name__ == "__main__":
    main()
