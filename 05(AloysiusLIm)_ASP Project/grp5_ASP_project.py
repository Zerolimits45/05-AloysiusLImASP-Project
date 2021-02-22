import pandas as pd
import matplotlib.pyplot as plt


class Asia5():

    imva = pd.read_excel('IMVA.xls')  # import xls file that is in the same folder

    asia5 = [imva['Brunei Darussalam'], imva['Indonesia'], imva['Malaysia'], imva['Myanmar'], imva['Philippines'],
             imva['Thailand'], imva['Vietnam'],
             imva['China'], imva['Hong Kong SAR'], imva['Taiwan'], imva['Japan'], imva['South Korea'], imva['Bangladesh'],
             imva['India'], imva['Pakistan'], imva['Sri Lanka'],
             imva['Iran'], imva['Israel'], imva['Kuwait'], imva['Saudi Arabia'],
             imva['United Arab Emirates']]  #selcting all the regions in asia

    columns_in_asia_5_as_INDEX = range(len(list(asia5)))  # range of columns in asia5 this is 0 - 20
    all_SUM_of_asia5 = []  # it is to store the 10 year data sum
    all_COUNTRY_of_asia5 = []  # it is to store all the 20 country

    #print(columns_in_asia_5_as_INDEX)
    #print(asia5[0].name)

    count_values = 0
    count_number_of_columns = 0
    for col_id in columns_in_asia_5_as_INDEX:
        #print(asia5[col_id].name)  # header of the column
        #print("Column " + str(count_number_of_columns) + " out of 20 in Asia5")
        sum_of_each_col = []  # forgot to reset
        count_number_of_columns = count_number_of_columns + 1
        for value_index in range(len(asia5[col_id])):

            if asia5[col_id][value_index] == asia5[col_id][396] or value_index > 396:  # value_index is the integer index for whole 516 #forgot to set it up
                if asia5[col_id][value_index] == 'na':
                    asia5[col_id][value_index] = '0'
                sum_of_each_col.append(int(asia5[col_id][value_index].replace(',', ''))) # use this for months and years too



        all_SUM_of_asia5.append(sum(sum_of_each_col))
        all_COUNTRY_of_asia5.append(asia5[col_id].name)
        #print("this is the sum of each column: " + str(sum(all_SUM_of_asia5)))
        #print("---------------")

        sum_2011 = sum(sum_of_each_col[0:11])
        sum_2012 = sum(sum_of_each_col[12:23])
        sum_2013 = sum(sum_of_each_col[34:45])
        sum_2014 = sum(sum_of_each_col[34:45])
        sum_2015 = sum(sum_of_each_col[45:56])
        sum_2016 = sum(sum_of_each_col[56:67])
        sum_2017 = sum(sum_of_each_col[67:78])
        sum_2018 = sum(sum_of_each_col[78:89])
        sum_2019 = sum(sum_of_each_col[89:100])
        sum_2020 = sum(sum_of_each_col[100:111])

        print("Year 2011")
        print(sum_of_each_col[0:11])
        print("------")
        print("Year 2012")
        print(sum_of_each_col[12:23])
        print("------")
        print("Year 2013")
        print(sum_of_each_col[34:45])
        print("------")
        print("Year 2014")
        print(sum_of_each_col[34:45])
        print("------")
        print("Year 2015")
        print(sum_of_each_col[45:56])
        print("------")
        print("Year 2016")
        print(sum_of_each_col[56:67])
        print("------")
        print("Year 2017")
        print(sum_of_each_col[67:78])
        print("------")
        print("Year 2018")
        print(sum_of_each_col[78:89])
        print("------")
        print("Year 2019")
        print(sum_of_each_col[89:100])
        print("------")
        print("Year 2020")
        print(sum_of_each_col[100:111])


    final_dataframe_of_asia5 = pd.DataFrame()

    #final_dataframe_of_asia5.head(3)

    final_dataframe_of_asia5["country"] = all_COUNTRY_of_asia5
    final_dataframe_of_asia5["values"] = all_SUM_of_asia5
    final_dataframe_of_asia5.sort_values(by=['values'], inplace=True, ascending=False)

    # Bar chart for the top 3 countries
    final_dataframe_of_asia5.head(3).plot.bar(x="country", y="values", rot=70,
                                              title="Top 3 COUNTRIES from period 2011 - 2020",
                                              ylabel="Number of travelers [in millions]")
    #print(final_dataframe_of_asia5.head(3)
    sum_of_top3 = 26713289 + 23203897 + 11005817
    mean_of_top3 = sum_of_top3/3
    print("")
    print("The mean value for the top 3 countries is " + str((round((mean_of_top3), 2))))
    print("The total no. of visitors for the top 3 countries is " + str((sum_of_top3)))

    plt.savefig("top3Countries.png")

    # Bar chart for all the countries
    final_dataframe_of_asia5.plot.bar(x="country", y="values", rot=70,
                                      title="ALL COUNTRIES from period 2011 - 2020",
                                      figsize=(10, 10),
                                      ylabel="Number of travelers [in millions]", )
    plt.savefig("allCountries.png")





