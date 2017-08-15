import sunpy.map
import sunpy.data.sample
import matplotlib.pyplot as plt
import matplotlib.colors as colors

smap = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
smap.plot(norm=colors.Normalize())
plt.colorbar()
ax2 = fig.add_subplot(2,1,2)
smap.plot(norm=colors.LogNorm())
fig.subplots_adjust(hspace=0.4)
plt.colorbar()
plt.show()