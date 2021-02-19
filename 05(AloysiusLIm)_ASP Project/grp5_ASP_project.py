import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Asia5():

    imva = pd.read_excel('IMVA.xls')  # import xls file that is in the same folder

    asia5 = [imva['Brunei Darussalam'], imva['Indonesia'], imva['Malaysia'], imva['Myanmar'], imva['Philippines'],
             imva['Thailand'], imva['Vietnam'],
             imva['China'], imva['Hong Kong SAR'], imva['Taiwan'], imva['Japan'], imva['South Korea'], imva['Bangladesh'],
             imva['India'], imva['Pakistan'], imva['Sri Lanka'],
             imva['Iran'], imva['Israel'], imva['Kuwait'], imva['Saudi Arabia'],
             imva['United Arab Emirates']]  # select regions of asia5

    columns_in_asia_5_as_INDEX = range(len(list(asia5)))  # range of columns in asia5 this is 0...20
    all_SUM_of_asia5 = []
    all_COUNTRY_of_asia5 = []

    #print(columns_in_asia_5_as_INDEX)
    #print(asia5[0].name)

    count_values = 0
    count_number_of_columns = 0
    for col_id in columns_in_asia_5_as_INDEX:  # if im already looping througha ll columns why do i need to do this 5 times again? right?
        #print(asia5[col_id].name)  # header of the column
        #print("Column " + str(count_number_of_columns) + " out of 20 in Asia5")
        sum_of_each_col = []  # forgot to reset
        count_number_of_columns = count_number_of_columns + 1
        for value_index in range(len(asia5[col_id])):

            if asia5[col_id][value_index] == asia5[col_id][396] or value_index > 396:  # value_index is the integer index for whole 516 #forgot to set it up
                if asia5[col_id][value_index] == 'na':
                    asia5[col_id][value_index] = '0'
                sum_of_each_col.append(int(asia5[col_id][value_index].replace(',', '')))

        all_SUM_of_asia5.append(sum(sum_of_each_col))
        all_COUNTRY_of_asia5.append(asia5[col_id].name)
        #print("this is the sum of each column: " + str(sum(all_SUM_of_asia5)))
       #print("---------------")
    final_dataframe_of_asia5 = pd.DataFrame()

    final_dataframe_of_asia5.head(3)

    final_dataframe_of_asia5["country"] = all_COUNTRY_of_asia5
    final_dataframe_of_asia5["values"] = all_SUM_of_asia5
    final_dataframe_of_asia5.sort_values(by=['values'], inplace=True, ascending=False)

    # Bar chart for the top 3 countries
    final_dataframe_of_asia5.head(3).plot.bar(x="country", y="values", rot=70,
                                              title="Top 3 COUNTRIES from period 2011 - 2020",
                                              ylabel="Number of travelers [in millions]")
    #print(final_dataframe_of_asia5.head(3))
    sum_of_top3 = 26713289 + 23203897 + 11005817
    mean_of_top3 = sum_of_top3/3
    print("The mean value for the top 3 countries is " + str((round((mean_of_top3), 2))))
    print("The total no. of visitors for the top 3 countries is " + str((sum_of_top3)))

    plt.savefig("top3Countries.png")

    # Bar chart for all the countries
    final_dataframe_of_asia5.plot.bar(x="country", y="values", rot=70,
                                      title="ALL COUNTRIES from period 2011 - 2020",
                                      figsize=(10, 10),
                                      ylabel="Number of travelers [in millions]", )
    plt.savefig("allCountries.png")





