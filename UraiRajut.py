def urai(kata):
    string = '' #string kosong utk menampung uraian / hasil iterasi
    for i in kata:
        string = string + i
        print(string,end='') #menggunakan parameter end agar tidak membentuk new line
    return string

print(urai('code'))
print(urai('python'))
print(urai('purwadhika'))
