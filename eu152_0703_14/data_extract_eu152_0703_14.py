import numpy as np
import pandas
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


from functions import read_file, get_counts, get_live_time

isotope = "eu152_0703_14"

###extract experimental data
source_data = read_file(f"experimental_data/{isotope}.Spe")
background_data = read_file("experimental_data/Background_07_03_2022.Spe")
intensity_data = get_counts(source_data)
background_intensity_data = get_counts(background_data)
livetime_data = get_live_time(source_data)
#background treatment with spectrum collection time adjustments
intensity_data = intensity_data - ( background_intensity_data * (livetime_data/get_live_time(background_data)))
#cut the data short because most of them are meaningless
bin_no = 3500 #3500 bins
intensity_data = intensity_data[:bin_no]

#manual callibration of energy
peaks = find_peaks(intensity_data, prominence=1000)[0]
#print(peaks)
#plt.semilogy(intensity_data)
#plt.show()
#select two photopeaks of eu-152 get its energy and match bin pos
#print(peaks[6])
m = (964.057 - 121.7817) / (peaks[11] - (peaks[5]))
b = 121.7817 - (m * peaks[5])

#generating the ebins
x = np.arange(bin_no)
energy_data = b + x * m

#create dataframe
df_data = pandas.DataFrame({
    'energy': energy_data[1:],
    'intensity': intensity_data[1:]
})

#plt.semilogy(df_data.energy, df_data.intensity)
#plt.show()