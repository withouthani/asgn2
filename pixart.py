import turtle as t

screen = t.Screen()
screen.setup(600, 600)
t.speed(-1000)

def get_color(char):
    if char == '0':
        return 'black'
    elif char == '1':
        return 'white'
    elif char == '2':
        return 'red'
    elif char == '3':
        return 'yellow'
    elif char == '4':
        return 'orange'
    elif char == '5':
        return 'green'
    elif char == '6':
        return 'yellowgreen'
    elif char == '7':
        return 'sienna'
    elif char == '8':
        return 'tan'
    elif char == '9':
        return 'gray'
    elif char == 'A':
        return 'darkgray'
    else:
        return None
    
def draw_color_pixel(color_string, turta):
    t.fillcolor(color_string)
    t.begin_fill()
    
    for _ in range(4):
        t.forward(20)
        t.right(90)
    
    t.end_fill()

def draw_pixel(char, turta):
    color_string = get_color(char)
    if color_string:
        draw_color_pixel(color_string, turta)

def draw_line_from_string(color_string, turta):
    prev_pos = t.pos() # preserves the starting point on the row
    for char in color_string:
        color = get_color(char)
        if color:
            draw_pixel(char, turta)
            t.forward(20)
        else:
            return False
    
    ## added for draw_grid
    t.goto(prev_pos)
    t.penup()
    t.setheading(270)
    t.forward(20)
    t.setheading(0)
    t.pendown()
    return True

def draw_shape_from_string(color_string, turta):
    if len(color_string) >= 1:
        pass
    else:
        color_string = input("Enter a color string: ") ## to triger input, pass color_string parameter as ("")
    draw_line_from_string(color_string, turta)
    turta.penup()
    turta.setheading(270)  
    turta.forward(20)      
    turta.setheading(180) 
    turta.forward(20 * len(color_string))  
    turta.setheading(0)   
    turta.pendown()

def draw_grid(turta):
    t.penup()
    t.goto(-250, 250)
    t.pendown()
    for row in range(20):
        if row % 2 == 0:
            test_string = "02020202020202020202"
            print(0)
        else:
            test_string = "20202020202020202020"
            print(1)
        draw_line_from_string(test_string, turta)

def draw_shape_from_file(turta):
    t.penup()
    t.goto(-250, 250)
    t.pendown()
    txtinput = input("Enter the path for a .txt blueprint: ")
    txtloc = open(txtinput, "r")
    #print(txtloc.read()) use this to confirm the txt file is getting imported correctly
    txtread = (txtloc.read()).splitlines()
    # print(txtread) use this to confirm the txt file is split correctly
    for row in range(len(txtread)):
        prev_pos = t.pos() # preserves the starting point on the row
        color_string = txtread[row]
        print(color_string)
        draw_shape_from_string(color_string, turta)
        t.goto(prev_pos)
        t.penup()
        t.setheading(270)
        t.forward(20)
        t.setheading(0)
        t.pendown()


turta = t.Turtle()
draw_shape_from_file(turta)


t.done()