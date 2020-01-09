alien_0 = {'x_position': 1,'y_position': 25, 'speed':'fast'}
# mudar a posicao x do alien, de acordo com sua velocidade

print(f"The original x_position: {alien_0['x_position']}")

if alien_0['speed'] == 'low':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2

else:
    # alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x_position'] += x_increment

print(f"New x-position: {alien_0['x_position']}")