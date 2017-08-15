import matplotlib.pyplot as plt
import sunpy
import sunpy.data.sample
from sunpy.spectra.sources.callisto import CallistoSpectrogram
image = CallistoSpectrogram.read(sunpy.data.sample.CALLISTO_SPECTRUM)
nobg = image.subtract_bg()
interesting = nobg.in_interval("06:27")
interesting.peek(vmin=0)