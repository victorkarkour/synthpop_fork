import synthpop, pandas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from RadVel import BRAVA_Rad_Vel as BRV
import matplotlib.cm as cm
import matplotlib as mpl




# model = synthpop.SynthPop("config.synthpop_conf")
# model.init_populations()
# model.process_location(0, -4,1.0e-2)


#RV1 = BRV(startup = True,path = "/home/victor/SURP/venv/lib/python3.10/site-packages/synthpop/outputfiles/default_synthpop/*")
# print("1")
# RV1 = BRV(startup = True,path = "/home/victor/SURP/venv/lib/python3.10/site-packages/synthpop/outputfiles/default_synthpop/besancon_Robin2003_l-2.000_b-5.000.csv")
# print("2")
# RV2 = BRV(startup = True,path = "/home/victor/SURP/venv/lib/python3.10/site-packages/synthpop/outputfiles/default_synthpop/besancon_Robin2003_l-1.500_b-5.000.csv")
# print("3")
# RV3 = BRV(startup = True,path = "/home/victor/SURP/venv/lib/python3.10/site-packages/synthpop/outputfiles/default_synthpop/besancon_Robin2003_l-1.000_b-5.000.csv")
# print("4")
# RV4 = BRV(startup = True,path = "/home/victor/SURP/venv/lib/python3.10/site-packages/synthpop/outputfiles/default_synthpop/besancon_Robin2003_l-0.500_b-5.000.csv")
# print("5")
# RV5 = BRV(startup = True,path = "/home/victor/SURP/venv/lib/python3.10/site-packages/synthpop/outputfiles/default_synthpop/besancon_Robin2003_l0.500_b-5.000.csv")
# print("6")
# RV6 = BRV(startup = True,path = "/home/victor/SURP/venv/lib/python3.10/site-packages/synthpop/outputfiles/default_synthpop/besancon_Robin2003_l1.000_b-5.000.csv")
# print("7")
# RV7 = BRV(startup = True,path = "/home/victor/SURP/venv/lib/python3.10/site-packages/synthpop/outputfiles/default_synthpop/besancon_Robin2003_l1.500_b-5.000.csv")
# print("8")
# RV8 = BRV(startup = True,path = "/home/victor/SURP/venv/lib/python3.10/site-packages/synthpop/outputfiles/default_synthpop/besancon_Robin2003_l2.000_b-5.000.csv")
# print("9")
# RV9 = BRV(startup = True,path = "/home/victor/SURP/venv/lib/python3.10/site-packages/synthpop/outputfiles/default_synthpop/besancon_Robin2003_l10.000_b-4.000.csv")
# print("10")
RV1 = BRV(startup = True,path = "/home/victor/SURP/outputfiles/hst_bulge_treasury_sim/Oct2024_l-10.000_b-4.000.csv")
RV2 = BRV(startup = True,path = "/home/victor/SURP/outputfiles/hst_bulge_treasury_sim/Oct2024_l10.000_b-4.000.csv")


RV_pd = pd.DataFrame()
RV_pd = pd.concat([RV_pd, RV1.pd_RVs],ignore_index = True)
RV_pd = pd.concat([RV_pd, RV2.pd_RVs],ignore_index = True)
# RV_pd = pd.concat([RV_pd, RV3.pd_RVs],ignore_index = True)
# RV_pd = pd.concat([RV_pd, RV4.pd_RVs],ignore_index = True)
# RV_pd = pd.concat([RV_pd, RV5.pd_RVs],ignore_index = True)
# RV_pd = pd.concat([RV_pd, RV6.pd_RVs],ignore_index = True)
# RV_pd = pd.concat([RV_pd, RV7.pd_RVs],ignore_index = True)
# RV_pd = pd.concat([RV_pd, RV8.pd_RVs],ignore_index = True)
# RV_pd = pd.concat([RV_pd, RV9.pd_RVs],ignore_index = True)
# RV_pd = pd.concat([RV_pd, RV10.pd_RVs],ignore_index = True)

# lists = [3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15,15.5]
# # len(lists)
# # # num_list_B = RV1.Bulge_list_n
# # # num_list_D = RV1.Disk_list_n
# # # num_list_BD = []
# RV_B = RV1.RV_B
# RV_D = RV1.RV_D
# B_s = RV1.B_s
# D_s = RV1.D_s
# RV_Blsr = RV1.RV_Blsr
# RV_Dlsr = RV1.RV_Dlsr
# # for i in range(len(num_list_B)):
#     num_list_BD.append(num_list_B[i]-num_list_D[i])
# Bulge_numd_pd = pd.DataFrame(
#     {
#         "Number Density" : RV1.Bulge_list_n ,
#         "s" : lists
#     }
# )
# fig, ax = plt.subplots(2, 1, sharex=True, figsize=(9,11))

# ax[0].scatter(B_s, RV_B, label = "Bulge")
# ax[0].scatter(D_s, RV_D, label = "Disk")
# ax[1].scatter(lists, RV_Blsr, label = "Bulge")
# ax[1].scatter(lists, RV_Dlsr, label = "Disk")

# ax[1].set_xlabel("Distance from Sun [kpc]")
# ax[0].set_ylabel("Radial Velocity (LSR) of Bulge [km/s]")
# ax[1].set_ylabel("Mean Radial Velocity (LSR) of Disk [km/s]")
# ax[0].set_title("LSR Radial Velocity vs. Distance (10 l ,-4 b)")
# ax[1].set_title("Mean LSR Radial Velocity vs. Distance (10 l , -4 b)")
# ax[0].set_ylim(-400,400)
# ax[1].set_ylim(-400,400)
# ax[0].legend()
# ax[1].legend()
# plt.show()

# fig, ax2 = plt.subplots(figsize=(7,7))
# ax2.scatter(lists, num_list_BD)
# ax2.set_xlabel("Distance from Sun [kpc]")
# ax2.set_ylabel("Number Density Separation between Bulge and Disk [$m^{-3}$]")
# ax2.set_title("Separation of Number Density as a Function of Distance")
# plt.show()

# fig, ax2 = plt.subplots(figsize=(7,7))
# ax2.scatter(lists, RV1.num_list)
# ax2.set_xlabel("Radial Velocity ")
# ax2.set_ylabel("Number of Stars per bin")
# ax2.set_title("")
# plt.show()




# fig, ax2 = plt.subplots(figsize=(7,7))
# ax2.scatter(lists,RV_B, label = "RV of Bulge")
# ax2.scatter(lists,RV_D, label = "RV of Disk")
# ax2.set_xlabel("Distance from Sun [kpc]")
# ax2.set_ylabel("Radial Velocity [km/s]")
# ax2.set_title("Radial Velocity of Disk & Bulge as a function of Distance")
# ax2.legend()
# plt.show()



# THE BIG PLOT
# l_axis = RV_pd["l"]
# for i in range(len(l_axis)):
#     if l_axis[i] >= 180:
#         l_axis[i] = l_axis[i] - 360
#     elif (l_axis[i] <= 180 or l_axis[i] >= 90):
#         l_axis[i] = 360 - l_axis[i]
# b_axis = RV_pd["b"]
# RV_axis = RV_pd["Mean RV"].to_list()
# ticks = np.linspace(0,1,6)
# """
# Fix latitudes for plotting
# """
print(RV_pd)

# fig, (ax) = plt.subplots(sharex=True)
# ax.scatter(l_axis,b_axis, c = RV_axis,cmap = cm.seismic)
# ax_pcm = ax.scatter(l_axis,b_axis, c = RV_axis,cmap = cm.seismic, vmax = 100, vmin = -100)

# ax.set_xlabel("$l$ (deg.)")
# ax.set_xlim(-10,10)
# ax.invert_xaxis()
# ax.set_ylim(-10,10)
# ax.set_ylabel("$b$ (deg.)")
# ax.set_title("Radial Velocity")
# fig.colorbar(ax_pcm, label = "<RV> (km/sec)")

# plt.show()

    # COMPLETE!!!!! First, Split data into Bulge Data and Disk Data, via greater than 1.5 B-V, put the RVs & coordinates (degrees) in there too
        # Done!!!!!  Second, Find Number Density of Bulge & Disk Population Data & Put them in bins
        # Third, Plug all of these points into an eqaution, then solve for RV, and probably RV dispersion as well