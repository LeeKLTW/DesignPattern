# -*- coding: utf-8 -*-
import weakref # Weak reference support for Python.

class CarModel:
    _models = weakref.WeakKeyDictionary()

    def __new__(cls,model_name,*args,**kwargs):
        model = cls._models.get(model_name)

        if not model:
            model = super().__new__(cls)
            cls._models[model_name] = model
        return model

    def __init__(self, model_name, air=False,tilt=False, power_locks=False, alloy_wheel=False, usb_charger=False):
        if not hasattr(self,"initted"):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.power_locks = power_locks
            self.alloy_wheel = alloy_wheel
            self.usb_charger = usb_charger

    def check_serial(self, serial_number):
        print(f"Sorry, we are unable to check {serial_number} at {self.model_name}")

class Car:
    def __init__(self,model,color,serial):
        self.model = model
        self.color = color
        self.serial = serial

    def check_serial(self):
        return self.model.check_serial(self.serial)


# todo debug
# dx = CarModel("FIT DX")
# lx = CarModel("FIT LX", air=True, cruise_control=True,power_locks=True, tilt=True)
# car1 = Car(dx, "blue", "12345")
# car2 = Car(dx, "black", "12346")
# car3 = Car(lx, "red", "12347")
#
#
# id(lx)
# del lx
# del car3
# import gc
# gc.collect()
# lx = CarModel("FIT LX", air=True, cruise_control=True,power_locks=True, tilt=True)
# id(lx)
# lx = CarModel("FIT LX")
# id(lx)