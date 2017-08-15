import sunpy.map
import sunpy.data.sample

aia = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)
aia.peek()