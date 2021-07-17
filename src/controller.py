domain_x = 1000
domain_y = 1000
tiles_x = 3
tiles_y = 2

def calculate_id(x, y, x_len):
    return x + y * x_len

def get_borders(x, y, x_len, y_len):
    # Added to current coordinate to find the specified side's adjacent tile.
    # Up is +y and Right is +x. And Coordinate is in order [x, y].
    # List in order: Up, Right, Down, Left.
    # Returns a list of values of either ids or a wall as -1.
    side_offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    borders = []
    for offset in side_offsets:
        new_x = x + offset[0]
        new_y = y + offset[1]
        
        # Coordinates include 0, so length in 1 larger than the highest coordinate.
        if new_x > x_len-1 or new_x < 0:
            borders.append(-1)
        elif new_y > y_len-1 or new_y < 0:
            borders.append(-1)
        else:
            borders.append(calculate_id(new_x, new_y, x_len))
    return borders

def gen_tiles(dom_x, dom_y, x_tiles, y_tiles):
    tile_data = []
    tsize_x = dom_x/x_tiles
    tsize_y = dom_y/y_tiles
    for y in range(y_tiles):
        for x in range(x_tiles):
            tile_data.append({
                "tile_pos": [x, y],
                "id": calculate_id(x, y, x_tiles),
                "borders": get_borders(x, y, x_tiles, y_tiles),
                "start_pos": [tsize_x*x, tsize_y*y],
                "end_pos": [tsize_x*(x+1), tsize_y*(y+1)]
            })
    return tile_data

print(gen_tiles(domain_x, domain_y, tiles_x, tiles_y))