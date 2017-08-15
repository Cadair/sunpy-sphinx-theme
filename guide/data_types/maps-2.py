import sunpy.map
import sunpy.data.sample
import matplotlib.pyplot as plt
smap = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)
smap.plot_settings['title'] = "My Second SunPy Plot"
smap.plot_settings['cmap'] = plt.cm.Blues_r
fig = plt.figure()
smap.plot()
plt.colorbar()
plt.show()