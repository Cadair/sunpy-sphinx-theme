from sunpy import lightcurve as lc
from sunpy.data.sample import NORH_TIMESERIES
norh = lc.NoRHLightCurve.create(NORH_TIMESERIES)
norh.peek()