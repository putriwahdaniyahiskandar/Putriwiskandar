# DESKRIPSI BENDA
print("deskripsi boneka")
boneka=[]

# STRING
merk= input("merk boneka: ")
print("merk boneka adalah:",merk)
print("-bertype:" ,type(merk))
boneka.append(merk)

# INTEGER
ukuran = int(input("ukuran boneka:"))
print("ukuran boneka adalah:",ukuran)
print("_bertype:",type(ukuran))
boneka.append(ukuran)

# FLOAT
harga = float(input("harga boneka"))
print("harga boneka adalah:",harga)
print("-bertype ",type(harga))
boneka.append(harga)

# STRING
color = input("color boneka:")
print("color boneka adalah:",color)
print("-bertype: ",type(color))
boneka.append(color)

# INTEGER
total = int(input("total boneka yang di miliki:"))
print("total boneka adalah:",total)
print("-bertype: ",type(total))
boneka.append(total)

print("merk boneka adalah",merk,"dengan ukuran",ukuran,"dengan harga",harga,"color",color,"dan total yang dimiliki",total)

print(boneka)
