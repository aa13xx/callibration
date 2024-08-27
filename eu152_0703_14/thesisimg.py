import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

import sys
#other file
from resolution_eu152_0703_14 import fit_a, fit_b, fit_c
from openmc_extract_eu152_0703_14 import df_openmc, energy
from data_extract_eu152_0703_14 import df_data, isotope
from functions import broad_spectrum, sci_notation, background, findpeakarea, peakfinder, peakleftwin, peakrightwin, peakleft, peakright

renorm_broadened_spectrum = broad_spectrum(df_openmc.intensity.to_numpy(), energy, sum(df_openmc.intensity), fit_a, fit_b, fit_c)

plt.figure(1)

plt.vlines(x=121.7817, color="red", ls =':', label="121.8 kev", ymin = 0, ymax=1e6)
#plt.vlines(x=344.2785, color="red", ls =':', label="344.3 kev", ymin = 0, ymax=1e6)
#plt.vlines(x=778.9045, color="red", ls =':', label="778.9 kev", ymin = 0, ymax=1e6)
plt.vlines(x=964.057, color="red", ls =':', label="964.1 kev", ymin = 0, ymax=1e6)
#plt.vlines(x=1085.837, color="red", ls =':', label="1086 kev", ymin = 0, ymax=1e6)
#plt.vlines(x=1112.076, color="red", ls =':', label="1112 kev", ymin = 0, ymax=1e6)
#plt.vlines(x=1408.013, color="red", ls =':', label="1408 kev", ymin = 0, ymax=1e6)

#plt.semilogy(df_openmc.energy, df_openmc.intensity, label="original simulation", color="crimson", alpha=0.2)
plt.semilogy(df_data.energy, df_data.intensity, label="experimental", color="steelblue", alpha=1)
#plt.semilogy(df_openmc.energy, renorm_broadened_spectrum, label="post processed simulation", color="crimson", alpha=0.5)

plt.legend()
#plt.xlim(955,972)
plt.xlim(0,1500)
plt.xlabel('Energy [keV]')
plt.ylabel('Intensity')
plt.title(f"Experimental Data - {isotope}")
plt.minorticks_on()
plt.grid(True)
plt.tight_layout()
plt.savefig(f"plots_{isotope}/" + f"data_twopeaks_callibration.png")