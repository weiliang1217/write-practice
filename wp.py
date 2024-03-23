products = []
while True: #強制進入loop環節；(boolen-> True or fail)
	item = input('商品名稱: ')
	if item == 'q':
		break # 當再商品紀錄: 輸入'q'時，會執行break 離開loop
	price = input('商品價錢: ')
	products.append([item, price])
print(products)
print(products[0][0])
print(products[0][1])
print(products[1][0])
print(products[1][1])

with open('wp1.csv', 'w') as file: # 將'wp1.csv'作為file稱呼，隨著with open結束 file定義也release
	for product in products:
		file.write(product[0] + ',' + product[1] + '\n')

with open('wp1.txt', 'w') as file:
	for product in products:
		file.write(product[0] + ',' + product[1] + '\n')

print('------------------------')

products1 = []
with open('wp1.csv', 'r') as file:
	for product1 in file:
		products1.append(product1)
		print(products1)

products2 = []
with open('wp1.txt', 'r') as file:
	for product2 in file:
		products2.append(product2)
		print(products2)