import pandas as pd

df1 = pd.read_csv('casepercent_withmaskmandate_nograph.csv')


n = df1['casepercent'].mean() #gets mean case percentage
print("The average case percentage per all 50 states is:", n)
df_nomask = df1.loc[(df1['Percent of 2020']) == 0.000000] #gets states that had no mask mandate
tota_zero = (len(df_nomask.index)) #gets the number of them
df2 = df1.loc[(df1['casepercent'] > n) & (df1['Percent of 2020'] == 0.000000)] #gets states that had no mandate and had above the average case percent
zer_above_avg = (len(df2.index)) #gets the number of them
percent_0_above_avg = (zer_above_avg/tota_zero)*100
print('The number of states that never had a mask mandate and are above the average case percentage is:', zer_above_avg)
print('The percent of states that never had a mask mandate and are above the average case percentage is:', percent_0_above_avg)

n = df1['casepercent'].mean()
df_mask = df1.loc[(df1['Percent of 2020']) == 1.000000] #gets states that always had a mask mandate
tota_zero = (len(df_mask.index))
df3 = df1.loc[(df1['casepercent'] > n) & (df1['Percent of 2020'] == 1.000000)] #gets the states that always had a mandate and were above the case percent
zer_above_avg = (len(df3.index))
percent_0_above_avg = (zer_above_avg/tota_zero)*100 
print('The number of states that always had a mask mandate and are above the average case percentage is:', zer_above_avg)
print('The percent of states that always had a mask mandate and are above the average case percentage is:', percent_0_above_avg)

n = df1['casepercent'].mean()
df_abovehlf = df1.loc[(df1['Percent of 2020']) > 0.5] #gets states that had a mask percentage over 50% off 2020
tota_zero = (len(df_abovehlf.index))
df4 = df1.loc[(df1['casepercent'] > n) & (df1['Percent of 2020'] > 0.5)] #gets states that had a mandate over 50% of the time and above the percentage
zer_above_avg = (len(df4.index))
percent_0_above_avg = (zer_above_avg/tota_zero)*100
print('The number of states that had a mask mandate over 50 percent of the time in 2020 is:', tota_zero)
print('The percent of states that had a mask mandate over 50 percent of the time in 2020 and are above the average case percentage is:', percent_0_above_avg)

n = df1['casepercent'].mean()
df_bigpop = df1.loc[(df1['Population']) > 10000000] #gets states with population over 10,000,000
tota_state = (len(df_bigpop.index))
df5 = df1.loc[(df1['casepercent'] > n) & (df1['Population'] > 10000000)] #gets states that also had over the case percenatge
zer_above_avg = (len(df5.index))
percent_0_above_avg = (zer_above_avg/tota_state)*100
print('The number of states that have a population over 10,000,000 is:', tota_state)
print('The percentage of states that have a population over 10,000,000 and are above the average case percent is', percent_0_above_avg)
print("The two states above the average are Illinois and Georgia, Illinois always had a mandate while Georgia never did.")