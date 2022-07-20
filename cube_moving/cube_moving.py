import bpy

from math import sin, cos, radians

for i in range(0, 361, 10):
    obj = bpy.context.object
    obj.location = 15*cos(radians(i)), 15*sin(radians(i)), 4*sin(radians(i*6))
    obj.keyframe_insert(data_path="location", frame=i)
