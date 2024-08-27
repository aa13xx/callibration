#package
import numpy as np
import pandas
from decimal import Decimal
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from scipy.optimize import curve_fit

import sys
#other files
from data_extract_eu152_0703_14 import df_data, isotope, bin_no, energy_data
from functions import FWHM, peakfinder

#extract peakfinder results (peak energy, peak energy range)
peakfinder_prominence = 500
peak_energy_arr = peakfinder(df_data,peakfinder_prominence)[0]
identified_peak_range = peakfinder(df_data,peakfinder_prominence)[1]

#array of peak's fwhm
peak_fwhm_arr = []
for i,j in identified_peak_range:
        peak_fwhm_arr.append(FWHM(df_data,i,j))

peak_resolution_arr = peak_fwhm_arr / peak_energy_arr
print(peak_energy_arr)
print(peak_fwhm_arr)
print(peak_resolution_arr)

#curve fit to find the resolution function
def resolution_fx(energy, a, b, c):
    fwhm = a + (b * ((energy + (c * (energy ** 2)))**0.5))
    return(fwhm)

parameters, covariance = curve_fit(resolution_fx, peak_energy_arr, peak_fwhm_arr)
#parameters in the gaussian function
fit_a = parameters[0]
fit_b = parameters[1]
fit_c = parameters[2]
print(fit_a)
print(fit_b)
print(fit_c)

#plotting the resolution curve vs fwhm graph
x = np.linspace(energy_data[0], energy_data[bin_no - 1], bin_no)
y = resolution_fx(x, fit_a, fit_b, fit_c)

plt.figure(0)
plt.plot(peak_energy_arr, peak_fwhm_arr, color="steelblue")
plt.plot(x, y, color="red")
plt.xlim(0,1650)
plt.xlabel('Energy [keV]')
plt.ylabel('Full Width Half Maximum [keV]')
plt.title("Detector FWHM Curve Obtained from Experimental Data")
plt.grid(True)
plt.minorticks_on()
plt.tight_layout()
plt.savefig(f"plots_{isotope}" + f"/exp_detector_fwhm.png")

plt.figure(1)
plt.plot(peak_energy_arr, peak_resolution_arr, color="steelblue")
plt.xlim(0,1650)
plt.xlabel('Energy [keV]')
plt.ylabel('Resolution')
plt.title("Detector Resolution Obtained from Experimental Data")
plt.grid(True)
plt.minorticks_on()
plt.tight_layout()
plt.savefig(f"plots_{isotope}" + f"/exp_detector_resolution.png")
