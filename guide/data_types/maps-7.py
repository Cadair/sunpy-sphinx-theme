import sunpy.map
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import sunpy.data.sample
smap = sunpy.map.Map(sunpy.data.sample.AIA_193_CUTOUT01_IMAGE)
cmap = smap.plot_settings['cmap']
cmap.set_over('blue', 1.0)
cmap.set_under('purple', 1.0)
norm = colors.Normalize(vmin=0, vmax=smap.mean() + 5 * smap.std())
smap.plot(norm=norm)
plt.colorbar(extend='both')
plt.show()