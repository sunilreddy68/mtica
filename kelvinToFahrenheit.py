
def kelvinToFahrenheit(Temperature):
    assert (Temperature>=0),'colder than absolute zero at MTICA'
    res=((Temperature-273)*1.8)+32
    return res
try:
    print(kelvinToFahrenheit(-50))
except Exception as ob:
    print(ob)
try:
    print(kelvinToFahrenheit(273))
except Exception as ob:
    print(ob)    
try:
    print(kelvinToFahrenheit(50.78))
except Exception as ob:
    print(ob)    
try:
    print(kelvinToFahrenheit(-5))
except Exception as ob:
    print(ob)
print("sunil reddy")
