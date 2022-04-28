from xxlimited import new


class Complex :
    def __init__(self, ComplexRealPart, ComplexImagePart):
        self.real = ComplexRealPart
        self.image = ComplexImagePart 

    def showComplex(self):
        print(self.real, "+", "(",self.image,"i",")")    
    
    def sum(self, newComplex):
        return Complex(  (self.real+newComplex.real) , (self.image+newComplex.image)  ) 

    def sub (self, newComplex):
        return Complex( (self.real - newComplex.real) , (self.image - newComplex.image ) )

    def multiple(self, newComplex): 
        return Complex ( ((self.real*newComplex.real) - (self.image*newComplex.image)) ,
        ((self.real*newComplex.image) + (self.image*newComplex.real)) )


inputNumber = int(input('choose operation:\n1-add two complex number \n2-subtract two complex number \n3-multiple two complex number\n'))

firstComplexRealPart=int(input("enter real part for first complex number\n"))
firstComplexImagePart=int(input("enter image part for first complex number\n"))
secondComplexRealPart=int(input("enter real part for second complex number\n"))
secondComplexImagePart=int(input("enter image part for second complex number\n"))

firstComplexNumber = Complex(firstComplexRealPart,firstComplexImagePart)
secondComplexNumber = Complex(secondComplexRealPart,secondComplexImagePart)

if inputNumber == 1:
    firstComplexNumber.sum(secondComplexNumber).showComplex()
if inputNumber == 2:
    firstComplexNumber.sub(secondComplexNumber).showComplex()
if inputNumber == 3:
    firstComplexNumber.multiple(secondComplexNumber).showComplex()
