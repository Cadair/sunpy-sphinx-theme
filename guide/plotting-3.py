import sunpy.map
import sunpy.data.sample
smap = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)
smap.peek(draw_limb=True)