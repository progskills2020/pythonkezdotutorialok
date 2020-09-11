
#while ciklus 
"""
#felépítése: 
while feltétel:
    futtatandó programsorok
    -
    -
    kilépő feltétel

#működése: amíg a feltétel IGAZ, addig a while ciklus futni fog,
#          a KILÉPŐ FELTÉTELLEL kell meghatároznunk, hogy a program
#          futása MIKOR álljon le
"""

run = True
szamlalo = 0
hanyszor_fusson = int(input("Hányszor fusson le a program"))

while run:
    print("hello %d" % szamlalo)
    szamlalo+=1
    if szamlalo == hanyszor_fusson:
        break
    





