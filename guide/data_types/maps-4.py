import sunpy.map
import sunpy.data.sample
import matplotlib.pyplot as plt

smap = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)
cmap = plt.get_cmap('sohoeit171')

fig = plt.figure()
ax = plt.subplot(1,1,1)
smap.plot(cmap=cmap)
plt.colorbar()
plt.show()