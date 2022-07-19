# Analysis-of-Effectiveness-of-State-Mask-Mandate-in-2020
Using available data, I analyzed the correlation between a state wide mask mandate and its effectiveness to stop the spread of Covid in 2020

Using the python Pandas and BeautifulSoup library in 'covidbypop.py':
First, using the CDC's database, I got a CSV for all the cases of every state in 2020.
I then got the population of all the states and merged them into one table.
Next I calculated the percentage of the state with covid and sorted the table by that.
This table can be seen on 'covid2020.csv'

Next I gathered information about how much of 2020 each particular state had a mask mandate and added a column in the csv for it.
I calculated the percentage of the 9 months with the pandemic (April-December) in 2020 that each state had a mandate and made that a column.
This can be seen on 'casepercent_withmaskmandate_graph.csv'

I created a graph that compares the percentage of cases with the percentage of mandate.
This can be seen on 'covidgraph.png'

I then used the same libraries in analysis in 'covidpop_analysis.py'
I used the table to produce some interesting data:

  1. The average case percentage per all 50 states is: 0.06292329808
  2. The number of states that never had a mask mandate and are above the average case percentage is: 8
  3. The percent of states that never had a mask mandate and are above the average case percentage is: 80.0
  4. The number of states that always had a mask mandate and are above the average case percentage is: 3
  5. The percent of states that always had a mask mandate and are above the average case percentage is: 33.33333333333333
  6. The number of states that had a mask mandate over 50 percent of the time in 2020 is: 30
  7. The percent of states that had a mask mandate over 50 percent of the time in 2020 and are above the average case percentage is: 43.333333333333336
  8. The number of states that have a population over 10,000,000 is: 9
  9. The percentage of states that have a population over 10,000,000 and are above the average case percent is 11.11111111111111
  10. The two states above the average are Illinois and Georgia, Illinois always had a mandate while Georgia never did.


Conclusions:
As we have seen since the start of the pandemic there has been a lot of talk about how effective masks are and if they help. The data here shows many things but is also not conclusive. There are many factors that have an effect on the number of cases, not only masks. There isn't a clear correlation between mask mandates and covid cases but it seems to have a positive effect in many states.
