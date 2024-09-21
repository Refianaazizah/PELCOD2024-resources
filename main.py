nilai = int(input("masukkan nilai: "))

nilai =nilai + 5

if (nilai > 90 and nilai <= 100):
    print("selamat anda lulus,dengan nilai yang memuaskan")
elif (nilai > 80):
    print("selamat anda lulus")    
elif(nilai > 70): 
    print("lulus tapi dekat jurang")    
    
else:
    print("anda masih belum lulus tes,semangat dan coba lagi")


# for loop
for i in range(10, 0, -2):
   print(i)
   print("hello world")


angka = 10

while (angka > 1):
   print(angka)
   angka -= 1 # angka = angka - 1

# [function]
# def
def sayHello():
    print("hello refi")
    print("selamat pagi")

sayHello()
sayHello()
sayHello()
sayHello()

fungsi_kurang4 = lambda param_angka : param_angka - 4

angka = 10

print(fungsi_kurang4(angka))