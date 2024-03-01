num = input('Enter a number (decimal or integer): ')
# type your code here
a=num.strip(" ")
b=a.replace(".","")
c=b.lstrip("0")
sf = len(c)
# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
