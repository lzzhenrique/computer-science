from collections import namedtuple


class Address:
    def __init__(self, street, number, district):
        self.street = street
        self.number = number
        self.district = district


class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address


address = Address(
    street='Rua da camomila',
    number=555,
    district='bairro Maranhao')


User('Luiz H', address)


# named tuple example

GeoPoint = namedtuple('Geopoint', 'lat lon')
print(namedtuple('Geopoint', 'lat lon'))

location = GeoPoint(-22.81711234090266, -47.069559317039655)

print(location)
