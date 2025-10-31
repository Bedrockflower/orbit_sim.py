from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

G = 6.67430e-11
earth_mass = 5.972e24
dt = 60 * 60
steps = 100000

moon_x_list = []
moon_y_list = []
anim = None
moon_pos = None
moon_vel = None

fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.set_size_inches(12, 8)
plt.subplots_adjust(bottom=0.25)
ax.set_aspect('equal')
ax.set_xlim(-6e8, 6e8)
ax.set_ylim(-6e8, 6e8)
ax.set_title("Moon Orbit Simulator")

ax.scatter([0], [0], color='blue', label='Earth', s=1091.78)
moon_dot, = ax.plot([], [], 'ro', markersize=10)
moon_line, = ax.plot([], [], color='lightgray', linestyle='--', label='Moon Orbit Path')

ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
ax_slider2 = plt.axes([0.2, 0.05, 0.65, 0.03])
ax_slider3 = plt.axes([0.2, 0.01, 0.65, 0.03])
velocity_slider = Slider(ax_slider2, 'Velocity', 1e2, 1e4, valinit=1.02e3)
distance_slider = Slider(ax_slider, 'Distance', 1e7, 1e9, valinit=3.844e8)
earth_mass_slider = Slider(ax_slider3, 'Mass', 1e24, 8e25, valinit=5.972e24, valstep=1e22,
    valfmt='%1.3e'
)



def generate_orbit(distance, velocity, earth_mass):
    global moon_pos, moon_vel
    moon_pos = np.array([distance, 0.0])
    moon_vel = np.array([0.0, velocity])
    moon_xs, moon_ys = [], []
    for _ in range(steps):
        r_moon = np.linalg.norm(moon_pos)
        acc_moon = -G * earth_mass * moon_pos / r_moon ** 3
        moon_vel += acc_moon * dt
        moon_pos += moon_vel * dt
        moon_xs.append(moon_pos[0])
        moon_ys.append(moon_pos[1])
    return moon_xs, moon_ys


def animate(i):
    if i < len(moon_x_list):
        moon_line.set_data(moon_x_list[:i], moon_y_list[:i])
        moon_dot.set_data([moon_x_list[i]], [moon_y_list[i]])
    return moon_line, moon_dot


def update_slider(val):
    global moon_x_list, moon_y_list, anim, earth_mass
    distance = distance_slider.val
    velocity = velocity_slider.val
    earth_mass = earth_mass_slider.val
    moon_x_list, moon_y_list = generate_orbit(distance, velocity, earth_mass)

    moon_line.set_data(moon_x_list, moon_y_list)

    if moon_x_list and moon_y_list:
        moon_dot.set_data([moon_x_list[0]], [moon_y_list[0]])

    if anim:
        anim.event_source.stop()

    anim = FuncAnimation(fig, animate, frames=len(moon_x_list), interval=10, blit=True, repeat=False)
    fig.canvas.draw_idle()


distance_slider.on_changed(update_slider)
velocity_slider.on_changed(update_slider)
earth_mass_slider.on_changed(update_slider)


update_slider(None)
plt.legend()
plt.show()

import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(16, 8))

# Left axis - full solar system
ax = fig.add_axes([0.35, 0.25, 0.42, 0.7])  # left, bottom, width, height
ax.set_facecolor("black")
ax.set_title("Full Planet Orbit Simulator")

zoom_ax = plt.axes([0.2, 0.19, 0.65, 0.015])
zoom_slider = Slider(zoom_ax, 'Zoom', 1e10, 9e11, valinit=9e11)

def update_zoom(val):
    zoom_range = zoom_slider.val
    ax.set_xlim(-zoom_range, zoom_range)
    ax.set_ylim(-zoom_range, zoom_range)
    fig.canvas.draw_idle()

zoom_slider.on_changed(update_zoom)

