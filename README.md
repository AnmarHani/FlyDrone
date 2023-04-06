# FlyDrone
## Description:
FlyDrone is still in its early stages, developing an easy and automated api for controlling drones using python.

## Getting Started:
Starting up, we create an instance of the ``Drone`` class, the ``Drone`` class takes the connection string as a parameter:
```py
from flydrone import Drone

my_first_drone = Drone("udpin:localhost:14550")
```
if no parameter is specified, it will be assigned to ``udpin:localhost:14550`` by default.
<br>
Now we have access to different awesome functions to control the drone, lets have some examples:
```py
my_first_drone.arm() # If your drone is ready, this should arm
my_first_drone.takeoff(15) # The drone should takeoff with altitude of 15
```

## Documentation: **STATUS - INCOMPLETE**
``Drone``: a class that holds all functionalities and takes the connection string as a parameter. You can refer to this documentation for more information about connection strings https://mavlink.io/en/mavgen_python/.
<br>
``Drone/arm()``: a function that make the drone arm if its ready.
<br>
``Drone/disarm()``: a function that make the drone disarm if its ready.
<br>
``Drone/takeoff()``: a function that make the drone takeoff if its armed and ready, takes the altitude as a parameter.
<br>
``Drone/change_mode()``: a function that changes the drone's mode if its ready, takes the mode as a parameter. You can refer to this documentation for more information about drone's modes https://ardupilot.org/copter/docs/flight-modes.html.
<br>
``Drone/return_to_launch()``: a function that changes the drone's mode to RTL so it returns to the place that its launched from.
<br>
``Drone/local_movement()``:

