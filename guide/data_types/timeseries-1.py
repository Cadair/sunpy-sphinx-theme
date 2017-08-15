import sunpy.timeseries as ts
import sunpy.data.sample
ts_plot = ts.TimeSeries(sunpy.data.sample.GOES_XRS_TIMESERIES, source='XRS')
fig = ts_plot.peek()