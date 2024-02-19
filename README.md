# Animations using Matplotlib

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
```

## Animation classes

The animation process in Matplotlib can be thought of in 2 different ways:

`FuncAnimation`: Generate data for first frame and then modify this data for each frame to create an animated plot.

`ArtistAnimation`: Generate a list (iterable) of artists that will draw in each frame in the animation.

`FuncAnimation` is more efficient in terms of speed and memory as it draws an artist once and then modifies it. 
On the other hand `ArtistAnimation` is flexible as it allows any iterable of artists to be animated in a sequence.

## `FuncAnimation`


```python
fig, ax = plt.subplots()
t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
z = g * t**2 / 2 + v0 * t

v02 = 5
z2 = g * t**2 / 2 + v02 * t

scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()


def update(frame):
    # for each frame, update the data stored on each artist.
    x = t[:frame]
    y = z[:frame]
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    # update the line plot:
    line2.set_xdata(t[:frame])
    line2.set_ydata(z2[:frame])
    return (scat, line2)


ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
plt.show()
```


## `ArtistAnimation`


```python
fig, ax = plt.subplots()
rng = np.random.default_rng(19680801)
data = np.array([20, 20, 20, 20])
x = np.array([1, 2, 3, 4])

artists = []
colors = ['tab:blue', 'tab:red', 'tab:green', 'tab:purple']
for i in range(20):
    data += rng.integers(low=0, high=10, size=data.shape)
    container = ax.barh(x, data, color=colors)
    artists.append(container)


ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=400)
plt.show()
```



## Saving Animations

Pillow writers:

```python
ani.save(filename="/tmp/pillow_example.gif", writer="pillow")
ani.save(filename="/tmp/pillow_example.apng", writer="pillow")
```

HTML writers:

```python
ani.save(filename="/tmp/html_example.html", writer="html")
ani.save(filename="/tmp/html_example.htm", writer="html")
ani.save(filename="/tmp/html_example.png", writer="html")
```









## Credits

- [Animations using Matplotlib](https://matplotlib.org/stable/users/explain/animations/animations.html)