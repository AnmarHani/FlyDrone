# FlyDrone
## Description:
FlyDrone is still in its early stages, developing an easy and automated api for controlling drones using python.

## Documentation:
First, we create an instance of the ``Drone`` class, the ``Drone`` class takes the connection string as a parameter:
```py
from flydrone import Drone

my_first_drone = Drone("udp:localhost:14550")
```
