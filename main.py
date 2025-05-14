#initial data set
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]


#stores the number of missions as a variable, outputs the number
#I use variables here to make print() less complicated & easier to debug
mission_num = len(mission_names) 
print("\nThere were \033[0;34m" + str(mission_num) + "\033[0m total missions.")

#counts the number of successful missions, prints
mission_suc = mission_success.count(True)
print("\033[0;34m" + str(mission_suc) + "\033[0m missions were completed successfully.")

#calculates success percentage of the missions, prints
miss_suc_rate = ((mission_suc / mission_num) * 100)
print(f"Mission success rate was \033[0;34m{miss_suc_rate:.2f}\033[0m%.")

#setting up some variables for use in creating output arrays
year_index_list = []

#uses enumerate to separate mission_years into a series of years and indexes,
# if mission year is before 2000, index is output into new list: year_index_list[]
# for use in later outputs
for i, v in enumerate(mission_years):
    if v < 2000:
        year_index_list.append(i)

#prints the mission names matching the index in 
# year_index_list, prints from mission_names[] and mission_years[]
# (I added years to fill out the presentation a bit)
print("The names of missions launched before the year 2000 are:")
for i in year_index_list:
    print("- " + mission_names[i] + ", " + str(mission_years[i]))

print("\n***END PROGRAM***\n")