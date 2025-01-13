class India():
    def capital(self):
        print("The Capital of India is New Delhi")

class USA():
    def capital(self):
        print("The Capital of USA is Washington DC")

class Brazil():
    def capital(self):
        print("The Capital of Brazil is Brasilia")


class USA():
    def capital(self):
        print("The Capital of USA is Washington DC")


class China():
    def capital(self):
        print("The Capital of China is Beijing")



class France():
    def capital(self):
        print("The Capital of France is Paris")

class Malaysia():
    def capital(self):
        print("The Capital of Malaysia is Kuala Lumpur")


obj_india = India()
obj_usa = USA()
obj_france = France()
obj_brazil = Brazil()
obj_china = China()
obj_malaysia = Malaysia()
   
for i in (obj_india,obj_usa,obj_france,obj_brazil,obj_china,obj_malaysia):
    i.capital()