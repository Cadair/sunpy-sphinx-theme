import sunpy.timeseries
from sunpy.data.sample import EVE_TIMESERIES
eve = sunpy.timeseries.TimeSeries(EVE_TIMESERIES, source='eve')
eve.peek(subplots=True)