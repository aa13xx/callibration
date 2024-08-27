#package
import openmc
import numpy as np
import pandas

import sys
#other files
from openmc_eu152_0203_74 import energy_bins, sim_batch, sim_particle, tally_1, tally_1_type, source_activity
from data_extract_eu152_0203_74 import isotope

#extract tallies into pandas df
sp = openmc.StatePoint(f"statepoint.{sim_batch}.h5")
#sp = openmc.StatePoint(f"{source}" + f"/statepoint.20.1e6.h5")
tally = sp.get_tally(name=f"{tally_1}")
#chopping first entry because it is ridiculous
intensity = list(tally.get_values(scores=[tally_1_type]).flatten())
#chopping first entry because it is ridiculous and last entry because it is excessive
energy = energy_bins[1:]/1000
energy_adjusted = energy[1:]

df_openmc = pandas.DataFrame({
    'energy': energy_adjusted,
    'intensity': intensity
})

