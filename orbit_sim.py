from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np



G = 6.67430e-11
M = 1.989e30
M_earth = 5.972e24
dt = 60 * 60 * 2
steps = 1100000

earth_x_list = []
earth_y_list = []
mercury_x_list = []
mercury_y_list = []
venus_x_list = []
venus_y_list = []
moon_x_list = []
ganymede_x_list = []
ganymede_y_list = []
moon_y_list = []
mars_x_list = []
mars_y_list = []
jupiter_x_list = []
jupiter_y_list = []
pluto_x_list = []
pluto_y_list = []
saturn_x_list = []
saturn_y_list = []
titan_x_list = []
titan_y_list = []
uranus_x_list = []
uranus_y_list = []
neptune_x_list = []
neptune_y_list = []

anim = None
earth_pos = None
earth_vel = None
mercury_pos = None
mercury_vel = None
venus_pos = None
venus_vel = None
moon_pos = None
moon_vel = None
ganymede_pos = None
ganymede_vel = None
mars_pos = None
mars_vel = None
jupiter_pos = None
jupiter_vel = None
pluto_pos = None
pluto_vel = None
saturn_pos = None
saturn_vel = None
titan_pos = None
titan_vel = None
uranus_pos = None
uranus_vel = None
neptune_pos = None
neptune_vel = None

fig = plt.figure(figsize=(24, 16))
ax = fig.add_axes((0.325, 0.25, 0.4, 0.72))
ax.set_facecolor('black')
ax.set_title('Full Orbit Sim')

zoom_ax = plt.axes((0.18, 0.31, 0.12, 0.65))
zoom_slider = Slider(zoom_ax, label='Zoom', valmin=1e8, valmax=6e12, valinit=6e12, orientation='vertical')
def update_zoom(val):
    zoom_range = zoom_slider.val
    ax.set_xlim(-zoom_range, zoom_range)
    ax.set_ylim(-zoom_range, zoom_range)
    fig.canvas.draw_idle()
zoom_slider.on_changed(update_zoom)
ax.set_aspect('equal')
ax.set_xlim(-6e12, 6e12)
ax.set_ylim(-6e12, 6e12)



ax.scatter([0], [0], color='yellow', label='Star', s=250)
earth_line, = ax.plot([], [], color='lightgray', linestyle='--', label='Earth Orbit Path')
earth_dot, = ax.plot([], [], 'go', markersize=6)
moon_dot, = ax.plot([], [], 'mo', markersize=1.5)
moon_line, = ax.plot([], [], color='lightgray', linestyle='--', label='Moon Orbit Path')
mercury_dot, = ax.plot([], [], 'ro', markersize=2)
mercury_line, = ax.plot([], [], color='lightgray', linestyle='--', label='Mercury Orbit Path')
venus_dot, = ax.plot([], [], 'yo', markersize=5.8)
venus_line, = ax.plot([], [], color='lightgray', linestyle='--', label='Venus Orbit Path')
mars_dot, = ax.plot([], [], 'ro', markersize=3)
mars_line, = ax.plot([], [], color='lightgray', linestyle='--', label='Mars Orbit Path')
jupiter_dot, = ax.plot([], [], 'yo', markersize=10)
jupiter_line, = ax.plot([], [], color='lightgray', linestyle='--', label='Jupiter Orbit Path')
ganymede_dot, = ax.plot([], [], 'go', markersize=2.6)
ganymede_line, = ax.plot([], [], color='lightgray', linestyle='--')
pluto_dot, = ax.plot([], [], 'yo', markersize=5)
pluto_line, = ax.plot([], [], color='lightgray', linestyle='--')
saturn_dot, = ax.plot([], [], 'ro', markersize=9.5)
saturn_line, = ax.plot([], [], color='lightgray', linestyle='--')
titan_dot, = ax.plot([], [], 'bo', markersize=5.5)
titan_line, = ax.plot([], [], color='lightgray', linestyle='--')
uranus_dot, = ax.plot([], [], 'go', markersize=8)
uranus_line, = ax.plot([], [], color='lightgray', linestyle='--')
neptune_dot, = ax.plot([], [], 'bo', markersize=7.98)
neptune_line, = ax.plot([], [], color='lightgray', linestyle='--')

ax_slider = plt.axes((0.2, 0.01, 0.65, 0.015))
ax_slider2 = plt.axes((0.2, 0.02, 0.65, 0.015))
ax_slider3 = plt.axes((0.2, 0.03, 0.65, 0.015))
ax_slider4 = plt.axes((0.2, 0.04, 0.65, 0.015))
ax_slider5 = plt.axes((0.2, 0.05, 0.65, 0.015))
ax_slider6 = plt.axes((0.2, 0.06, 0.62, 0.015))
ax_slider7 = plt.axes((0.2, 0.07, 0.65, 0.015))
ax_slider8 = plt.axes((0.2, 0.08, 0.65, 0.015))
ax_slider9 = plt.axes((0.2, 0.09, 0.65, 0.015))
ax_slider10 = plt.axes((0.2, 0.1, 0.65, 0.015))
ax_slider11 = plt.axes((0.2, 0.11, 0.65, 0.015))
ax_slider12 = plt.axes((0.2, 0.12, 0.65, 0.015))
ax_slider13 = plt.axes((0.2, 0.13, 0.65, 0.015))
ax_slider14 = plt.axes((0.2, 0.14, 0.65, 0.015))
ax_slider15 = plt.axes((0.2, 0.15, 0.65, 0.015))
ax_slider16 = plt.axes((0.2, 0.16, 0.65, 0.015))
ax_slider17 = plt.axes((0.2, 0.17, 0.65, 0.015))
ax_slider18 = plt.axes((0.2, 0.18, 0.65, 0.015))
ax_slider19 = plt.axes((0.2, 0.19, 0.65, 0.015))
ax_slider20 = plt.axes((0.2, 0.20, 0.65, 0.015))
ax_slider21 = plt.axes((0.2, 0.21, 0.65, 0.015))
eth_velocity_slider = Slider(ax_slider2, 'Earth Velocity', 1e2, 1e5, valinit=30290)
eth_distance_slider = Slider(ax_slider, 'Earth Distance', 1e9, 6e12, valinit=1.471e11)
eth_mass_slider = Slider(ax_slider3, 'Earth Mass', 1e24, 8e25, valinit=5.972e24, valstep=1e22, valfmt='%1.3e')
mars_velocity_slider = Slider(ax_slider8, label='Mars Velocity', valmin=1e2, valmax=1e5, valinit=2.41e4)
mars_distance_slider = Slider(ax_slider9, label='Mars Distance', valmin=1e9, valmax=6e12, valinit=2.28e11)
mer_velocity_slider = Slider(ax_slider4, label='Mercury Velocity', valmin=1e2, valmax=1e5, valinit=4.736e4)
mer_distance_slider = Slider(ax_slider5, label='Mercury Distance', valmin=1e9, valmax=6e12, valinit=5.80e10)
ven_velocity_slider = Slider(ax_slider6, label='Venus Velocity', valmin=1e2, valmax=1e5, valinit=3.502e4)
ven_distance_slider = Slider(ax_slider7, label='Venus Distance', valmin=1e9, valmax=6e12, valinit=1.08e11)
jup_velocity_slider = Slider(ax_slider10, label='Jupiter Velocity', valmin=1e2, valmax=1e5, valinit=1.31e4)
jup_distance_slider = Slider(ax_slider11, label='Jupiter Distance', valmin=1e9, valmax=6e12, valinit=7.785e11)
jup_mass_slider = Slider(ax_slider12, label='Jupiter Mass', valmin=1e26, valmax=1e28, valinit=1.898e27)
pluto_velocity_slider = Slider(ax_slider13, label='Pluto Velocity', valmin=1e2, valmax=1e5, valinit=4.74e3)
pluto_distance_slider = Slider(ax_slider14, label='Pluto Distance', valmin=1e9, valmax=6e12, valinit=5.9e12)
sat_distance_slider = Slider(ax_slider15, label='Saturn Distance', valmin=1e9, valmax=6e12, valinit=1.429e12)
sat_velocity_slider = Slider(ax_slider16, label='Saturn Velocity', valmin=1e2, valmax=1e5, valinit=9.68e3)
sat_mass_slider = Slider(ax_slider17, label='Saturn Mass', valmin=1e26, valmax=1e27, valinit=5.683e26)
uran_distance_slider = Slider(ax_slider18, label='Uranus Distance', valmin=1e9, valmax=6e12, valinit=2.871e12)
uran_velocity_slider = Slider(ax_slider19, label='Uranus Velocity', valmin=1e2, valmax=1e5, valinit=6.8e3)
nep_distance_slider = Slider(ax_slider20, label='Neptune Distance', valmin=1e9, valmax=6e12, valinit=4.495e12)
nep_velocity_slider = Slider(ax_slider21, label='Neptune Velocity', valmin=1e2, valmax=1e5, valinit=5.43e3)




def generate_orbit(eth_distance, eth_velocity, eth_mass, mer_distance, mer_velocity, ven_distance, ven_velocity, mars_distance, mars_velocity,
    jup_distance, jup_velocity, jup_mass, plu_distance, plu_velocity, sat_distance, sat_velocity, sat_mass, uran_distance, uran_velocity, nep_distance, nep_velocity
                   ):
    global earth_pos, earth_vel, mercury_pos, mercury_vel, venus_pos, venus_vel, moon_pos, moon_vel, moon_x_list, moon_y_list, mars_pos, mars_vel, \
    jupiter_pos, jupiter_vel, pluto_pos, pluto_vel, ganymede_pos, ganymede_vel, ganymede_x_list, ganymede_y_list, saturn_pos, saturn_vel, titan_pos, titan_vel, \
    titan_x_list, titan_y_list, uranus_pos, uranus_vel, neptune_pos, neptune_vel

    earth_pos = np.array([eth_distance, 0.0])
    earth_vel = np.array([0.0, eth_velocity])
    mercury_pos = np.array([mer_distance, 0.0])
    mercury_vel = np.array([0.0, mer_velocity])
    venus_pos = np.array([ven_distance, 0.0])
    venus_vel = np.array([0.0, ven_velocity])
    mars_pos = np.array([mars_distance, 0.0])
    mars_vel = np.array([0.0, mars_velocity])
    jupiter_pos = np.array([jup_distance, 0.0])
    jupiter_vel = np.array([0.0, jup_velocity])
    pluto_pos = np.array([plu_distance, 0.0])
    pluto_vel = np.array([0.0, plu_velocity])
    moon_pos = earth_pos + np.array([3.484e8, 0.0])
    moon_vel = earth_vel + np.array([0.0, 1022.0])
    ganymede_pos = jupiter_pos + np.array([1.07e9, 0.0])
    ganymede_vel = jupiter_vel + np.array([0.0, 1.088e4])
    saturn_pos = np.array([sat_distance, 0.0])
    saturn_vel = np.array([0.0, sat_velocity])
    titan_pos = saturn_pos + np.array([1.222e9, 0.0])
    titan_vel = saturn_vel + np.array([0.0, 5.57e3])
    uranus_pos = np.array([uran_distance, 0.0])
    uranus_vel = np.array([0.0, uran_velocity])
    neptune_pos = np.array([nep_distance, 0.0])
    neptune_vel = np.array([0.0, nep_velocity])
    earth_xs, earth_ys = [], []
    moon_xs, moon_ys = [], []
    ganymede_xs, ganymede_ys = [], []
    mercury_xs, mercury_ys = [], []
    venus_xs, venus_ys = [], []
    mars_xs, mars_ys = [], []
    jupiter_xs, jupiter_ys = [], []
    pluto_xs, pluto_ys = [], []
    saturn_xs, saturn_ys = [], []
    titan_xs, titan_ys = [], []
    uranus_xs, uranus_ys = [], []
    neptune_xs, neptune_ys = [], []
    store_every = 1500
    for step in range(steps):
        r_earth = np.linalg.norm(earth_pos)
        acc_earth = -G * M * earth_pos / r_earth ** 3
        earth_vel += acc_earth * dt
        earth_pos += earth_vel * dt
        earth_xs.append(earth_pos[0])
        earth_ys.append(earth_pos[1])
        r_mercury = np.linalg.norm(mercury_pos)
        acc_mercury = -G * M * mercury_pos / r_mercury ** 3
        mercury_vel += acc_mercury * dt
        mercury_pos += mercury_vel * dt
        mercury_xs.append(mercury_pos[0])
        mercury_ys.append(mercury_pos[1])
        r_venus = np.linalg.norm(venus_pos)
        acc_venus = -G * M * venus_pos / r_venus ** 3
        venus_vel += acc_venus * dt
        venus_pos += venus_vel * dt
        venus_xs.append(venus_pos[0])
        venus_ys.append(venus_pos[1])
        r_mars = np.linalg.norm(mars_pos)
        acc_mars = -G * M * mars_pos / r_mars ** 3
        mars_vel += acc_mars * dt
        mars_pos += mars_vel * dt
        mars_xs.append(mars_pos[0])
        mars_ys.append(mars_pos[1])
        r_jupiter = np.linalg.norm(jupiter_pos)
        acc_jupiter = -G * M * jupiter_pos / r_jupiter ** 3
        jupiter_vel += acc_jupiter * dt
        jupiter_pos += jupiter_vel * dt
        jupiter_xs.append(jupiter_pos[0])
        jupiter_ys.append(jupiter_pos[1])
        r_pluto = np.linalg.norm(pluto_pos)
        acc_pluto = -G * M * pluto_pos / r_pluto ** 3
        pluto_vel += acc_pluto * dt
        pluto_pos += pluto_vel * dt
        pluto_xs.append(pluto_pos[0])
        pluto_ys.append(pluto_pos[1])
        r_saturn = np.linalg.norm(saturn_pos)
        acc_saturn = -G * M * saturn_pos / r_saturn ** 3
        saturn_vel += acc_saturn * dt
        saturn_pos += saturn_vel * dt
        saturn_xs.append(saturn_pos[0])
        saturn_ys.append(saturn_pos[1])
        r_uranus = np.linalg.norm(uranus_pos)
        acc_uranus = -G * M * uranus_pos / r_uranus ** 3
        uranus_vel += acc_uranus * dt
        uranus_pos += uranus_vel * dt
        uranus_xs.append(uranus_pos[0])
        uranus_ys.append(uranus_pos[1])
        r_neptune = np.linalg.norm(neptune_pos)
        acc_neptune = -G * M * neptune_pos / r_neptune ** 3
        neptune_vel += acc_neptune * dt
        neptune_pos += neptune_vel * dt
        neptune_xs.append(neptune_pos[0])
        neptune_ys.append(neptune_pos[1])
        r_moon_sun = moon_pos
        r_moon_earth = moon_pos - earth_pos
        acc_moon = (
                -G * M * r_moon_sun / np.linalg.norm(r_moon_sun) ** 3 +
                -G * eth_mass * r_moon_earth / np.linalg.norm(r_moon_earth) ** 3
        )
        moon_vel += acc_moon * dt
        moon_pos += moon_vel * dt
        moon_xs.append(moon_pos[0])
        moon_ys.append(moon_pos[1])
        r_ganymede_sun = ganymede_pos
        r_ganymede_jupiter = ganymede_pos - jupiter_pos
        acc_ganymede = (
                -G * M * r_ganymede_sun / np.linalg.norm(r_ganymede_sun) ** 3 +
                -G * jup_mass * r_ganymede_jupiter / np.linalg.norm(r_ganymede_jupiter) ** 3
        )
        ganymede_vel += acc_ganymede * dt
        ganymede_pos += ganymede_vel * dt
        ganymede_xs.append(ganymede_pos[0])
        ganymede_ys.append(ganymede_pos[1])
        r_titan_sun = titan_pos
        r_titan_saturn = titan_pos - saturn_pos
        acc_titan = (
            -G * M * r_titan_sun / np.linalg.norm(r_titan_sun) ** 3 +
            -G * sat_mass * r_titan_saturn / np.linalg.norm(r_titan_saturn) ** 3
        )
        titan_vel += acc_titan * dt
        titan_pos += titan_vel * dt
        titan_xs.append(titan_pos[0])
        titan_ys.append(titan_pos[1])

        if step % store_every == 0:
            earth_xs.append(earth_pos[0])
            earth_ys.append(earth_pos[1])
            mercury_xs.append(mercury_pos[0])
            mercury_ys.append(mercury_pos[1])
            venus_xs.append(venus_pos[0])
            venus_ys.append(venus_pos[1])
            mars_xs.append(mars_pos[0])
            mars_ys.append(mars_pos[1])
            jupiter_xs.append(jupiter_pos[0])
            jupiter_ys.append(jupiter_pos[1])
            saturn_xs.append(saturn_pos[0])
            saturn_ys.append(saturn_pos[1])
            pluto_xs.append(pluto_pos[0])
            pluto_ys.append(pluto_pos[1])
            moon_xs.append(moon_pos[0])
            moon_ys.append(moon_pos[1])
            ganymede_xs.append(ganymede_pos[0])
            ganymede_ys.append(ganymede_pos[1])
            titan_xs.append(titan_pos[0])
            titan_ys.append(titan_pos[1])
            uranus_xs.append(uranus_pos[0])
            uranus_ys.append(uranus_pos[1])
            neptune_xs.append(neptune_pos[0])
            neptune_ys.append(neptune_pos[1])
        moon_x_list = moon_xs
        moon_y_list = moon_ys
        ganymede_x_list = ganymede_xs
        ganymede_y_list = ganymede_ys
        titan_x_list = titan_xs
        titan_y_list = titan_ys
    return (earth_xs, earth_ys, mercury_xs, mercury_ys, venus_xs, venus_ys, mars_xs, mars_ys, jupiter_xs, jupiter_ys, pluto_xs, pluto_ys, saturn_xs, saturn_ys,
    uranus_xs, uranus_ys, neptune_xs, neptune_ys
            )

def animate(i):
    if i < len(earth_x_list):
        earth_dot.set_data([earth_x_list[i]], [earth_y_list[i]])
        mercury_dot.set_data([mercury_x_list[i]], [mercury_y_list[i]])
        venus_dot.set_data([venus_x_list[i]], [venus_y_list[i]])
        moon_dot.set_data([moon_x_list[i]], [moon_y_list[i]])
        mars_dot.set_data([mars_x_list[i]], [mars_y_list[i]])
        jupiter_dot.set_data([jupiter_x_list[i]], [jupiter_y_list[i]])
        ganymede_dot.set_data([ganymede_x_list[i]], [ganymede_y_list[i]])
        pluto_dot.set_data([pluto_x_list[i]], [pluto_y_list[i]])
        saturn_dot.set_data([saturn_x_list[i]], [saturn_y_list[i]])
        titan_dot.set_data([titan_x_list[i]], [titan_y_list[i]])
        uranus_dot.set_data([uranus_x_list[i]], [uranus_y_list[i]])
        neptune_dot.set_data([neptune_x_list[i]], [neptune_y_list[i]])

    return (earth_dot, mercury_dot, venus_dot, moon_dot, mars_dot, jupiter_dot, ganymede_dot, pluto_dot, saturn_dot, titan_dot, uranus_dot, neptune_dot)

def update_slider(val):
    global earth_x_list, earth_y_list, mercury_x_list, mercury_y_list, venus_x_list, venus_y_list, mars_x_list, mars_y_list, \
        jupiter_x_list, jupiter_y_list, anim, M_earth, pluto_x_list, pluto_y_list, saturn_x_list, saturn_y_list, uranus_x_list, uranus_y_list, neptune_x_list, neptune_y_list
    eth_distance = eth_distance_slider.val
    eth_velocity = eth_velocity_slider.val
    mer_distance = mer_distance_slider.val
    mer_velocity = mer_velocity_slider.val
    ven_distance = ven_distance_slider.val
    ven_velocity = ven_velocity_slider.val
    mars_distance = mars_distance_slider.val
    mars_velocity = mars_velocity_slider.val
    jup_distance = jup_distance_slider.val
    jup_velocity = jup_velocity_slider.val
    plu_distance = pluto_distance_slider.val
    plu_velocity = pluto_velocity_slider.val
    jup_mass = jup_mass_slider.val
    eth_mass = eth_mass_slider.val
    sat_distance = sat_distance_slider.val
    sat_velocity = sat_velocity_slider.val
    sat_mass = sat_mass_slider.val
    uran_distance = uran_distance_slider.val
    uran_velocity = uran_velocity_slider.val
    nep_distance = nep_distance_slider.val
    nep_velocity = nep_velocity_slider.val
    (earth_x_list, earth_y_list, mercury_x_list, mercury_y_list, venus_x_list, venus_y_list, mars_x_list, mars_y_list,
     jupiter_x_list, jupiter_y_list, pluto_x_list, pluto_y_list, saturn_x_list, saturn_y_list, uranus_x_list, uranus_y_list, neptune_x_list, neptune_y_list) = generate_orbit(eth_distance, eth_velocity, eth_mass,
    mer_distance, mer_velocity, ven_distance, ven_velocity, mars_distance, mars_velocity, jup_distance, jup_velocity, jup_mass, plu_distance, plu_velocity,
    sat_distance, sat_velocity, sat_mass, uran_distance, uran_velocity, nep_distance, nep_velocity
    )

    earth_line.set_data(earth_x_list, earth_y_list)
    moon_line.set_data(moon_x_list, moon_y_list)
    mercury_line.set_data(mercury_x_list, mercury_y_list)
    venus_line.set_data(venus_x_list, venus_y_list)
    mars_line.set_data(mars_x_list, mars_y_list)
    jupiter_line.set_data(jupiter_x_list, jupiter_y_list)
    ganymede_line.set_data(ganymede_x_list, ganymede_y_list)
    pluto_line.set_data(pluto_x_list, pluto_y_list)
    saturn_line.set_data(saturn_x_list, saturn_y_list)
    titan_line.set_data(titan_x_list, titan_y_list)
    uranus_line.set_data(uranus_x_list, uranus_y_list)
    neptune_line.set_data(neptune_x_list, neptune_y_list)


    if earth_x_list and earth_y_list and mercury_x_list and mercury_y_list and venus_x_list and venus_y_list and mars_y_list and mars_y_list and jupiter_x_list and jupiter_y_list and pluto_x_list and pluto_y_list and saturn_x_list and saturn_y_list and uranus_x_list and uranus_y_list and neptune_x_list and neptune_y_list:
        earth_dot.set_data([earth_x_list[0]], [earth_y_list[0]])
        mercury_dot.set_data([mercury_x_list[0]], [mercury_y_list[0]])
        venus_dot.set_data([venus_x_list[0]], [venus_y_list[0]])
        mars_dot.set_data([mars_x_list[0]], [mars_y_list[0]])
        jupiter_dot.set_data([jupiter_x_list[0]], [jupiter_y_list[0]])
        pluto_dot.set_data([pluto_x_list[0]], [pluto_y_list[0]])
        saturn_dot.set_data([saturn_x_list[0]], [saturn_y_list[0]])
        uranus_dot.set_data([uranus_x_list[0]], [uranus_y_list[0]])
        neptune_dot.set_data([neptune_x_list[0]], [neptune_y_list[0]])


    if anim:
        anim.event_source.stop()

    anim = FuncAnimation(fig, animate, frames=len(earth_x_list), interval=10, blit=True, repeat=False)
    fig.canvas.draw_idle()


eth_distance_slider.on_changed(update_slider)
eth_velocity_slider.on_changed(update_slider)
eth_mass_slider.on_changed(update_slider)
mer_velocity_slider.on_changed(update_slider)
mer_distance_slider.on_changed(update_slider)
ven_velocity_slider.on_changed(update_slider)
ven_distance_slider.on_changed(update_slider)
mars_distance_slider.on_changed(update_slider)
mars_velocity_slider.on_changed(update_slider)
jup_distance_slider.on_changed(update_slider)
jup_mass_slider.on_changed(update_slider)
jup_velocity_slider.on_changed(update_slider)
pluto_distance_slider.on_changed(update_slider)
pluto_velocity_slider.on_changed(update_slider)
sat_distance_slider.on_changed(update_slider)
sat_velocity_slider.on_changed(update_slider)
sat_mass_slider.on_changed(update_slider)
uran_distance_slider.on_changed(update_slider)
uran_velocity_slider.on_changed(update_slider)
nep_distance_slider.on_changed(update_slider)
nep_velocity_slider.on_changed(update_slider)

update_slider(None)
plt.legend()
plt.show()



