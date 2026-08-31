class phone()
    def set_color(self,color):
        self.color=color
    def set_price(self,price):
        self.price=price
    def show_color(self):
        return self.color
    def show_price(self):
        return self.price
    def play(self):
        print("i am playing game")
    def reply(self):
        print("hi daa mwonu")
phone1 = phone()
phone1.set_color("Black")
phone1.set_price("200000")
print(phone1.show_color())
print(phone1.show_price())
phone1.play()
phone1.reply()
                                                    
