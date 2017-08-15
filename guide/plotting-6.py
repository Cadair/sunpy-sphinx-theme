import matplotlib.pyplot as plt
import astropy.units as u

import sunpy.map
import sunpy.data.sample

smap = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)

fig, ax = plt.subplots()

im = smap.plot()

# Prevent the image from being re-scaled while overplotting.
ax.set_autoscale_on(False)

xc = [0,100,1000] * u.arcsec
yc = [0,100,1000] * u.arcsec

p = plt.plot(xc, yc, 'o')

# Set title.
ax.set_title('Custom plot without WCSAxes')

plt.colorbar()
plt.show()