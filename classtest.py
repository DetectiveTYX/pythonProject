# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def sit(self):
#         print(f"{self.name} is now sitting")
#     def roll_over(self):
#         print(f"{self.name} roll over!")

class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} has {self.cuisine_type} ")
        print(self.restaurant_name + " has " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is opening.")


restaurant = Restaurant("restaurant", "it")
restaurant.describe_restaurant()
restaurant.open_restaurant()


class User:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def describe_user(self):
        print("user is " + self.first_name + self.last_name)

    def greet_user(self):
        print("welcome," + self.first_name + self.last_name + "!")


"""父类，子类"""


class inner:
    def __init__(self, characteristic, money=0):
        self.characteristic = characteristic
        self.money = money

    def describe_inner(self):
        print("with " + self.characteristic + " has " + str(self.money))


class MasterUser(User):
    def __init__(self, first, last, Inner, money=0):
        super().__init__(first, last)
        self.inner = inner(Inner, money)

    def describe_user(self):
        print("user is " + self.first_name + self.last_name + ",the master user")


tyx = MasterUser("tao", "yuxuan", "inner", 20)
yxy = User("yao", "xinyan")

tyx.describe_user()
tyx.inner.describe_inner()
yxy.describe_user()

tyx.greet_user()
yxy.greet_user()

import re

a = "\d\.\d+"
b = "1.2345"
match = re.match(a, b)
print(match)
# 匹配


patten = "破解|呵呵"
b = "我可以破解你呵呵"
match = re.sub(patten, 'xxx', b)
print(match)
# 替换，屏蔽关键词


patten = '[/|.]'
b = "https://?zhuanlan.zhihu.com/p/43750433"
match = re.split(patten, b)
print(match)


def fun(name="1", *b,**a):
    print(name)
    print(b)
    for i in a:
        print(i)

fun("haha",4,2)