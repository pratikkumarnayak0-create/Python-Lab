class Employee:
    def __init__(self, empid, name, basicpay, ta, da):
        
        self.empid = empid
        self.name = name
        self.basicpay = basicpay
        self.ta = ta
        self.da = da
        self.gross_pay = 0

    def calc(self):
        self.gross_pay = self.basicpay + (0.10 * self.ta) + (0.40 * self.da)

    
    def disp(self):
        print("Employee Details")
        print("------------------------")
        print("Employee ID :", self.empid)
        print("Name        :", self.name)
        print("Basic Pay   :", self.basicpay)                                                               
        print("TA          :", self.ta)
        print("DA          :", self.da)
        print("Gross Pay   :", self.gross_pay)


emp1 = Employee(209, "Pratik", 30000, 5000, 8000)

emp1.calc()

emp1.disp()