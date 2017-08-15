import sunpy.data.sample
import sunpy.timeseries
rhessi = sunpy.timeseries.TimeSeries(sunpy.data.sample.RHESSI_TIMESERIES, source='RHESSI')
rhessi.peek()