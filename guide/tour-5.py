import sunpy.map
import matplotlib.pyplot as plt
import sunpy.data.sample

aia = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)

fig = plt.figure()
ax = plt.subplot(111, projection=aia)

aia.plot()
aia.draw_limb()
aia.draw_grid()
aia.draw_limb()
plt.colorbar()

plt.show()