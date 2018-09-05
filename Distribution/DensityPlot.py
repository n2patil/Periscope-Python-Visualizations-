#Try example SQL Query using Periscope Demo Connection: Select spend from demo.ad_spend

#INPUT: Single column in DataFrame to represent Density, Note: Periscope SQL output is imported as a pandas dataframe variable called "df"
#OUTPUT: Seaborn Density Plot, for more details on optional parameters check out this seaborn documentation: https://seaborn.pydata.org/generated/seaborn.kdeplot.html 


import pandas as pd
import seaborn as sns

#set columnName equal to the column name of your SQL output
columnName='spend'
def densityPlot(columnName):
	dPlot=sns.kdeplot(df[columnName], shade=True, color='purple')
  
  #option to use the parameter bw to control bandwidth of density plot
  #dPlot=sns.kdeplot(df[columnName], shade=True, color='purple', bw=2)
  
	return dPlot
  
periscope.output(densityPlot(columnName))
