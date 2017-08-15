import sunpy.data.sample
import sunpy.timeseries
norh = sunpy.timeseries.TimeSeries(sunpy.data.sample.NORH_TIMESERIES, source='NoRH')
norh.peek()