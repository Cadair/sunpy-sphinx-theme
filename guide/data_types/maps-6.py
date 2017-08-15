import sunpy.map
import matplotlib.pyplot as plt
import sunpy.data.sample
smap = sunpy.map.Map(sunpy.data.sample.AIA_193_CUTOUT01_IMAGE)
txt = "min={min}, max={max}, $\mu$={mean}, $\sigma$={std}".format(min=int(smap.min()),
                                                                  max=int(smap.max()),
                                                                  mean=int(smap.mean()),
                                                                  std=int(smap.std()))
plt.text(-1100, 0, txt, color='white')
smap.plot()
plt.colorbar()
plt.show()