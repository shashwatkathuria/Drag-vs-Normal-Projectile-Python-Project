# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 20:53:22 2018

@author: Shashwat Kathuria
"""
import math
import pylab as plt


def main():
          flag=True
          xaxis=[]
          yaxis=[]
          dragRange=0.0
          normalRange=0.0
          print("The following program illustrates the trajectory followed by a drag projectile")
          print("and normal projectile (when coefficient of restitution,drag coefficients,etc values are provided)")
          print("and the compares the two trajectories assuming the particle to be a point particle.")
          print()
          while flag:
              theta=float(input("Enter the initial angle(in degrees):  "))
              if theta>0 and theta<90:
                  flag=False
              elif flag:
                  print("Please enter a valid value of theta(between 0 and 90)")
          v=float(input("Enter the initial velocity(in m/s):  "))
          flag=True
          while flag:
            e=float(input("Enter the value of the coefficient of restitution:  "))
            if e>0 and e<1:
                flag=False
            elif flag:
                print("Please enter a valid value of e (between 0 and 1).")
          flag=True
          while flag:
            k=float(input("Enter the value of the drag coefficient(in Ns/m):  "))
            if k>0 and k<1:
                flag=False
            elif flag:
                print("Please enter a valid value of k(bigger than 0 and less than 1:to avoid erroneous output).")
    
          flag=True
          while flag:  
            m=float(input("Enter the value of mass of projectile(in kgs):  "))
            if m>0:
                flag=False
            elif flag:
                print("Please enter a valid value of m (bigger than 0).")
          vy=v*(math.sin((theta*math.pi)/180))
          vx=v*(math.cos((theta*math.pi)/180))
          (xaxis,yaxis,normalRange)=normalProjectile(vy,vx,e)
          normalMaxHeight=max(yaxis)
          plotNormalProjectile(xaxis,yaxis)
          xaxis=[]
          yaxis=[]
          (xaxis,yaxis,dragRange)=dragProjectile(vy,vx,e,k,m)
          dragMaxHeight=max(yaxis)
          plotDragProjectile(xaxis,yaxis)
          print()
          print()
          print("INITIAL VALUES:")
          print("Velocity                  :{}m/s".format(round(v,3)))
          print("Velocity(along x axis)    :{}m/s".format(round(vx,3)))
          print("Velocity(along y axis)    :{}m/s".format(round(vy,3)))
          print("Coefficient Of Restitution:{}".format(e))
          print("Mass of particle          :{}kg".format(m))
          print("Drag Coefficient          :{}Ns/m".format(k))
          print()
          print()
          print("RESULT:")
          print("Range(Normal Projectile)          :{}m".format(round(normalRange,3)))
          print("Range(Drag Projectile)            :{}m".format(round(dragRange,3)))
          print("Difference between Ranges         :{}m ".format(round(normalRange-dragRange,3)))
          print("Maximum Height(Normal Projectile) :{}m".format(round(normalMaxHeight,3)))
          print("Maximum Height(Drag Projectile)   :{}m".format(round(dragMaxHeight,3)))
          print("Difference between Maximum Heights:{}m".format(round(normalMaxHeight-dragMaxHeight,3)))
          
          
def plotNormalProjectile(d1,d2):
             '''
               This function takes in two lists in which the x values and the
               corresponding y values are stored and then displays them separately 
               and also displays their comparison with the trajectory of the normal projectile.
               
             '''
             plt.figure("Normal Projectile")
             plt.title("NORMAL PROJECTILE")
             plt.ylabel("Height(in metres)")
             plt.xlabel("Distance Travelled(in metres)")
             plt.plot(d1,d2)
             plt.figure("Comparison")
             plt.title("COMPARISON OF BOTH THE PROJECTILES")
             plt.plot(d1,d2)
             
             
def plotDragProjectile(d1,d2):
             '''
               This function takes in two lists in which the x values and the
               corresponding y values are stored and then displays them separately 
               and also displays their comparison with the trajectory of the normal projectile.
               
             '''
             plt.figure("Drag Projectile")
             plt.title("DRAG PROJECTILE")
             plt.ylabel("Height(in metres)")
             plt.xlabel("Distance Travelled(in metres)")
             plt.plot(d1,d2) 
             plt.figure("Comparison")
             plt.title("COMPARISON OF BOTH THE PROJECTILES")
             plt.ylabel("Height(in metres)")
             plt.xlabel("Distance Travelled(in metres)")
             plt.plot(d1,d2)
  
    
    
def normalProjectile(vy,vx,e):
             '''
               This function takes in the values of the vertical and horizontal 
               components of the velocity alongwith the value of the coefficient of
               restitution and then computes the x and corresponding y values and stores them 
               in separate lists until the trajectory tends to be very close to the ground.
               
             '''
             y=0.0
             x=0.0
             X=0.0
             xaxis=[]
             yaxis=[]
             while vy>0.001 and e<1:
               T=(2*vy)/9.8
               t1=T/10000
               for i in range(10000):
                  y=vy*i*t1-((0.5)*(9.8)*((i*t1)**2))
                  x=(vx*i*t1)+X
                  xaxis.append(x)
                  yaxis.append(y)
               X+=(2*vy*vx)/9.8
               vy=e*vy
             return (xaxis,yaxis,X)



def dragProjectile(vy,vx,e,k,m):
              '''
               This function takes in the values of the vertical and horizontal 
               components of the velocity alongwith the values of the coefficient of
               restitution,drag coefficient and mass of the particle and then computes 
               the x and corresponding y values and stores them in separate lists until the 
               trajectory tends to be very close to the ground.
               
              '''
              y=0.0
              x=0.0
              X=0.0
              xaxis=[]
              yaxis=[]
              yo=[]
              n=1
              while vy>0.01 and vx>0.01 and e<=1:
                  i=1
                  z=X
                  yo=[]
                  while True:
                      dt=0.001
                      y=((m*vy)/k)*(1-math.exp(-((k/m)*(i*dt))))-((m*9.8)/k)*((i*dt)-(m/k)*(1-math.exp(-((k/m)*(i*dt)))))
                      x=((m*vx)/k)*(1-math.exp(-((k*(i*dt))/m)))+X
                      xaxis.append(x)
                      yaxis.append(y)
                      yo.append(y)
                      i+=1
                      if max(yo)<0.005 or (y<0.005 and i>100):
                          t=i*dt
                          X+=x
                          break
                  n+=1
                  vy=math.fabs(e*(((-((m*9.8)/k))*(1-math.exp(-((k/m)*t))))+vy*math.exp(-((k/m)*t))))
                  vx=vx*math.exp(-((k/m)*t))
                  if n>=2:
                      X-=z
                      z=X
                      dragRange=x
              return (xaxis,yaxis,dragRange)
     

if __name__=="__main__":
    main() 




