# dominantColourFinder
This Python program finds the dominant colour/s in an image. This solution aims for simplicity, readability, and correctness within a reasonable time frame.

Main functionality:
- Find the most dominant colour: The program calculates the colour that appears most frequently in an image.
- Ignore specific colours: Optionally, you can provide a list of colours to be ignored during the calculation.
- Retrieve top N dominant colours: The program can return the top N most frequent colours.
  
We are using a colour space reduction, to avoid minor colour differences. The RGB values of each pixel are rounded to the nearest multiple of 10.

Requirements:
Python 3.x,
Pillow library (image processing),

To install:
Clone the repository or download the code files.
Install the required library: pip install pillow.

To run the script:
Use a file demo.py

Notes:
At the moment, the program does not handle cases where multiple colours have the same maximum frequency, it will return the one of the colours with maximum frequency.
This is an area for improvement in the future.
