from sunpy.spectra.spectrum import Spectrum
import numpy as np
spec = Spectrum(np.linspace(1, 100, 100), np.linspace(0, 10, 100))
spec.peek()