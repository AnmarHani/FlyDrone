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

## Documentation
