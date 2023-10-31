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
plt.ylabel("Hourly wage in 2022 Dollars")
plt.ylim(10,30)
plt.title('Wage by Gender')
plt.legend()
plt.show()

#calculate difference in wages
wage_gap["Difference"] = wage_gap["Men Median"] - wage_gap["Women Median"]
wage_mw = wage_gap[["Date", "Difference", "Men Median", "Women Median"]].sort_values(by=["Difference"])
print(wage_mw)

#plot of gender gap
plt.figure(4)
plt.plot("Date", "Gap (Regression-based)", data=wage_gap )
plt.xlabel("Year")
plt.ylabel("Percent Gap from Men")
plt.title("Wage Gap for Women")
plt.ylim(5, 40)
plt.show()

#track gap as percentage
gap_mw = wage_gap[["Date", "Gap (Regression-based)"]].sort_values(by=["Gap (Regression-based)"])
print("Gap:", gap_mw)

#plot of women Median wages
plt.figure(3)
plt.plot("Date", "Median", data=wage_am, label= "Median", color='k')
plt.plot("Date", "Black Women Median", data=wage_gap, label= "Black Women", color='g')
plt.plot("Date", "Hispanic Women Median", data=wage_gap, label= "Hispanic Women", color='c')
plt.plot("Date", "Black Men Median", data=wage_gap, label= "Black Men", color='g', alpha=0.65)
plt.plot("Date", "Hispanic Men Median", data=wage_gap, label= "Hispanic Men", color='c', alpha=0.65)
plt.xlabel("Year")
plt.ylabel("Hourly wage in 2022 Dollars")
plt.title("Wages by Race and Gender")
plt.ylim(10,30)
plt.legend()
plt.show()

#racial wage difference
wage_bw["Black Difference"] = wage_bw["White Median"] - wage_bw["Black Median"]
wage_hw["Hispanic Difference"] = wage_hw["White Median"] - wage_hw["Hispanic Median"]
bw = wage_bw[["Date", "Black Difference"]]
hw = wage_hw[["Date", "Hispanic Difference"]]
diff_bh = pd.merge(left=bw, right=hw)
print(diff_bh.head(), diff_bh.describe())

#plot of Median wages by race
plt.figure(5)
plt.plot("Date",  "Median", data=wage_am, label= "Median", color='k')
plt.plot("Date", "White Median", data=wage_bw, label= "White Median", color='m')
plt.plot("Date", "Black Median", data=wage_bw, label= "Black Median", color='g')
plt.plot("Date", "Hispanic Median", data=wage_hw, label= "Hispanic Median", color='c')
plt.xlabel("Year")
plt.ylabel("Hourly wage in 2022 Dollars")
plt.title("Wages by Race")
plt.ylim(10,30)
plt.legend()
plt.show()

#racial wage gap
wage_hw["Gap Hispanic"] = wage_hw["Gap (Regression-based)"]
wage_bw["Gap Black"] = wage_bw["Gap (Regression-based)"]
gap_b = wage_bw[["Date", "Gap Black"]]
gap_h = wage_hw["Gap Hispanic"]
gap_bh = pd.concat([gap_b, gap_h], axis=1)
print(gap_bh.sort_values(by=["Gap Black"]), gap_bh.sort_values(by=["Gap Hispanic"]), gap_bh.describe())


#plot gap by race
plt.figure(6)
plt.plot("Date", "Gap (Regression-based)", data=wage_bw, label= "Black Wage Gap", color='g')
plt.plot("Date", "Gap (Regression-based)", data=wage_hw, label= "Hispanic Wage Gap", color='c')
plt.ylabel("Percent Gap from White Earnings")
plt.title("Wage Gap for Racial Minorities")
plt.xlabel("Year")
plt.legend()
plt.ylim(5, 40)
plt.show()


