import matplotlib.pyplot as plt
import sunpy.spectra
import sunpy.data.sample
from sunpy.spectra.sources.callisto import CallistoSpectrogram
image = CallistoSpectrogram.read(sunpy.data.sample.CALLISTO_SPECTRUM)
image.peek()