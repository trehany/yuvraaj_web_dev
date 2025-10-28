Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('''Q1) Do you like Dawn or Dusk?
         1) Dawn
         2) Dusk''')
x = input('enter your choice:  ')
if x == 'Dawn':
  Gryffindor +=1
  Ravenclaw += 1
elif x == 'Dusk':
  Hufflepuff += 1
  Slytherin += 1
else:
  print('Wrong Input')

print('''Q2) When I’m dead, I want people to remember me as: 
         1) The Good
         2) The Great
         3) The Wise
         4) The Bold''')
y = int(input('Enter a number between 1-4: '))
if y == 1:
  Hufflepuff += 2
elif y == 2:
  Slytherin += 2
elif y == 3:
  Ravenclaw += 2
elif y == 4:
  Gryffindor += 2
else:
  print('Wronng Input')

print('''Q3) Which kind of instrument most pleases your ear?
         1) The violin
         2) The trumpet
         3) The piano
         4) The drum''')

z = int(input('Enter a number between 1-4: '))
if z == 1:
  Slytherin += 4
elif z == 2:
  Hufflepuff += 4
elif z == 3:
  Ravenclaw += 4
elif z == 4:
  Gryffindor += 4
else:
  print('Wronng Input')


print(f'Gryffindor : {Gryffindor}')
print (f'Ravenclaw: {Ravenclaw}') 
print(f'Hufflepuff : {Hufflepuff}')
print (f'Slytherin: {Slytherin}')   