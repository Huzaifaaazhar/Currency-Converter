with open ('CurrencyData.txt') as f:
    lines = f.readlines()
    
Currency_convert = {}
for line in lines:
    parsed = line.split("\t")
    Currency_convert[parsed[0]] = parsed[1]
    
Amount = int(input("Enter Amount: \n"))
print("Enter Currency Name to convert in: \n")
[print (item) for item in Currency_convert.keys()]
Currency = input("Enter name of Currency: \n")
print(f"{Amount} PKR is equal to {Amount * float(Currency_convert[Currency])} {Currency}")
