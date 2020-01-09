"""
A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.

"""

alien_0 = {'color':'green','points':'zero'}
print(alien_0['color'],alien_0['points'])



# adicionando valores aos dicionarios
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# valores do dictionario podem ser mudados
print(alien_0['color'])
alien_0['color'] = 'yellow'
print(alien_0['color'])

# forma mais legil de escrever dicionarios
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
    
print(f"Sarah's favorit language is {favorite_languages['sarah'].title()}")

# get() method, para caso não tenha algum valor, retornar uma mensagem, é como se fosse um try catch
alien_0 = {'color':'red', 'speed':'fast'}
#se vc tentar imprimir um valor como points, retoranaria um KeyError, pois a chava point nao foi criada
# print(alien_0['points'])
# por isso nos usamos o get()
print(alien_0.get('speed','No point value is assigned'))