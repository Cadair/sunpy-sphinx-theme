from sunpy.lightcurve import GBMSummaryLightCurve
from sunpy.data.sample import GBM_TIMESERIES
gbm = GBMSummaryLightCurve.create(GBM_TIMESERIES)
gbm.peek()