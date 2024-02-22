#Task_N1
'''
1.	შექმენი კლასი რომელსაც ექნება public, protected და private პარამეტრები.
გამოიყენე @property დეკორატორი და ასევე შექმენი setter და  getter დეკორატორებიანი ფუნქციები პარამეტრებზე წვდომისა და რედაქტირებისთვის.   
2.	შექმენი მისი შვილობილი კლასი და შეუცვალე რაიმე არსებული მეთოდი.
'''
print("Task_N1")

class Main:
    def __init__(self, public, _protected, __private):
        self.public = public
        self._protected = _protected
        self.__private = __private
    @property
    def get_public(self):
        return self.public
    @property
    def get_protected(self):
        return self._protected
    @property
    def get_private(self):
        return self.__private
    @get_public.setter
    def set_public(self, value):
        self.public = value
    @get_protected.setter
    def set_protected(self, value):
        self._protected = value
    @get_private.setter
    def set_private(self, value):
        self.__private = value

instance = Main("Main_Public_V1", "Main_Protected_V1", "Main_Private_V1")

print(f"Public_V1: ", instance.get_public)
print(f"Protected_V1: ", instance.get_protected)
print(f"Private_V1: ", instance.get_private)

instance.set_public = "Main_New Public_V2"
instance.set_protected = "Main_New Protected_V2"
instance.set_private = "Main_New Private_V2"

print(f"Modified Public :", instance.get_public)
print(f"Modified Protected :", instance.get_protected)
print(f"Modified Private :", instance.get_private)
print()



