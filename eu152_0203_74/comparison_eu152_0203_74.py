import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

#other file
from resolution_eu152_0203_74 import fit_a, fit_b, fit_c
from openmc_extract_eu152_0203_74 import df_openmc, energy
from data_extract_eu152_0203_74 import df_data, isotope
from functions import broad_spectrum, sci_notation, background, findpeakarea, peakfinder, peakleftwin, peakrightwin, peakleft, peakright

renorm_broadened_spectrum = broad_spectrum(df_openmc.intensity.to_numpy(), energy, sum(df_openmc.intensity), fit_a, fit_b, fit_c)

plt.figure(2)

#plt.vlines(x=121.7817, color="red", ls =':', label="121.8 kev", ymin = 0, ymax=1e6)
#plt.vlines(x=344.2785, color="red", ls =':', label="344.3 kev", ymin = 0, ymax=1e6)
#plt.vlines(x=778.9045, color="red", ls =':', label="778.9 kev", ymin = 0, ymax=1e6)
#plt.vlines(x=964.057, color="red", ls =':', label="964.1 kev", ymin = 0, ymax=1e6)
#plt.vlines(x=1085.837, color="red", ls =':', label="1086 kev", ymin = 0, ymax=1e6)
#plt.vlines(x=1112.076, color="red", ls =':', label="1112 kev", ymin = 0, ymax=1e6)
#plt.vlines(x=1408.013, color="red", ls =':', label="1408 kev", ymin = 0, ymax=1e6)

plt.semilogy(df_openmc.energy, df_openmc.intensity, label="original simulation", color="black", alpha=0.8)
#plt.semilogy(df_data.energy, df_data.intensity, label="experimental", color="steelblue", alpha=0.8)
plt.semilogy(df_openmc.energy, renorm_broadened_spectrum, label="post processed simulation", color="crimson", alpha=0.8)

plt.legend()
#plt.xlim(955,972)
plt.xlim(0,1500)
plt.xlabel('Energy [keV]')
plt.ylabel('Intensity')
#plt.title(f"{isotope}")
plt.minorticks_on()
plt.grid(True)
plt.tight_layout()
plt.savefig(f"plots_{isotope}/" + f"compare.png")

#plot 3 - peak compare
###344keV
est_peak_left = peakfinder(df_data,300)[1][13][0]
est_peak_right = peakfinder(df_data,300)[1][13][1]
###

baseline_val_data = background(df_data, est_peak_left, est_peak_right)
peak_sum_val_data = findpeakarea(df_data, est_peak_left, est_peak_right)
peak_left_data = peakleft(df_data, est_peak_left)
peak_right_data = peakright(df_data, est_peak_right)
peak_left_win_data = peakleftwin(df_data, est_peak_left)
peak_right_win_data = peakrightwin(df_data, est_peak_right)
baseline_val_openmc = background(df_openmc, est_peak_left, est_peak_right)
peak_sum_val_openmc = findpeakarea(df_openmc, est_peak_left, est_peak_right)
peak_left_openmc = peakleft(df_openmc, est_peak_left)
peak_right_openmc = peakright(df_openmc, est_peak_right)

plt.figure(3)
'''
plt.semilogy(df_data.energy, df_data.intensity, alpha=0.8, label="experimental", color="steelblue")
plt.vlines(x=peak_left_data, color="steelblue", alpha= 1, ls =':', ymin = 0, ymax=1e6)
plt.vlines(x=peak_right_data, color="steelblue", alpha= 1, ls =':', ymin = 0, ymax=1e6)
plt.hlines(y=baseline_val_data, color="steelblue", alpha= 0.5, ls =':', xmin = peak_left_win_data, xmax=peak_right_win_data)
plt.fill_between(x = df_data.energy, y1 = df_data.intensity, y2 = baseline_val_data,
        where = (peak_left_data <= df_data.energy)&(df_data.energy <= peak_right_data),
        color = "steelblue", alpha = 0.1)
'''

plt.semilogy(df_openmc.energy, df_openmc.intensity, alpha=0.3, label="simulation", color="black")
plt.vlines(x=peak_left_openmc, color="crimson", alpha= 1, ls =':', ymin = 0, ymax=1e6)
plt.vlines(x=peak_right_openmc, color="crimson", alpha= 1, ls =':', ymin = 0, ymax=1e6)
plt.hlines(y=baseline_val_openmc, color="crimson", alpha= 0.5, ls =':', xmin = peak_left_win_data, xmax=peak_right_win_data)
plt.fill_between(x = df_openmc.energy, y1 = df_openmc.intensity, y2 = baseline_val_openmc,
        where = (peak_left_openmc <= df_openmc.energy)&(df_openmc.energy <= peak_right_openmc),
        color = "black", alpha = 0.1)

plt.semilogy(df_openmc.energy, renorm_broadened_spectrum, alpha=0.8, label="processed simulation", color="crimson")
#plt.vlines(x=peak_left_openmc, color="crimson", alpha= 1, ls =':', ymin = 0, ymax=1e6)
#plt.vlines(x=peak_right_openmc, color="crimson", alpha= 1, ls =':', ymin = 0, ymax=1e6)
#plt.hlines(y=baseline_val_openmc, color="crimson", alpha= 0.5, ls =':', xmin = peak_left_win_data, xmax=peak_right_win_data)
plt.fill_between(x = df_openmc.energy, y1 = renorm_broadened_spectrum, y2 = baseline_val_openmc,
        where = (peak_left_openmc <= df_openmc.energy)&(df_openmc.energy <= peak_right_openmc),
        color = "crimson", alpha = 0.1)

plt.xlim(peak_left_win_data, peak_right_win_data)
plt.ylim(1e1,1e5)
plt.xlabel('Energy [keV]')
plt.ylabel('Intensity')
legend_elements = [#Patch(facecolor='steelblue', alpha = 1, label='data'),
                  #Patch(facecolor='steelblue', alpha = 0.2, label='background $=' + str(sci_notation(baseline_val_data,3)) + '$'),
                   #Patch(facecolor='crimson', alpha = 0.2, label='background $=' + str(sci_notation(baseline_val_openmc,3)) + '$'),
                   #Patch(facecolor='steelblue', alpha = 1, label='peak range'),
                   Patch(facecolor='black', alpha = 0.2),#, label='peak area $=' + str(sci_notation(peak_sum_val_data,3)) + '$'),
                   Patch(facecolor='crimson', alpha = 0.2)]#, label='peak area $=' + str(sci_notation(peak_sum_val_openmc,3)) + '$'),]
plt.legend(handles = legend_elements, loc='upper right', prop={'size': 10})
#plt.title(f"({est_peak_left} keV,{est_peak_right} keV)")
#plt.grid(True)
plt.minorticks_on()
plt.tight_layout()

plt.savefig(f"plots_{isotope}/" + f"compare_peak.png")
