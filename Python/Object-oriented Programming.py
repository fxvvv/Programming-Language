# 2024-01-24 Bilibili Study

class Dog:
    d_type = 'JB' # 公共属性：改变某一个实例中的该值，其他实例的该值都会改变

    def say_hi(self): # 方法：第一个参数必须是self，self 代表实例本身
        print("Hello, dog, type:", self.d_type)

d = Dog()
d2 = Dog() # 生成了一个实例

Dog.d_type = "藏獒"
d.say_hi()
