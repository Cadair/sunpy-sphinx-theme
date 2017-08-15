import numpy as np
import sunpy.data.sample
import sunpy.timeseries as ts

my_timeseries = ts.TimeSeries(sunpy.data.sample.GOES_XRS_TIMESERIES, source='XRS')
my_timeseries.peek()