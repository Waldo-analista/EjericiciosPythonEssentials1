def liters_100km_to_miles_gallon(litros_100km):
    mile=(1609.344/1000)/100 #100km
    gallon=3.785411784 #litros
    litros=1/gallon  #gallon
    cien_km=1/mile #mile
    var=litros_100km*(litros/cien_km)
    return var**-1

def miles_gallon_to_liters_100km(miles_gallon):
    mile=(1609.344/1000)/100 #100km
    gallon=3.785411784 #litros
    var=miles_gallon*(mile/gallon)
    return var**-1

#1 American mile = 1609.344 metres
#1 American gallon = 3.785411784 litres.

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))