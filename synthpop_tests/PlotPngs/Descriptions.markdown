# ARGRadVel_s.png
------------------------------
Description: Used to separate bulge and disk and understand why velocity dispersion could be different

Analysis: Seems to have a main bulge of stars between 5-12 kpc for the bulge section and the disk's stars being all throughout the plot. 

Location of test: Test.ipynb

------------------------------

# ColorMagCutGaiaG.png
------------------------------
Description: Used to find difference between the absolute magnitude (Gaia G magnitude) within the Disk and Bulge stars, assumed this could've been a problem with the generation. <br>
**(Still possibly could be, must look into further)**

Analysis: Because we made cuts to the stars according to our parameters for the project (Red Giants), we see Red Giant like stars within the plots.
Of course, due to the fact that the bulge has more stars within it, we see that there is a large spike of stars near the 0.9-1.5 B-V region for the bulge mainly,
with a main section of the Disk stars being in this region as well.

Location of test: Test.ipynb

------------------------------

# ColorMagGaigaG.png
------------------------------
Description: CMD of Star Populations, not separated by populations, using the Gaia G magnitude to determine luminosity.

Analysis: There were no cuts made to this Color Magnitude, which means that all of the stars in the generation are within this plot. As we can see, it would appear to be a pretty normal
Color Magnitude Diagram, with some stars on the far left depicting white dwarfs and the main sequence stars being the majority in the downward sloping line.

Location of test: Test.ipynb

------------------------------

# JKvsKTest.png
------------------------------
Description: CMD of Star Populations, separated by populations, using K magnitudes to determine luminosity.

Analysis: What we see in this plot is that there is a general increasing curved slope for both the Bulge and Disk stars as they increase in the J-K axis.
There isn't much to say about this graph, but the J-K was a potiential candidate to use for replacing the B-V range.

Location of test: Test.ipynb

------------------------------

# LSRRadVel_s.png
------------------------------
Description: A similar plot done by `ARGRadVel_s.png`, except utilizing mean LSR rather than only LSR Rad Vel.

Analysis: Compared to the previous plot, we find that the mean velocities for each sector of the Distance is relatively close to the 
origin (0), save a few points in the bulge that force the overall Mean Radial Velocity towards the negative portions of the graphs.

Location of test: Test.py

------------------------------

# NegRVCount.png
------------------------------
Description: This png will be glossed over, as the `VelDisp.png` is this plot except improved and with greater information.
This plot will be described in that section better.

Analysis: Analyzed in following pngs

Location of test: Test.py

------------------------------

# NumDens_s.png
------------------------------
Description: This plot is used to determine where the number densities for each section of the each population is being taken up from.

Analysis: As to be expected, the Bulge number density increases between the location of the bulge, that being 5-10 kpc. The number density 
for the disk hwoever is confusing because the initial value for the number density is rather large for the disk's size, but peters down as to be 
expected after some moments.

Location of test: Unknown

------------------------------

# RVCount.png
------------------------------
Description: See reasoning for no description in `NegRVCount.png`. It has the same reasoning as this png.

Analysis: 

Location of test: 

------------------------------

# RVCountsOrigin.png
------------------------------
Description: See reasoning for no description in `NegRVCount.png`. It has the same reasoning as this png.

Analysis: 

Location of test: 

------------------------------

# RadVelDB_s.png
------------------------------
Description: This plot is the aftermath of the creation of the BRAVA code created mistakingly as a range rather than a singular value.

Analysis: This plot is fragmented and incorrect, the png will be removed soon.

Location of test: Test.py

------------------------------

# RadVel_s.png
------------------------------
Description: This plot has the same problem as `RadVelDB_s.png` and will be removed soon alongside the mentioned png.

Analysis: This plot is fragmented and incorrect, the png will be removed soon.

Location of test: Test.py

------------------------------

# SepNumDens_s.png
------------------------------
Description: This plot is incorrect as the number density should not be negative for any value, this plot will be removed soon.

Analysis: This plot is fragmented and incorrect, the png will be removed soon.

Location of test: Unknown

------------------------------

# VelDisp_-10_-6.png
------------------------------
Description: These are the aforementioned plots that `NegRVCount.png`, `RVCount.png`, `RVCountsOrigin.png` mention within their descriptions.
In this plot, we attempted to match the raw data from the research paper via a gaussian with our own data generated by the synthetic population.
We also describe the Mean and Standard Deviation of each angle shown with the mean and standard deviation of the paper being on a separate spreadsheet located [here](https://docs.google.com/spreadsheets/d/1UBCK5BIft7aKlvVIGc33buV0wvXjqERnBTPN5mjysrg/edit?usp=sharing).

Analysis: As we can see from this angle, the Paper's fit does not match our own fit, with our Radial Velocity counts going crazy after a certain point past the origin.

Location of test: Test.ipynb

------------------------------

# VelDisp_-5_-8.png
------------------------------
Description: Description is the same as previous description. Look above for proper description.

Analysis: With this plot, we can see that the paper's fit is closer to our own data, however it is still off by a certain shift of the SynthPop data.

Location of test: Test.ipynb

------------------------------

# VelDisp_0_-6.png
------------------------------
Description: Description is the same as previous description. Look above for proper description.

Analysis: For this plot, the paper fit is very close to our own data, with the only problem being with our data is there being some uneven portions near the 
0-100 RV LSR axis range.

Location of test: Test.ipynb

------------------------------

# VelDisp_10_-6.png
------------------------------
Description: Description is the same as previous description. Look above for proper description.

Analysis: With this plot, the fit is very similar in amplitude and shape somewhat, however the data does not fit the paper's fit, as the data seems to be shifted to the
left leading to a more decreasing RV rather than an increasing RV we see in the paper.

Location of test: Test.ipynb

------------------------------

# VelDisp_5_-8.png
------------------------------
Description: Description is the same as previous description. Look above for proper description.

Analysis: This plot has the fit being barely similar to the data from the generation, with the shift of the velocity from the data being slightly greater compared to the previous
plot. 

Location of test: Test.ipynb

------------------------------
