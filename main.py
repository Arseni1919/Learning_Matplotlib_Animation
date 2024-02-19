import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation


fig, ax = plt.subplots()
t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
z = g * t**2 / 2 + v0 * t

v02 = 5
z2 = g * t**2 / 2 + v02 * t

scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
line2 = ax.plot(t[:20], z2[:20], label=f'v0 = {v02} m/s')[0]
ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()


def update(frame):
    # for each frame, update the data stored on each artist.
    x = t[:frame]
    y = z[:frame]
    if frame > 1:
        x = t[frame - 1:frame]
        y = z[frame - 1:frame]

    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)

    # update the line plot:
    # line2.set_xdata(t[:frame])
    # line2.set_ydata(z2[:frame])
    # return (scat, line2)
    return scat


ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=300)
# ani.save(filename="pillow_example.gif", writer="pillow")
# ani.save(filename="html_example.htm", writer="html")
# ani.save(filename="ffmpeg_example.mp4", writer="ffmpeg")
plt.show()


# fig, ax = plt.subplots()
# rng = np.random.default_rng(19680801)
# data = np.array([20, 20, 20, 20])
# x = np.array([1, 2, 3, 4])
#
# artists = []
# colors = ['tab:blue', 'tab:red', 'tab:green', 'tab:purple']
# for i in range(20):
#     data += rng.integers(low=0, high=10, size=data.shape)
#     container = ax.barh(x, data, color=colors)
#     artists.append(container)
#
#
# ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=400)
# ani.save(filename="pillow_example.gif", writer="pillow")
# ani.save(filename="html_example.htm", writer="html")
# ani.save(filename="/tmp/ffmpeg_example.mp4", writer="ffmpeg")
# plt.show()




