mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]


#stores the number of missions as a variable, outputs the number
mission_num = len(mission_names)
print(str(mission_num) + " total missions.\n")

#counts the number of successful missions
mission_suc = mission_success.count(True)
print(str(mission_suc) + " successful missions.\n")

#calculates success percentage of the missions
miss_suc_rate = ((mission_suc / mission_num) * 100)
print(f"{miss_suc_rate:.2f}% success rate.\n")

#list the names of all missions before the year 2000
#year_list_index = mission_years.index()
year_list_filtered = []
name_list_filtered  = []
year_list_index = 0

def find_years(list, element):
    #year_list_filtered = []
    for i, v in enumerate(list):
        if v < element:
            year_list_filtered.append(i)
    return year_list_filtered 


"""
find_names(name_list,index_list)
returns an array of names based on an array of indexes
"""
'''
def find_names(name_list,index_list):
    print (name_list[i] for i in index_list)

find_years(mission_years, 2000)
find_names(mission_names, year_list_filtered)
'''



'''
for x in enumerate(year_list_filtered):
    print(mission_names[x])
'''




print(find_years(mission_years, 2000))
'''
for x in mission_years:
    if x < 2000:
        year_list_filtered.append()
        #year_list_index = year_list_index + 1
        '''

print(mission_years)
#print(year_list_index)
print(year_list_filtered)
for i in year_list_filtered:
    print(mission_names[i])