class CarStore(object):
    def select_car(self, car_type):
        pass

    def order(self, car_type):
        return self.select_car(car_type)


class BMWCarStore(CarStore):
    def __init__(self):
        self.factory = BMWFactory()

    def select_car(self, car_type):
        return self.factory.select_car_by_type(car_type)


class BENZCarStore(CarStore):
    def __init__(self):
        self.factory = BENZFactory()

    def select_car(self, car_type):
        return self.factory.select_car_by_type(car_type)


class BMWFactory(object):
    def select_car_by_type(self, car_type):
        if car_type == "740":
            return BMW_740()
        elif car_type == "X5":
            return BMW_X5()
        elif car_type == "MiNi":
            return BMW_MiNi()


class BENZFactory(object):
    def select_car_by_type(self, car_type):
        if car_type == "S600":
            return BENZ_S600()
        elif car_type == "G500":
            return BENZ_G500()
        elif car_type == "A180":
            return BENZ_A180()


class Car(object):
    def move(self):
        print("车启动了")

    def music(self):
        print("车上播放音乐")

    def stop(self):
        print("车停了")

    def print_car(self):
        pass


class BMW_740(Car):
    def print_car(self):
        print("我是 宝马 740")


class BMW_X5(Car):
    def print_car(self):
        print("我是 宝马 X5")


class BMW_MiNi(Car):
    def print_car(self):
        print("我是 宝马 MiNi")


class BENZ_S600(Car):
    def print_car(self):
        print("我是 奔驰 S600")


class BENZ_G500(Car):
    def print_car(self):
        print("我是 奔驰 G500")


class BENZ_A180(Car):
    def print_car(self):
        print("我是 奔驰 A180")


bmw_car_store = BMWCarStore()

car = bmw_car_store.order("740")
car.print_car()
