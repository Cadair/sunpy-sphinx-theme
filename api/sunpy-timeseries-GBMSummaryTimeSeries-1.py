import sunpy.timeseries
import sunpy.data.sample
gbm = sunpy.timeseries.TimeSeries(sunpy.data.sample.GBM_TIMESERIES, source='GBMSummary')
gbm.peek()