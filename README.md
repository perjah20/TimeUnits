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

## License
This project is licensed under an Attribution License - you are free to use, 
distribute, and modify the code as long as you provide appropriate credit to 
the original author. Please see the LICENSE file for more details.


When you decide on a specific license, replace "Attribution License" with the name of your chosen license and provide a `LICENSE` file in your repository that clearly states the license terms.

Remember, the package name `timeunits` or `timeunit` and the precise license terms you wish to apply (requiring attribution) are crucial details, so make sure they're clearly communicated in your project documentation and setup configuration.
