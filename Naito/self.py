class Dog:
    def __init__(name):
        name = name # self.インスタンス変数 = 引数のname（ここでは"チワワ"）

    #def bark(name):
        #return "吠えたのは、" + name # self.name：インスタンス変数へアクセス

def bark(name):
    return "吠えたのは、" + name
print(bark('チワワ'))