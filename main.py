#initial data set
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]


#stores the number of missions as a variable, outputs the number
mission_num = len(mission_names)
print("\nThere were \033[0;34m" + str(mission_num) + "\033[0m total missions.")

#counts the number of successful missions, prints
mission_suc = mission_success.count(True)
print("\033[0;34m" + str(mission_suc) + "\033[0m missions were completed successfully.")

#calculates success percentage of the missions, prints
miss_suc_rate = ((mission_suc / mission_num) * 100)
print(f"Mission success rate was \033[0;34m{miss_suc_rate:.2f}\033[0m%.")


#setting up some variables for use in function
year_list_filtered = []
name_list_filtered  = []
mission_years_filtered = []
year_list_index = 0

#find_years - a function to filter a list based on an element
# the goal output is to determine the indexes of all mission_year[]
# that occurred before the year 2000 (enumerate is essential here)
# I added a bit to output mission_years_filtered[]
def find_years(list, element):
    for i, v in enumerate(list):
        if v < element:
            year_list_filtered.append(i)
            mission_years_filtered.append(v)
    return year_list_filtered 
    return mission_years_filtered

#initialize function for returns of formed lists
find_years(mission_years, 2000)

# test outputs
#print(mission_years)
#print(year_list_index)
#print(year_list_filtered)

#prints the mission names matching the index numbers in
#year_list_filtered, prints from mission_names[]
# I added years to fill it out a bit
print("The names of missions launched before the year 2000 are:")
for i in year_list_filtered:
    print("- " + mission_names[i] + ", " + str(mission_years_filtered[i-1]))

print("\n***END PROGRAM***\n")