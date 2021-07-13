'''Given the exclusive price of milk calculate the inclusive price of items in tuskys supermarket
'''
exclusivePrice = 45.34
vatTax = 16/100
vatAmount = exclusivePrice * vatTax 
inclusivePrice = exclusivePrice + (exclusivePrice * vatTax)
print(inclusivePrice)