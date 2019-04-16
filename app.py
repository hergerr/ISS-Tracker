import requests
import json
import turtle


class IssTracker:

    def __init__(self):
        self.iss = turtle.Turtle()
        self.iss.shape('circle')
        self.iss.color('black')

    def move(self, length, width):
        self.iss.penup()
        self.iss.goto(length, width)
        self.iss.pendown()

    def setup_display(self, display):
        display = turtle.Screen()
        display.setup(1000, 500)
        display.bgpic('earth.gif')
        display.setworldcoordinates(-180, -90, 180, 90)

    def track_iss(self):
        response = requests.get('http://api.open-notify.org/iss-now.json')
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            location = response_dict['iss_position']
            self.move(float(location['latitude']), float(location['longitude']))
        else:
            print('Request failed')
        widget = turtle.getcanvas()
        widget.after(1000, self.track_iss)


issTracker = IssTracker()
issTracker.setup_display(turtle.Screen())
issTracker.track_iss()
turtle.mainloop()
