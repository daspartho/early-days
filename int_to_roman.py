def roman(num):
    roman_num = ''
    converter = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

    while num != 0:
        for i in converter:
            if i <= num:
                roman_num += converter[i]
                roman_num += ''
                num -= i
                break
    return roman_num
print(roman(321)) 

     
    
















