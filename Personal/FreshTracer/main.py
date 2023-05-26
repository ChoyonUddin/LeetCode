#FreshTracer
#August 8th 2022 -
#imports
from PIL import Image
import math
from vec3 import vec3, color

#Decide to attempt to make a ray tracer because I kinda want to make something cool that isn't entirely braindead easy and 
#Some of my friends have made raytracers before so I decided why not. I will be referencing Peter Shirley Documentation and Github
#Ray Tracing in one weekend. The raytracer documentation is written in C++ however this is going to be in Python because I am
#idk

#Image

WIDTH = 256
HEIGHT = 256

img = Image.new(mode='RGB',size=(WIDTH,HEIGHT))

#Render


for x in range(WIDTH):
    for y in range(HEIGHT):
        
#*
#         r = x/(WIDTH-1)
#         g = y/(HEIGHT-1)
#         b = 0.25

#         r = math.ceil(r*255)
#         g = math.ceil(g*255)
#         b = math.ceil(b*255)

        pixel = color(x/(WIDTH-1),y/(HEIGHT-1),0.25)
        img.putpixel(xy=(x,HEIGHT - y -1),value=pixel.to_rgb())
        
#
img.save("test.png")