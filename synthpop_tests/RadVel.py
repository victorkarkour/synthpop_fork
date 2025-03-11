import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import glob
import matplotlib.cm as cm
#import scipy.interpolate as interpolate

class BRAVA_Rad_Vel:
    def __init__(self, startup = False, plot = False, binnum = 14 ,path = str):
        #self.path = glob.glob(path) # TRY TO MAKE AN "ALL" FUNCTION FOR EACH FUNCTION THAT ITERATES ON A FOLDER OF .CSV FILES
        self.path = path #
        print("Reading .csv file....")
        self.csv = pd.read_csv(self.path)
        self.binnum = binnum # DONT FORGET ABOUT THIS!!!! <-------
        
        if startup:
            print("Calculating B-V Magnitudes....")
            DF_BPVP = self.BP_VP()
        if startup:
            print("Isolating Red Giant Stars....")
            Bulge_Giants, Disk_Giants = self.RedGiant(DF_BPVP)
        if startup:
            print("Placing Stars into Distance Bins....")
            Bin_Giants_Bulge, Bin_Giants_Disk = self.BinDist(Giant_list = [Bulge_Giants, Disk_Giants])
        if startup:
            print("Calculating Number Density of Bins....")
            self.Bulge_list_n , self.Disk_list_n = self.n_density(Filtered_list = [Bin_Giants_Bulge, Bin_Giants_Disk])
        if startup:
            print("Caluclating Mean Radial Velocity....")
            self.pd_RVs = self.BRad_v(Total_list = [self.Bulge_list_n, self.Disk_list_n], Filtered_list = [Bin_Giants_Bulge,Bin_Giants_Disk])
            print()
        if plot:
            print("Plotting Radial Velocities....")
            self.PlotRVs(self.pd_RVs)
            
    def read_file(self, Print = False):
        """
        # TEST FUNCTION, NOT VERY HELPFUL
        Takes in the file and reads the file in prep for reading the Blue Photometer (BP) & Red Photometer (RP) difference
        ----------------------
        Parameters:
        path: string, required
        - Path to .csv file, only works with .csv file for now
        print: boolean, optional
        - Gives the option to print the entire file for reading or parsing purposes
        
        ----------------------
        """
        # Initialize
        self.df = ""
        self.df = pd.read_csv(self.path)
        # Basically a Test Function
        if Print:
            return print(self.df)
        else: 
            return self.path
    
    def BP_VP(self, BP = "Gaia"):
        """
        Reads the file and takes the BP-RP of the Stars; Can determine type of system that took BP/RP
        -------------------
        Parameters:
        BP: string, optional
        - Can change type of system used to find BP & RP
        
        -------------------
        Returns:
        DataFrame with BPVP on the rightmost column [DataFrame]
        """
        df = self.csv
        
        # CHECK IN GAIA AND BESSELL IF THESE ARE THE CORRECT PHOTOMETERS TO SEE IF THEY ARE CORRECT
        if BP == "Gaia":
            self.BP = df["Gaia_BP_EDR3"]
            self.VP = df["Gaia_RP_EDR3"]
            self.Gmag = df["Gaia_G_EDR3"]
            self.Dist = df["Dist"]
        else:
            # Didn't know which one to use, so gave the option for both ^^^^^
            self.BP = df["Bessell_B"]
            self.VP = df["Bessell_V"]
        # B-V Calculation inserted into main DataFrame
        df.insert(len(df.columns),"BPVP", self.BP-self.VP)
        # Calculate 
        DF = df
        return DF
    
    def RedGiant(self, DF_BPVP):
        """
        Finds where Red Giants are within the Star Populations, and splits them into two Data files: One for the Bulge Data,
        and the other for the Disk Data (Everything else)
        Returns two data files
        ------------------------
        Parameters:
        
        
        ------------------------
        Returns: List of Red Giant Stars [List]
        """
        # Initialize Variables
        self.Bulge_Data = pd.DataFrame(
                        {
                        },
                    )
        self.Disk_Data = pd.DataFrame(
                        {
                        },
                    )
        self.RV_B = []
        self.B_s = []
        self.RV_D = []
        self.D_s = []
        # Calls back to the B-V calculation to get the list of B-V values
        df = DF_BPVP
        
        # Teff <= 5300 & Log g <= 3.8 for Red Giants
        # Uses in the DataFrame.loc[] tool to help us filter out every other star but Red Giants
        Bulge_Data = df.loc[(df["BPVP"] > 0.95) & (df["Gaia_G_EDR3"] < 3.9) & (df["pop"] == 0),["VR_LSR","l","b","Dist", "pop"]]              
        
        # I'm making it avoid Population 1 because it is the Halo Population, I can always comment this out if its wrong
        Disk_Data = df.loc[(df["BPVP"] > 0.95) & (df["Gaia_G_EDR3"] < 3.9) & (df["pop"] != 0),["VR_LSR","l","b","Dist", "pop"]]
        
        self.RV_B = Bulge_Data["VR_LSR"]
        self.RV_D = Disk_Data["VR_LSR"]
        self.B_s = Bulge_Data["Dist"]
        self.D_s = Disk_Data["Dist"]
        return Bulge_Data, Disk_Data
    
    #def RedGiant_all(self , )

    def BinDist(self, Giant_list):
        """
        Puts the Distance of a DataFrame in Bins and returns it as a List of the DataFrames
        ------------------------
        Parameters:
        ## MAKE IT SO THAT YOU CAN CHANGE THE AMOUNT OF BINS U WANT FOR A GIVEN PLOT
        ------------------------
        Returns: List of Filtered DataFrames [List]
        """
        #Initializes the Data Sets
        self.Bulge_Data = Giant_list[0]
        self.Disk_Data = Giant_list[1]
        
        Dict_filter_DD = {}
        Dict_filter_BD = {}
        x = 3
        j = 0
        while x < 16:
            Dict_filter_BD["Dist_filter_{0}".format(j)] = self.Bulge_Data.loc[(self.Bulge_Data["Dist"] >= x) & (self.Bulge_Data["Dist"] <= x+0.5)]
            Dict_filter_DD["Dist_filter_{0}".format(j)] = self.Disk_Data.loc[(self.Disk_Data["Dist"] >= x) & (self.Disk_Data["Dist"] <= x+0.5)]
            x +=0.5
            j += 1
            #Dist_filter_0 = self.TD.loc[(self.TD["Dist"] >= 3) & (self.TD["Dist"] <= 4)]
            
        i=0
        Dfilter_list_BD = []
        Dfilter_list_DD = []
        for i in range(len(Dict_filter_BD)): Dfilter_list_BD.append(Dict_filter_BD["Dist_filter_{0}".format(i)])
        for i in range(len(Dict_filter_DD)): Dfilter_list_DD.append(Dict_filter_DD["Dist_filter_{0}".format(i)]) 
        return Dfilter_list_BD, Dfilter_list_DD

    def n_density(self, Filtered_list):
        """
        Calculates the number density of the Disk and the Bulge and returns it as a list
        Number Density = # of Stars / Volume of Cone 
        V = (pi * r^2 * h)/3
        ------------------------
        Parameters:
        
        
        ------------------------
        Returns: Disk and Bulge Number Density [List]
        """
        
        # Splits the List back into its two parts for both Filterings
        Dfilter_list_BD = Filtered_list[0]
        Dfilter_list_DD = Filtered_list[1]
        
        Bulge_List = []
        Disk_List = []
        
        # Some inital values for Number Density (Might be incorrect)
        # BulgeNum = len(self.Bulge_Data["Dist"])
        # DiskNum = len(self.Disk_Data["Dist"])
        angle = 1e-2 # Units of steradians
        j = 0
        x = 3
        
        # Convert solid angle to radians
        solidangle = angle**0.5
        
        # Actual Values (Subtract max radius by min radius to get truncated cone (look it up stupid))
        # Check Units of halfangle (could be in steradians or radians)
        halfangle = solidangle
        
        for j in enumerate(Dfilter_list_BD):
            if j[1].empty:
                Bulge_List.append(0)
            else:
                BulgeNum = len(j[1])
                # Conditions for Bulge & Disk Separation
                # Height Distances for Cone
                heightB_max = x+0.5
                heightB_min = x
                # heightB = heightB_max - heightB_min
                # CHANGE NUMBER DENSITY TO BE MORE ACCURATE
                r_close = heightB_min * np.tan(halfangle)
                r_far = heightB_max * np.tan(halfangle)
                # Volume Equation
                # if heightB == 0:
                #      heightB = 1
                #      VolumeB = (np.pi * heightB)/3 *()
                # else:
                VolumeB = (np.pi * heightB_min)/3 * (r_far + r_close)**2
                # Density Equation
                Bulge_Dens = BulgeNum / VolumeB
                # Build Bulge & Disk Lists
                Bulge_List.append(Bulge_Dens)
            x+=0.5
        j = 0
        x = 3
        for j in enumerate(Dfilter_list_DD):
            if j[1].empty:
                Disk_List.append(0)
            else: 
                DiskNum = len(j[1])
                # Average for Distance
                heightD_max = x+0.5
                heightD_min = x
                # heightD = heightD_max - heightD_min
                # CHANGE NUMBER DENSITY TO BE MORE ACCURATE
                r_close = heightD_min * np.tan(halfangle)
                r_far = heightD_max * np.tan(halfangle)
                # Volume Equation
                # if heightB == 0:
                #      heightB = 1
                #      VolumeB = (np.pi * heightB)/3 *()
                # else:
                # Volume Equation
                VolumeD = (np.pi * heightD_min)/3 * (r_far + r_close)**2
                # Density Equation
                Disk_Dens = DiskNum / VolumeD
                # Build Bulge & Disk Lists
                Disk_List.append(Disk_Dens)
            x+=0.5
        self.Total_Data = pd.concat([self.Bulge_Data,self.Disk_Data], sort = True)
        
        return Bulge_List, Disk_List
        
    def BRad_v(self, Total_list, Filtered_list, Dispersion = True):
        """
        Using an annoyingly complicated formula, finds the Radial Velocity of each Red Giant Star 
        ------------------------
        Parameters:
        
        
        ------------------------
        Returns: Mean Radial Velocity for a given amount of pops pops [List]
        """
        # Initialize all values for the for loop
        Bulge_List = Total_list[0]
        Disk_List = Total_list[1]
        self.RV_list = 0
        l_list = []
        b_list = []
        sum_eq1 = 0
        sum_eq2 = 0
        sumsq_eq1 = 0
        sumsq_eq2 = 0
        RV_mean = 0
        RV_disp = 0
        self.RV_Blsr = []
        self.RV_Dlsr = []
        self.dist_B = []
        self.dist_D = []
        
        Dfilter_list_BD = Filtered_list[0]
        Dfilter_list_DD = Filtered_list[1]
        #Dfilter_list = pd.DataFrame()
        #Dfilter_list = pd.concat([Dfilter_list_BD,Dfilter_list_DD], ignore_index=True)
        
        NanCon_BL =np.isnan(Bulge_List)
        Bulge_List = np.array(Bulge_List)
        Bulge_List[NanCon_BL] = 0.0
        Bulge_List = Bulge_List.tolist()
        NanCon_DL = np.isnan(Disk_List)
        Disk_List = np.array(Disk_List)
        Disk_List[NanCon_DL] = 0.0
        Disk_List = Disk_List.tolist()
        
        
        sumlist_1 = []
        sumlist_2 = []
        Dist_val_list = []
        num_list_B = []
        num_list_D = []
        self.num_list = []
        
        i = 0
        j = 3
        for i in range(len(Dfilter_list_BD)):
            DataFrame_BD = Dfilter_list_BD[i]
            DataFrame_DD = Dfilter_list_DD[i]
            
            #DataFrame_BD = DataFrame_BD.to_frame()
            #DataFrame_DD = DataFrame_DD.to_frame()
            
            # Condition if there are no values in a DataFrame
            if DataFrame_BD.empty == True:
                DataFrame_BD = pd.DataFrame({"Dist": [0] ,"VR_LSR": [0], "l": [None], "b": [None], "pop": [0]})
                #DataFrame_BD.fillna(value = 0, axis = 0, inplace = True)
            if DataFrame_DD.empty == True:
                DataFrame_DD = pd.DataFrame({"Dist": [0] ,"VR_LSR": [0], "l": [None], "b": [None], "pop": [5]})
            
            # Takes Average of Distance for Equation
            # Dist_val = (DataFrame_DD["Dist"].mean(skipna = True) + DataFrame_BD["Dist"].mean(skipna = True)) / 2
            Dist_val = j
            self.dist_B.append(DataFrame_BD.Dist)
            self.dist_D.append(DataFrame_DD.Dist) 
            # Takes Average of Angle Positions
            l_list.append((DataFrame_BD["l"].mean(skipna = True) + DataFrame_DD["l"].mean(skipna = True))/2)
            b_list.append((DataFrame_BD["b"].mean(skipna = True) + DataFrame_DD["b"].mean(skipna = True))/2)
            
            # Sorts the filter's RV by lowest at top to highest at bottom
            DataFrame_BD.sort_values(by="l")
            DataFrame_DD.sort_values(by="l")
            
            # Mean Local Standard of Rest RVs
            Bulge_lsr = DataFrame_BD["VR_LSR"].mean(skipna = True)
            self.RV_Blsr.append(Bulge_lsr)
            
            Disk_lsr = DataFrame_DD["VR_LSR"].mean(skipna = True)
            self.RV_Dlsr.append(Disk_lsr)
            
            # Numerator & Denominator Equations    
            Eq1 = (Disk_List[i] * Disk_lsr + Bulge_List[i] * Bulge_lsr) * Dist_val ** 0.6 
            Eq2 = (Bulge_List[i] + Disk_List[i]) * Dist_val ** 0.6
            
            sum_eq1 += Eq1
            sum_eq2 += Eq2
            
            sumsq_eq1 += Eq1**2
            sumsq_eq2 += Eq2**2
            
            sumlist_1.append(Eq1)
            sumlist_2.append(Eq2)
            Dist_val_list.append(Dist_val)
            num_list_B.append(len(DataFrame_BD))
            num_list_D.append(len(DataFrame_DD))
            
            i += 1
            j += 0.5
            
        # Final Equation
        RV_mean = sum_eq1 / sum_eq2
        
        # Calculates STD of BRAVA RVs
        if Dispersion == True: 
            RV_disp = ((sumsq_eq1 / sumsq_eq2) - RV_mean**2)**0.5
            l_mean = np.nanmean(l_list)
            b_mean = np.nanmean(b_list)
            
            if l_mean > 180:
                l_mean = l_mean - 360
                
            RV_pd = pd.DataFrame({"Mean RV": [RV_mean], "l": [round(l_mean,2)],"b": [round(b_mean,2)], "Dispersion": [RV_disp]})
        else: 
            l_mean = np.nanmean(l_list)
            b_mean = np.nanmean(b_list)
            RV_pd = pd.DataFrame({"Mean RV": [RV_mean], "l": [round(l_mean,2)],"b": [round(b_mean,2)]})
        self.num_list = num_list_B + num_list_D    
        
            
        return RV_pd
    # FIND A WAY TO TAKE MULTIPLE PANDAS FILES AND COMBINE THEM TO MAKE ONE BIG DATA SET WITH ALL MEAN RVs
    # OR TRY INCREASING SOLID ANGLE TO TAKE IN WHOLE DEGREES (LIKE 5 DEGREES) INSTEAD OF 0.01 DEGREES
    
    # DON'T FORGET ABOUT RV DISPERSION AS WELL (idk how to do the squared parts of that)
    
    def PlotRVs(self, Total_Data):
        l_axis = Total_Data["l"]
        b_axis = Total_Data["b"]
        RV_axis = Total_Data["Mean RV"]
        
        fig, (ax1) = plt.subplots(sharex=True)
        
        ax1.plot(l_axis,b_axis,color = "seismic")
        fig.colorbar(RV_axis, cmap="seismic", ax = ax1)
        ax1.set_xlabel("$l$ (deg.)")
        ax1.set_ylabel("$b$ (deg.)")
        ax1.set_title("Radial Velocity")
        plt.show()


# RV1 = BRAVA_Rad_Vel(startup = True,path = "/home/victor/SURP/outputfiles/hst_bulge_treasury_sim/Oct2024_l10.000_b-4.000.csv")