import sunpy.timeseries
import sunpy.data.sample
noaa = sunpy.timeseries.TimeSeries(sunpy.data.sample.NOAAPREDICT_TIMESERIES, source='NOAAPredictIndices')
noaa.peek()