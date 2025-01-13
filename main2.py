class roman :
    def rom_num(self, num):
        r_n = [(1000, "M"),(50 ,"L"),(5 ,"V")] 
        result = ""
        for(n , rome) in r_n :
            (d , num) = divmod(num , n)
            result += rome * d
        return result


print(roman().rom_num(1050))