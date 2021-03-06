import pandas
import numpy
import joblib

from sklearn.linear_model import LinearRegression

ds=pandas.read_csv("SalaryData.csv")

X = ds["Experience"].values.reshape(30,1)
Y = ds["Salary"]

mind = LinearRegression()
mind.fit(X ,Y )

# Predicts the output using this file
print("\n \t \t \t****Welcome Guys to the Machine Learning , Salary Predication*******************")
print(" ")
print(" ")
output = int(input("\t \t \tEnter your Job  exprerience :"))

ans=mind.predict([[output]])
print(" ")
print("YOUR ESTIMATED SALARY =")
print(ans)
print(" ")

# OR Load the model and predict using other file
joblib.dump( mind ,"SalaryModel.pkl")
