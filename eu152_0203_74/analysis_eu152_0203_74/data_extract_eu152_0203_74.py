import numpy as np
import pandas
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

import sys
#other file
sys.path.insert(1, "/Users/a.l/Desktop/MSC/openmc/detector/")
from functions import read_file, get_counts, get_live_time

isotope = "eu152_0203_74"

###extract experimental data
source_data = read_file(f"experimental_data/{isotope}.Spe")
background_data = read_file("experimental_data/Background_02_03_2022.Spe")
intensity_data = get_counts(source_data)
background_intensity_data = get_counts(background_data)
livetime_data = get_live_time(source_data)
#background treatment with spectrum collection time adjustments
intensity_data = intensity_data - ( background_intensity_data * (livetime_data/get_live_time(background_data)))
#cut the data short because most of them are meaningless
bin_no = 3500 #3500 bins
intensity_data = intensity_data[:bin_no]

#manual callibration of energy
peaks = find_peaks(intensity_data, prominence=3000)[0]
#print(peaks)
#plt.semilogy(intensity_data)
#plt.show()
#select two photopeaks of eu-152 get its energy and match bin pos
#print(peaks[6])
m = (964.057 - 121.7817) / (peaks[6] - (peaks[2]))
b = 121.7817 - (m * peaks[2])

#generating the ebins
x = np.arange(bin_no)
energy_data = b + x * m

#create dataframe
df_data = pandas.DataFrame({
    'energy': energy_data[1:],
    'intensity': intensity_data[1:]
})