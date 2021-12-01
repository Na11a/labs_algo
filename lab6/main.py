from io_data import *
from words import Words

data = input_data('./IO/wchain3.in')

words = Words(data['words'],data['count'])
words.counter(True)
max_chain = words.get_max_chain(True)
output_data('./IO/wchain.out',max_chain)

