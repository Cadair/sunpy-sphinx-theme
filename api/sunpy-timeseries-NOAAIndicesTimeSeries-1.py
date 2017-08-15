import sunpy.timeseries
import sunpy.data.sample
noaa = sunpy.timeseries.TimeSeries(sunpy.data.sample.NOAAINDICES_TIMESERIES, source='NOAAIndices')
noaa.peek()