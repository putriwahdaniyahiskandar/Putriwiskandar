import datetime

x = datetime.datetime.now()

print (x)
#print (x.year)
#print(x.strftime("%H"))

time = int (x.strftime("%H"))

if time >=00 and time  <= 10 :
    print ("=====================|============|======================")
    print ("                      Annyeonghaseo                       ")
elif time >= 10 and  time <= 15  :
    print ("=====================|============|======================")
    print ("                     Annayeonghaseo                       ")
elif time >= 15 and time  <= 22 :
    print ("=====================|============|======================")
    print ("                      Annyeonghaseo                         ")
    print ("=====================|============|======================")
    print("")

#input

ulang = "ya"
while(ulang == "ya") :
    username = input ("username: ")
    password = input ("password: ")
    if username == "Kim-yunna" and password == "1703" :
        print ("========================================")
        print ("====Annyeong Kim-yunna====")
        print ("=======--|From : Seol|--=======")
        print ("-----------Street jeju----------")
        print ("========================================")
        print ("====================")
        print ("Sistem Konversi Suhu")
        print ("====================")

        
    else :
        print ("username and password failed")
        continue
    #konversi suhu
        
    celcius=float(input("masukan suhu = "))
    farenheit=9/5*celcius+32
    kelvin=273+celcius
    reamur=4/5+celcius
    print("\n")
    print("celcius =",celcius)
    print("farenheit =",farenheit)
    print("kelvin =",kelvin)
    print("reamur=",reamur)


    ulang= input ("DO YOU WANT TO TRY AGAIN?yes/no:")
