import introduce

class IntroFam(introduce.Intro):
    def __init__(self,name, age, cat_name):
        super().__init__(name,age) # introduceの中の関数を指定
        # self.name = name これを追記するとオーバーライド
        # self.age = age
        self.cat_name = cat_name

    def cat_name_out(self):
        nametxt = "飼い猫の名前は、" + self.cat_name + "です"
        return nametxt