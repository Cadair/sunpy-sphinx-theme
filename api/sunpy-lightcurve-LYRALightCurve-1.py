import sunpy.lightcurve
from sunpy.data.sample import LYRA_LEVEL3_TIMESERIES
lyra = sunpy.lightcurve.LYRALightCurve.create(LYRA_LEVEL3_TIMESERIES)
lyra.peek()