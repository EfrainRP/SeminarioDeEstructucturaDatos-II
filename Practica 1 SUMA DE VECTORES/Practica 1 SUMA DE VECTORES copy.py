
import math 

class Vector:
    X=0
    Y=0
    angleRad=0

    def __init__ (self,x_,y_):
        self.X=x_
        self.Y=y_
        self.angleRad= math.atan(self.Y/self.X)

    def getX(self):
        return self.X

    def getY(self):
        return self.Y
    
    def getAngleRad(self):
        return self.angleRad

    def setX(self,x_):
        self.X=x_

    def setY(self,y_):
        self.Y=y_

    def setAngleRad(self,a_):
        self.angleRad=a_

    def getMagnitude(self):
        return math.sqrt((self.X**2 + self.Y**2))

    def findLineX(self, h_):
        return h_*math.cos(self.angleRad)

    def findLineY(self, h_):
        return h_*math.sin(self.angleRad)

    def __str__(self):
        return '(' + str(format(self.X,',.2f')) + ', ' + str(format(self.Y,',.2f')) + ')'

    #def toString(self):
        #if self.X < 0:
     #       str = "self.X , s"
      #  return str

print("\t\t\tSUMA DE VECTORES\n")

a = int(input("Introduce un vector:\n"))
b = int(input())
v1=Vector(a,b)

a = int(input("\nIntroduce otro vector:\n"))
b = int(input())
v2=Vector(a,b)

#print(v1.getMagnitude())
#v1.printVector()
#print(v1.findLineX(v1.getMagnitude()))
h1=v1.getMagnitude()
h2=v2.getMagnitude()

xf=v1.findLineX(h1) + v2.findLineX(h2)
yf=v1.findLineY(h1) + v2.findLineY(h2)

vf=Vector(xf,yf)

print("Vector 1:     ", v1)
print("Vector 2:     ",v2)
print("Vector Final: ",vf)

#print("Vector Final     ----->          Magnitud: ",vf.getMagnitude(), \
#"     Dirección: ", math.acos((vf.getX()/vf.getMagnitude())), "radianes")
# #print("grados:", math.acos((vf.getX()/vf.getMagnitude()))*(180/math.pi))

print("\n\nVector Final:\n\t\tMagnitud: ",format(vf.getMagnitude(),'.4f'), 
"   -->    Dirección: ", format(vf.getAngleRad(),'.4f'), "radianes")

print("\t\tMagnitud: ",format(vf.getMagnitude(),'.4f'),
"   -->    Dirección: ", format(vf.getAngleRad()*(180/math.pi),'.4f'), "  grados")


