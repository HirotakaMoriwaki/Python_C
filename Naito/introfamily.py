import intro

class IntroFam(intro.Intro):
    def __init__(self,name,age,cat):
        super().__init__(name,age)
        self.cat=cat

    #def __init__(self,cat):
    #    self.cat=cat

    def cat_out(self):
        text = "飼い猫の名前は、"+self.cat+"です"
        return text