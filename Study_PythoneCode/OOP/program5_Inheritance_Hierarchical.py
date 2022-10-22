# Parent class / Super class / Base class
class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")


# Child class, Sub class, Derrived class
class Samsung(Phone):
    # call, message
    def photo(self):
        print("You can photo")


p = Phone()
p.message()
p.call()

s = Samsung()
s.message()
s.call()
s.photo()

print(issubclass(Samsung, Phone))
