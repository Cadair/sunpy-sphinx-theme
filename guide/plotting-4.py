import matplotlib.pyplot as plt
import astropy.units as u

import sunpy.map
import sunpy.data.sample

aia_map = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)
aia_map.plot()
aia_map.draw_limb()

# let's add contours as well
aia_map.draw_contours([10,20,30,40,50,60,70,80,90] * u.percent)

plt.colorbar()
plt.show()