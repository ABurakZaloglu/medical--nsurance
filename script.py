import csv

ages = []
sexs = []
bmis = []
children = []
smokers = []
regions = []
charges = []

with open('insurance.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ages.append(row['age'])
        sexs.append(row['sex'])
        bmis.append(row['bmi'])
        children.append(row['children'])
        smokers.append(row['smoker'])
        regions.append(row['region'])
        charges.append(row['charges'])


male_count = len([male for male in sexs if male == 'male'])
female_count = len([female for female in sexs if female == 'female'])
smoker_count = len([smoker for smoker in smokers if smoker == 'yes'])
nonsmoker_count = len([smoker for smoker in smokers if smoker == 'no'])
reigon_count = {'southwest' : 0,'southeast':0,'northwest':0,'northeast':0}
over_18_years_old_count = len([age for age in ages if int(age) > 18])
below_18_years_old_count = len([age for age in ages if int(age) <= 18])

def average_age(ages):
    sum = 0
    for age in ages:
        sum += int(age)
    return round(sum / len(ages),2)

def average_bmi(bmis):
    sum = 0
    for bmi in bmis:
        sum += float(bmi)
    return round(sum / len(bmis),2)

def calculate_regions_count(regions):
    for region in regions:
        if region == 'southwest':
            reigon_count['southwest'] +=1 
        
        elif region == 'southeast':
            reigon_count['southeast'] +=1 

        elif region == 'northwest':
            reigon_count['northwest'] +=1 

        elif region == 'northeast':
            reigon_count['northeast'] +=1 

def average_charge_based_on_sex(sexs,charges):
    male_charge = 0
    female_charge = 0
    data = list(zip(sexs,charges))
    for item in data:
        if item[0] == 'female':
            female_charge += float(item[1])
        else:
            male_charge += float(item[1])
    average_male_charge = round((male_charge/male_count),2)
    average_female_charge = round((female_charge/female_count),2)
    print("The average annual medical charge for males is: $" + str(average_male_charge))
    print("The average annual medical charge for females is: $" + str(average_female_charge))

def average_charge_based_on_reigon(regions,charges):
    data = list(zip(regions,charges))
    southwest_total_cost = 0
    southeast_total_cost = 0
    northwest_total_cost = 0
    northeast_total_cost = 0

    for item in data:
        if item[0] == 'southwest':
            southwest_total_cost += float(item[1])
        
        elif item[0] == 'southeast':
            southeast_total_cost += float(item[1])

        elif item[0] == 'northwest':
            northwest_total_cost += float(item[1])

        elif item[0]== 'northeast':
            northeast_total_cost += float(item[1])
    
    average_southwest_charge = round((southwest_total_cost/reigon_count['southwest']),2)
    average_southeast_charge = round((southeast_total_cost/reigon_count['southeast']),2)
    average_northwest_charge = round((northwest_total_cost/reigon_count['northwest']),2)
    average_northeast_charge = round((northeast_total_cost/reigon_count['northeast']),2)

    print("The average annual medical charge for Southwesterners is: $" + str(average_southwest_charge))
    print("The average annual medical charge for Southeasterners is: $" + str(average_southeast_charge))
    print("The average annual medical charge for Northwesterners is: $" + str(average_northwest_charge))
    print("The average annual medical charge for Northeasterners is: $" + str(average_northeast_charge))

def average_charge_based_on_age(ages,charges):
    data = list(zip(ages,charges))
    total_cost_over_18 = 0
    total_cost_below_18 = 0

    for item in data:
        if int(item[0]) > 18:
            total_cost_over_18 += float(item[1])
        else:
            total_cost_below_18 += float(item[1])
    
    average_cost_over_18 = round((total_cost_over_18/over_18_years_old_count),2)
    average_cost_below_18 = round((total_cost_below_18/below_18_years_old_count),2)

    print("The average annual medical charges for a person with a Age over 18 is: $" + str(average_cost_over_18))
    print("The average annual medical charges for a person with a Age below 18 is: $" + str(average_cost_below_18))

def average_charge_based_on_smoker(smokers,charges):
    data = list(zip(smokers,charges))
    smoker_total_cost = 0
    nonsmoker_total_cost = 0

    for item in data:
        if item[0] == 'yes':
            smoker_total_cost += float(item[1])
        else:
            nonsmoker_total_cost += float(item[1])
    
    average_smoker_charge = round((smoker_total_cost/smoker_count),2)
    average_nonsmoker_charge = round((nonsmoker_total_cost/nonsmoker_count),2)

    print("The average annual medical charges for a smoker person is: $" + str(average_smoker_charge))
    print("The average annual medical charges for a nonsmoker person is: $" + str(average_nonsmoker_charge))

calculate_regions_count(regions)
average_charge_based_on_sex(sexs,charges)
average_charge_based_on_reigon(regions,charges)
average_charge_based_on_age(ages,charges)
average_charge_based_on_smoker(smokers,charges)