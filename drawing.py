from turtle import Screen, Turtle
from pixart import draw_grid, draw_shape_from_file, draw_shape_from_string

# Main function and script
def main():
    screen = Screen()
    turta = Turtle()

    draw_shape_from_string("", turta)  
    draw_shape_from_file(turta)
    draw_grid(turta)

    screen.exitonclick() 

if __name__ == "__main__":
    main()
