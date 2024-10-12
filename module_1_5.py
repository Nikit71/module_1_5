# Неизменяемые и изменяемые объекты. Кортежи
print('Практическая работа по уроку "Неизменяемые и изменяемые объекты. Кортежи"')
immuteble_var=([1971,'март',13],'Никитин',53)
muteble_var=[[1971,'март',13],'Никитин',53]
print("Операции со списком")
print("Список muteble_var:",muteble_var)

print(muteble_var[1])
muteble_var[1]='Евгений'
print(muteble_var)
muteble_var[0][1:]='май'
print(muteble_var)
muteble_var[1:]=muteble_var[1]
print(muteble_var)
print()
print("Операции с кортежем")
print("Кортеж immuteble_var:",immuteble_var)
print(immuteble_var[1])
immuteble_var[0][1]='Май'
print(immuteble_var)
immuteble_var[1]='Евгений'
print(immuteble_var)