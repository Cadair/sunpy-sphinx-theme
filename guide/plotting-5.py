import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import SkyCoord

import sunpy.map
import sunpy.data.sample

smap = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)

fig = plt.figure()
# Provide the Map as a projection, which creates a WCSAxes object
ax = plt.subplot(projection=smap)

im = smap.plot()

# Prevent the image from being re-scaled while overplotting.
ax.set_autoscale_on(False)

xc = [0,100,1000] * u.arcsec
yc = [0,100,1000] * u.arcsec

coords = SkyCoord(xc, yc, frame=smap.coordinate_frame)

p = ax.plot_coord(coords, 'o')

# Set title.
ax.set_title('Custom plot with WCSAxes')

plt.colorbar()
plt.show()