def DecimalToBinary(num, k_prec):
    binary = ""
    Integral = int(num)
    fractional = num - Integral
    while(Integral):
        rem = Integral % 2
        binary += str(rem)
        Integral //= 2
    binary = binary[ : : -1]
    while (k_prec) :
         
        # Find next bit in fraction
        fractional *= 2
        fract_bit = int(fractional)
 
        if (fract_bit == 1) :
             
            fractional -= fract_bit
            binary += '1'
             
        else :
            binary += '0'
 
        k_prec -= 1
 
    return binary



arr = []
num_arr = []



f = open("decimal_real_value.txt", 'r')
f_2 = open("decimal_binary_value.txt", 'w')

while True:
    line = f.readline()
    line = line.strip("\n")
    arr.append(line)
    if not line: break
             
num_arr = list(map(float, arr[0:len(arr)-1]))

for j in range(0, len(num_arr)):
    num_arr[j] = DecimalToBinary(num_arr[j], 12)

for i in range(0, len(num_arr)):    
    f_2.write(str(num_arr[i]))
    f_2.write("\n")
    
f.close()
f_2.close()