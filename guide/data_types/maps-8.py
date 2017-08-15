import sunpy.data.sample
import sunpy.map
import matplotlib.pyplot as plt
my_maps = sunpy.map.Map(sunpy.data.sample.EIT_195_IMAGE, sunpy.data.sample.RHESSI_IMAGE, composite=True)
my_maps.add_map(sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE))
my_maps.set_alpha(2, 0.5)
my_maps.set_levels(1, [50, 60, 70, 80, 90], percent = True)
my_maps.plot()
plt.show()