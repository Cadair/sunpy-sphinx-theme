from sunpy import lightcurve as lc
from sunpy.data.sample import GOES_XRS_TIMESERIES
goes = lc.GOESLightCurve.create(GOES_XRS_TIMESERIES)
goes.peek()