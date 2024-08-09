import ezc3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#loading the c3d file
c3d = ezc3d.c3d(r"C:\Users\justi\OneDrive\Documents\GitHub\OpenBiomechanics\baseball_pitching\data\c3d\000002\000002_003034_73_207_002_FF_809.c3d")
labels = c3d["parameters"]["POINT"]["LABELS"]["value"]
points = c3d["data"]["points"]

fig = plt.figure(figsize=(14,5))
select_frames = [100, 200, 300, 400, 500, 600, 700]
for i, frame in enumerate(select_frames):
  ax = fig.add_subplot(1, 4, i+1, projection='3d')
  x = points[0, :, frame]
  y = points[1, :, frame]
  z = points[2, :, frame]
  marker_points = ax.scatter(x, y, z, alpha=0.75, color='red')
  ax.set_title(f"Frame {frame} of {points.shape[2]}")
  ax.axis('equal')
  ax.set_xticklabels([])
  ax.set_yticklabels([])
  ax.set_zticklabels([])
  ax.view_init(elev=30, azim=-55, roll=0)
  
