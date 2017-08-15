import sunpy.lightcurve
from sunpy.data.sample import EVE_TIMESERIES
eve = sunpy.lightcurve.EVELightCurve.create(EVE_TIMESERIES)
eve.peek(subplots=True)