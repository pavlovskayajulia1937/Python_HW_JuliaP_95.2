from smartphone import Smartphone

catalog = [
    Smartphone("11", "x",  "+17"),
    Smartphone("15", "v", "+67" ),
    Smartphone("1", "k", "+98"),
    Smartphone("6", "g", "+45" ),
    Smartphone("223", "r", "+7" )
]

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model} - {smartphone.number}")
