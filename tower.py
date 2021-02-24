def tower_builder(n_floors):
    max_stars = (n_floors * 2) - 1
    tower_array = []
    
    for star in range(1, max_stars + 2, 2):
        layer = "*" * star
        layer[0] = layer[0].center(max_stars)
        tower_array.append(layer)
    return tower_array

print(tower_builder(5))