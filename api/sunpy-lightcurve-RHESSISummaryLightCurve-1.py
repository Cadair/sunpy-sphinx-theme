from sunpy import lightcurve as lc
from sunpy.data.sample import RHESSI_TIMESERIES
rhessi = lc.RHESSISummaryLightCurve.create(RHESSI_TIMESERIES)
rhessi.peek()