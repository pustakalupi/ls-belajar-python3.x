'''
done
'''
class Pesawat:
    healthy = 10
    name = ""

    def hit(self):
        self.healthy -= 1
    
    def isAlive(self):
        if self.healthy <= 0:
            print("explodes")
        else:
            print(self.name, ": ", self.healthy, " remaining")

psw1 = Pesawat() #psw1 adalah object atau instance dari class Pesawat
psw1.name = "Pesawat1"

psw2 = Pesawat() #psw2 adalah object atau instance lain dari class Pesawat
psw2.name = "Pesawat2"

psw1.hit()

psw1.isAlive()
psw2.isAlive()