class Person(object):
    __healthRate=0;
    def __init__(self, full_name,money,sleepmood,healthRate):
        self.full_name = full_name
        self.money = money
        self.sleepmood = sleepmood
        self.setHealthRate(healthRate)
    
    def sleep(self):
        print("sleeping")
        
    def eat(self):
        print("eating")

    def buy(self):
        print("buying")
    def setHealthRate(self,healthRateInput):
        if(healthRateInput>0 and healthRateInput <=100):
            self.healthRate=healthRateInput;
        else:
            print("health must be between 100 and 0 ")
