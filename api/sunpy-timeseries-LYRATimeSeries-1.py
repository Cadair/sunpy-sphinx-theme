import sunpy.timeseries
import sunpy.data.sample
lyra = sunpy.timeseries.TimeSeries(sunpy.data.sample.LYRA_LEVEL3_TIMESERIES, source='LYRA')
lyra.peek()