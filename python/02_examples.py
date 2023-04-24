# Neste segundo vídeo vimos:

# 	- Uma esplicação sobre variáveis e strings
# 	  Link: https://www.w3schools.com/python/python_variables.asp

#	- Como acessar python keyworkds
#     Link: https://www.edureka.co/community/49394/python-function-to-find-a-list-of-all-keywords#:~:text=You%20can%20use%20the%20keyword,the%20current%20version%20of%20python.

	# - Nomenclatura de variáveis
	#   Link: https://www.w3schools.com/python/python_variables_names.asp


x = 5
y = 'John'

print(x)
print(y)
print(type(x))
print(type(y))

import keyword
list = keyword.kwlist 
print('---Print da lista sem for loop--')
print(list)

print('---Print da lista com for loop--')
for item in list:
	print(item)	

print('--Atribuindo mais de uma variável por linha---')
x, y, z, w = 'Laranja', 'Banana', 'Cherry', 'Abacaxi'
print(x)
print(y)
print(z)
print(w)
