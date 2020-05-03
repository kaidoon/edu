import pprint as pp

symbols = '¢æ…–¢¬¢¶äööü¬¢ääöä'
# the symbol var in the listcomp (list comprehention) are
codes = [ord(symbol) for symbol in symbols]
pp.pprint(codes)

