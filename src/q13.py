# stripped down version but gets the answer

class test():

    def fact(self, num):
        fact = 1
        for n in range(1, num+1):
            fact *= n
        return fact

    def expoApprox(self, x):
        n = 0
        expo = 0
        check = ((x ** n) / self.fact(n))
        count = 1

        while check >= 0.01:
            expo = expo + ((x**n)/self.fact(n))

            n = n + 1
            check = ((x ** n) / self.fact(n))
            count += 1

        return round(expo + check, 3)


testObj = test()
print("expoApprox(1) = " + str(testObj.expoApprox(1)))
print("expoApprox(4) = " + str(testObj.expoApprox(4)))
