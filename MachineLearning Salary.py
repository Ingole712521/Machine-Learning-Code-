{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " \t \t \t****Welcome Guys to the Machine Learning , Salary Predication*******************\n",
      " \n",
      " \n",
      "\t \t \tEnter your Job  exprerience :5\n",
      " \n",
      "YOUR ESTIMATED SALARY =\n",
      "[73042.01180594]\n",
      " \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['SalaryModel.pkl']"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas\n",
    "import numpy\n",
    "import joblib\n",
    "\n",
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "ds=pandas.read_csv(\"SalaryData.csv\")\n",
    "\n",
    "X = ds[\"Experience\"].values.reshape(30,1)\n",
    "Y = ds[\"Salary\"]\n",
    "\n",
    "mind = LinearRegression()\n",
    "mind.fit(X ,Y )\n",
    "\n",
    "# Predicts the output using this file\n",
    "print(\"\\n \\t \\t \\t****Welcome Guys to the Machine Learning , Salary Predication*******************\")\n",
    "print(\" \")\n",
    "print(\" \")\n",
    "output = int(input(\"\\t \\t \\tEnter your Job  exprerience :\"))\n",
    "\n",
    "ans=mind.predict([[output]])\n",
    "print(\" \")\n",
    "print(\"YOUR ESTIMATED SALARY =\")\n",
    "print(ans)\n",
    "print(\" \")\n",
    "\n",
    "# OR Load the model and predict using other file\n",
    "joblib.dump( mind ,\"SalaryModel.pkl\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
