import os #載入operating system模組

products = []
if os.path.isfile('products.csv'): #檢查檔案在不在
	print('找到檔案！')

	#讀取檔案
	with open('products.csv', 'r', encoding='utf-8') as e:
		for line in e:
			if '品名,價格' in line:
			    continue #繼續
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案~')


#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

#印出所有購買紀錄
for product in products:
	print(product[0], '的價格是', product[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('品名,價格\n')
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')
