import ezc3d
import numpy as np
import matplotlib.pyplot as plt

test_c3d = ezc3d.c3d(r"C:\Users\justi\OneDrive\Documents\GitHub\OpenBiomechanics\baseball_pitching\data\c3d\000002\000002_003034_73_207_002_FF_809.c3d")
num_markers = test_c3d['header']['points']['size']
meta_data_marker = test_c3d['header']['points']
meta_data_analog = test_c3d['header']['analogs']

#define marker measurement rate and number of frames
fs_marker = meta_data_marker['frame_rate']
num_frames_marker = meta_data_marker['last_frame'] - meta_data_marker['first_frame']

#define analog measurement rate and number of frames
fs_analog = meta_data_analog['frame_rate']
num_frames_analog = meta_data_analog['last_frame'] - meta_data_analog['first_frame']

# create time vectors for marker and analog data
time_marker = np.arange(0, num_frames_marker/fs_marker, 1/fs_marker)
time_analog = np.arange(0, num_frames_analog/fs_analog, 1/fs_analog)

#assign marker labels
marker_labels = test_c3d['parameters']['POINT']['LABELS']['value']

#assign force plate corner coordinates
fp_corners = test_c3d['parameters']['FORCE_PLATFORM']['CORNERS']['value']

# set up plot
fig = plt.figure(figsize = (10,10), facecolor = 'w')
ax = fig.add_subplot(111, projection = '3d')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim3d(-0.5, 2.5)
ax.set_zlim3d(-0.5, 2.)

# hide axis tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

ax.view_init(elev = 20, azim = 0)
# ax.view_init(elev = 10, azim = 90) # uncomment for other viewpoint

# plot data
for i in range(fp_corners.shape[-1]):
    for j in range(4):
        ax.scatter(fp_corners[0, j, i], fp_corners[1, j, i], fp_corners[2, j, i], c = 'r', marker = 'o')
    # draw lines between corners
    for j in range(4):
        ax.plot([fp_corners[0, j, i], 
                 fp_corners[0, (j + 1) % 4, i]], 
                [fp_corners[1, j, i], 
                 fp_corners[1, (j + 1) % 4, i]], 
                [fp_corners[2, j, i], 
                 fp_corners[2, (j + 1) % 4, i]], c='k')
plt.show()

