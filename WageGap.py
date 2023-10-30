#import packages
import pandas as pd
import matplotlib.pyplot as plt

#import data from csv
wage_gap = pd.read_csv("C:/Users/Z/Documents/GitHub/zeesetash/WageGap/EPI Data Library - Gender wage gap.csv")
wage_am = pd.read_csv("C:/Users/Z/Documents/GitHub/zeesetash/WageGap/EPI Data Library - Medianaverage hourly wages.csv")
wage_bw = pd.read_csv("C:/Users/Z/Documents/GitHub/zeesetash/WageGap/EPI Data Library - Black-white wage gap.csv")
wage_hw = pd.read_csv("C:/Users/Z/Documents/GitHub/zeesetash/WageGap/EPI Data Library - Hispanic-white wage gap.csv")
print(wage_gap.describe(), wage_am.describe(), wage_bw.describe(), wage_hw.describe())



#plot of men, women, and overall
plt.figure(1)
plt.plot("Date", "Men Median", data=wage_gap, label= "All Men", color='b')
plt.plot("Date", "Women Median", data=wage_gap, label= "All Women", color='r')
plt.plot("Date", "Median", data=wage_am, label= "Median", color='k')
plt.xlabel("Year")
plt.ylabel("Median wage in 2022 Dollars")
plt.ylim(10,30)
plt.title('Wage by Gender')
plt.legend()
plt.show()

#plot of gender gap
plt.figure(4)
plt.plot("Date", "Gap (Median)", data=wage_gap )
plt.xlabel("Year")
plt.ylabel("Percent Gap of Median")
plt.title("Wage Gap for Women")
plt.show()

#plot of men Median wages
plt.figure(2)
plt.plot("Date", "Median", data=wage_am, label= "Median", color='k')
plt.plot("Date", "Men Median", data=wage_gap, label= "All Men", color='b')
plt.plot("Date", "White Men Median", data=wage_gap, label= "White Men", color='m')
plt.plot("Date", "Black Men Median", data=wage_gap, label= "Black Men", color='g')
plt.plot("Date", "Hispanic Men Median", data=wage_gap, label= "Hispanic Men", color='c')
plt.xlabel("Year")
plt.ylabel("Median wage in 2022 Dollars")
plt.title("Men's wages by Race")
plt.ylim(10,30)
plt.legend()
plt.show()


#plot of women Median wages
plt.figure(3)
plt.plot("Date", "Median", data=wage_am, label= "Median", color='k')
plt.plot("Date", "Women Median", data=wage_gap, label= "All Women", color='r')
plt.plot("Date", "White Women Median", data=wage_gap, label= "White Women", color='m')
plt.plot("Date", "Black Women Median", data=wage_gap, label= "Black Women", color='g')
plt.plot("Date", "Hispanic Women Median", data=wage_gap, label= "Hispanic Women", color='c')
plt.xlabel("Year")
plt.ylabel("Median wage in 2022 Dollars")
plt.title("Women's wages by Race")
plt.ylim(10,30)
plt.legend()
plt.show()

#plot of Median wages by race
plt.figure(5)
plt.plot("Date",  "Median", data=wage_am, label= "Median", color='k')
plt.plot("Date", "White Median", data=wage_bw, label= "White Median", color='m')
plt.plot("Date", "Black Median", data=wage_bw, label= "Black Median", color='g')
plt.plot("Date", "Hispanic Median", data=wage_hw, label= "Hispanic Median", color='c')
plt.xlabel("Year")
plt.ylabel("Median wage in 2022 Dollars")
plt.title("Wages by Race")
plt.ylim(10,30)
plt.legend()
plt.show()