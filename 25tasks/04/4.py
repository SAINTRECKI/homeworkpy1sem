file = open('products.csv')
result = open('expensive.csv', 'w')
result.write(file.readline() + '\n')
for stroke in file:
    temp = stroke.split(',')
    if int(temp[2]) > 100:
        result.write(stroke)
