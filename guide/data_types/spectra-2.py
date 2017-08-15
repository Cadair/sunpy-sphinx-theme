from matplotlib import pyplot as plt
import sunpy
import sunpy.data.sample
from sunpy.spectra.sources.callisto import CallistoSpectrogram
image = CallistoSpectrogram.read(sunpy.data.sample.CALLISTO_SPECTRUM)
nobg = image.subtract_bg()
nobg.peek(vmin=0)