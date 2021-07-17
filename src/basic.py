from random import randint

grid_x = 10
grid_y = 10
ballno = 10
minvel = 1
maxvel = 2

# Functions
def gen_render_array(balls, x_size, y_size):
    # render_array = [[' '] * x_size] * y_size
    # render_array2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    render_array = []
    for y in range(y_size):
        for x in range(x_size):
            render_array[y][x] = " "
    # if render_array != render_array2:
    #     print("Oh!")
    # else:
    #     print("Nope")
    print(render_array)
    for ball in balls:
        loc = ball["loc"]
        # print(loc[1], loc[0])
        render_array[loc[1]][loc[0]] = "o"
        # print(render_array[loc[1]])
        # x = render_array[loc[1]]
        # x[loc[0]] = "o"
        # print(x)
        # render_array[loc[1]] = x
        # print(render_array[1])
        # render_array[9][1] = "o"
    return render_array

# Generate balls
balls = []
for n in range(ballno):
    balls.append({
        "loc": [randint(0, grid_x-1), randint(0, grid_y-1)],
        "velocity": [randint(minvel, maxvel), randint(minvel, maxvel)]
    })
print(balls)

# Main loop
while True:
    render_array = gen_render_array(balls, grid_x, grid_y)
    print(render_array)
    for line in render_array:
        print((" ".join(line)))
    exit()