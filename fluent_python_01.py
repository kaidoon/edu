import pprint as pp
import array

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
