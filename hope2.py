import pandas as p                                 
from sklearn.linear_model import LinearRegression   
from sklearn.model_selection import train_test_split
apple = {
    "Year": [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971, 1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962, 1961, 1960],
    "Inflation Rate (%)":[5.65,6.7, 5.13, 6.62, 3.73, 3.94, 3.33, 4.95, 4.91, 6.67, 10.02, 9.48, 8.91, 11.99, 10.88, 8.35, 6.37, 5.8, 4.25, 3.77, 3.81, 4.3, 3.78, 4.01, 4.67, 13.23, 7.16, 8.98, 10.22, 10.25, 6.33, 11.79, 13.87, 8.97, 7.07, 9.38, 8.8, 8.73, 5.56, 8.32, 11.87, 7.89, 13.11, 11.35, 6.28, 2.52, 8.31, -7.63, 5.75, 28.6, 16.94, 6.44, 3.08, 5.09, -0.58, 3.24, 13.06, 10.8, 9.47, 13.36, 2.95, 3.63, 1.7, 1.78]
}
weee=[1.78, 1.7, 3.63, 2.95, 13.36, 9.47, 10.8, 13.06, 3.24, -0.58, 5.09, 3.08, 6.44, 16.94, 28.6, 5.75, -7.63, 8.31, 2.52, 6.28, 11.35, 13.11, 7.89, 11.87, 8.32, 5.56, 8.73, 8.8, 9.38, 7.07, 8.97, 13.87, 11.79, 6.33, 10.25, 10.22, 8.98, 7.16, 13.23, 4.67, 4.01, 3.78, 4.3, 3.81, 3.77, 4.25, 5.8, 6.37, 8.35, 10.88, 11.99, 8.91, 9.48, 10.02, 6.67, 4.91, 4.95, 3.33, 3.94, 3.73, 6.62, 5.13, 6.7, 5.65]

df = p.DataFrame(apple)
x = df["Year"].values.reshape(-1,1)
y = df["Inflation Rate (%)"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
model = LinearRegression()
model.fit(x_train,y_train)


def inpuuts():
    print("Enter the initial year")
    year = int(input())
    print("Enter the final year")
    year2 = int(input())
    if year>year2:
        year=year+year2
        year2=year-year2
        year=year-year2
    index1=year-1960
    index2=year2-1960
    print("enter initial amount")
    moni=float(input())
    return year,year2,index1,index2,moni

def infla(year,year2,moni):
    if (year<1960 and year2<1960) or (year>2023 and year2 >2023):
        for i in range(year,year2) :
            a = model.predict([[i]])[0]
            moni+=a*(moni/100) 
        return moni

    elif(year<1960 and year2>=1960 and year2<=2023):
        for i in range(year,1960) :
           a = model.predict([[i]])[0]
           moni+=a*(moni/100) 
        for i in range(index2):
            moni+=weee[i]*(moni/100)
        return moni
            
    elif(year>=1960 and year<=2023 and year2>2023):
        for i in range(index1,64):
            moni+=weee[i]*(moni/100)
        for i in range(2024,year2):
            a = model.predict([[i]])[0]
            moni+=a*(moni/100) 
        return moni
    
    elif(year>=1960 and year<=2023) and (year2>=1960 and year2<=2023):
        for i in range(index1,index2):
            moni+=weee[i]*(moni/100)
        return moni


    elif year<1960 and year2>2023:
        for i in range(year,1960) :
           a = model.predict([[i]])[0]
           moni+=a*(moni/100) 
        moni*=82.6887
        for i in range(2024,year2):
            a = model.predict([[i]])[0]
            moni+=a*(moni/100)
        return moni 
    
        
print("Welcome to Inflation Calculator and Investment Comparision")
print("Type 1 on your keyboard for Inflation Calculator\nType 2 on your keyboard for Investment Comparision(Inflation is calculated here as well)\nType any other integer  to exit")
choice=int(input())
if(choice==1):
    returned_values = inpuuts()
    year, year2, index1, index2, moni = returned_values
    print(f"The inflated value of {moni} in {year2} is : {infla(year,year2,moni):.2f}")
elif(choice==2):
    returned_values = inpuuts()
    year, year2, index1, index2, moni = returned_values
    print("Enter the final amount after investment")
    finalmoni=int(input())
    if(finalmoni>=infla(year,year2,moni)):
        print("Your Investment has Combatted Inflation Succesfully")
        print(f"Your investment has a profit of {(finalmoni-infla(year,year2,moni)):.2f} compared to the inflation")
        print(f"Your investment has a profit percentage of {((finalmoni-infla(year,year2,moni))/infla(year,year2,moni))*100:.2f} % compared to the inflation")

    else:
        print("Your Investment has Failed to Combat Inflation")
        print(f"Your investment has a loss of {-(finalmoni-infla(year,year2,moni)):.2f} compared to the inflation")
        print(f"Your investment has a loss percentage of {-((finalmoni-infla(year,year2,moni))/infla(year,year2,moni))*100:.2f} % compared to the inflation")



    



#print(f"predicted inflation rate for {year} : {a:.2f}%")
