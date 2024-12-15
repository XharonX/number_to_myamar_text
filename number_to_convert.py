from math import log10


class NumToMM():
    digit = ['သုည', 'တစ်', 'နှစ်', 'သုံး', 'လေး', 'ငါး', 'ခြောက်', 'ခုနှစ်', 'ရှစ်', 'ကိုး']
    power = ['', 'ဆယ်', 'ရာ', 'ထောင်', 'သောင်း', 'သိန်း']
    
    def convert_to_mm(self, number):
        conv_str = ""
        base = 10
        if number == 0:
            return conv_str
        
        else:
            try:
                i = int(log10(number))
                d = number // base ** i
                num = d * base ** i
                conv_str = self.digit[d] + self.power[i]
                if number - num > 0:
                    if "း" not in self.power[i]:
                        conv_str += "့"
                    conv_str += self.convert_to_mm(number - num)
            except IndexError:
                p = self.power[-1]
                i = self.power.index(p)
                num = number // (base ** i) 
                n = number % (base ** i)
                if log10(num) > 1 and not n and num % base:
                    conv_str = p + self.convert_to_mm(num)
                else:
                    conv_str += self.convert_to_mm(num) + p
                conv_str += self.convert_to_mm(n)
        return conv_str
