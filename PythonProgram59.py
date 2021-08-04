class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")


class Samsung(Phone):
     def photo(self):
         print("You can take a photo")


s = Samsung()
s.message()
s.call()
s.photo()
