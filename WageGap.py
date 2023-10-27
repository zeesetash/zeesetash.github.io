#import packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import data from csv
wage_gap = pd.read_csv("C:/Users/Z/Documents/GitHub/zeesetash/WageGap/EPI Data Library - Gender wage gap.csv")
print(wage_gap.head(), wage_gap.info())


#create separate dataframes for wage and wage gap
gap=[col for col in wage_gap.columns if 'Gap' in col]
wage_df = wage_gap.drop(gap, axis=1)
gap_df = wage_gap[gap]


#set up combined plot
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
fig.suptitle("Wages Over Time")

#plot of men average wages
ax1.plot("Date", "Men Average", data=wage_df, label= "All Men")
ax1.plot("Date", "White Men Average", data=wage_df, label= "White Men")
ax1.plot("Date", "Black Men Average", data=wage_df, label= "Black Men")
ax1.plot("Date", "Hispanic Men Average", data=wage_df, label= "Hispanic Men")
ax1.legend()


#plot of women average wages
ax2.plot("Date", "Women Average", data=wage_df, label= "All Women")
ax2.plot("Date", "White Women Average", data=wage_df, label= "White Women")
ax2.plot("Date", "Black Women Average", data=wage_df, label= "Black Women")
ax2.plot("Date", "Hispanic Women Average", data=wage_df, label= "Hispanic Women")
ax2.legend()

fig.tight_layout()
plt.show()
