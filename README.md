# TimeUnits

The TimeUnits library offers a straightforward and intuitive approach for handling
time units in Python. It facilitates easy conversions between various time units, 
promoting clear and concise code. Inspired by ['Orders of Magnitude (Time)'](https://en.wikipedia.org/wiki/Orders_of_magnitude_(time)), this
project aims to ease time-related calculations in software development.


## Features

- Define and manipulate time units explicitly in your code.
- Convert between an extensive range of time units, from seconds to yottaseconds and beyond.
- Perform arithmetic operations on time units, such as addition, subtraction, multiplication, and division.
- Designed for extensibility, allowing for the easy addition of new time units.

## Quick Start
Here's how you can use TimeUnits to work with different time scales:
```python
from timeunits import Sec, QuectoSec

# Creating a second
one_second = Sec(1)

# Converting to QuectoSeconds
quecto_seconds = one_second.to_quecto()
print(quecto_seconds)  # Expected output: 1000000000000000000000 qs

# Converting back to Seconds
seconds = quecto_seconds.to_sec()
print(seconds)  # Expected output: 1 s
```

## Contributing
Your contributions are welcome! If you'd like to add new time units, enhance 
the documentation, or fix issues, we'd appreciate your help. Please fork the 
repository, make your changes, and submit a pull request.
