class test():
    def fact(self,num):
        fact = 1
        for n in range(1,num+1):
            fact *= n
        return fact

    def expoApprox(self, x):
        n = 0
        expo = 0
        check = ((x ** n) / self.fact(n))
        count = 1

        while check >= 0.01:
            n = n + 1
            check = ((x ** n) / self.fact(n))
            count += 1
        print("Count: {}".format(count))

        for n in range(count):
            expo = expo + ((x**n)/self.fact(n))

        return round(expo, 3)


if __name__ == '__main__':
    testObj = test()
    running = True

    while running:
        print("*******************************START********************************")
        testNum = int(input("Enter a number to calculate expo: "))
        print("Expo of {} is {}".format(testNum, testObj.expoApprox(testNum)))
        print("********************************END*********************************")

        checkMore = input("Do you want to check more number(y/n):\n")

        if checkMore.upper() != "Y" and checkMore.upper() != "YES":
            running = False

