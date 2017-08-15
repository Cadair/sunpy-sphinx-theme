import sunpy.map
import sunpy.data.sample
import matplotlib.pyplot as plt
smap = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)
fig = plt.figure()
smap.plot(cmap=plt.cm.Greys_r)
plt.colorbar()
plt.show()