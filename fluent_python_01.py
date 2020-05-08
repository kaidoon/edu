import pprint as pp
import array
import os
from collections import namedtuple

symbols = '¢æ…–¢¬¢¶äööü¬¢ääöä'
# the symbol var in the listcomp (list comprehention) are
codes_listcom = [ord(symbol) for symbol in symbols]
pp.pprint('codes_listcom :: ')
pp.pprint(codes_listcom)

# generator expressions : genexp
codes_genexp = tuple(ord(symbol) for symbol in symbols)
pp.pprint('codes_genexp :: ')
pp.pprint(codes_genexp)

# cartesian products
colors = ['yellow', 'red', 'blue', 'black']
sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL']
tshirts = [(color, size) for color in colors for size in sizes]
pp.pprint('codes_listcom (cartesian product) :: ')
pp.pprint(tshirts)

# array
codes_array = array.array('I', (ord(symbol) for symbol in symbols))
pp.pprint('codes_array :: ')
pp.pprint(codes_array)

# tuples as records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveller_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856' )]

pp.pprint('tuples as records :: ')
for passport in sorted(traveller_ids):
    print('%s/%s' % passport)

for country, _ in traveller_ids:
    print(country)

# tuple unpacking
print('tuple unpacking')
latitude, longitude = lax_cordinates
print('latitude :: ', latitude )
print('longitude :: ', longitude)

a = 10
b = 20

b, a = a, b

print('a :: ', a)
print('b :: ', b)

t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print('quotient  :: ', quotient)
print('remainder :: ', remainder)

_, filename = os.path.split('/Users/kaidoon/prj/edu/fluent_python_01.py')
print('filename :: ', filename)

print('* to grab expressions')
a, b, *rest = range(5)
print('a :: ', a, ', b :: ', b, ', rest:: ', rest)

a, b, *rest = range(3)
print('a :: ', a, ', b :: ', b, ', rest:: ', rest)

a, b, *rest = range(2)
print('a :: ', a, ', b :: ', b, ', rest:: ', rest)

a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)

metro_areas = [
    ('Tokio', 'JP', 36.933, (35.689722, 139.691667)),
    ('Dehli NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    print(fmt.format(name, latitude, longitude))

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

# Named tuples
# collection.namedtuple function is afactory that produces subclasses of tuple
# enhanced with field names and a class name (helps debugging)

City = namedtuple('City', 'name country population coordinates')
tokio = City('Tokio', 'JP', 36.933, (35.689722, 139.691667))
print(tokio)
print(tokio.population)
print(City._fields)