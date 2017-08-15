import sunpy.timeseries
import sunpy.data.sample
ts_goes = sunpy.timeseries.TimeSeries(sunpy.data.sample.GOES_XRS_TIMESERIES, source='XRS')
ts_goes.peek()