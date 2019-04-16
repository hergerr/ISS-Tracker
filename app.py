import requests, json, turtle

def move(length, width):
    global iss

    iss.penup()
    iss.goto(length, width)
    iss.pendown()

def setup_display(display):
    global iss
    
    display= turtle.Screen()
    display.setup(1000,500)
    display.bgpic('earth.gif')
    display.setworldcoordinates(-180, -90, 180, 90)

    iss = turtle.Turtle()
    iss.shape('circle')
    iss.color('black')

def track_iss():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        location = response_dict['iss_position']
        move(float(location['latitude']), float(location['longitude']))
    else:
        print('Request failed')
    widget = turtle.getcanvas()
    widget.after(1000, track_iss)

global iss
setup_display(turtle.Screen)
track_iss()
turtle.mainloop()