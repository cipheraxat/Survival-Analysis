# importing the required python libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import NelsonAalenFitter

# reading the data into python dataframe
telco_data = pd.read_csv('telco_customer.csv')

# filtering and preparing the data to the required format
telco_data['TotalCharges']=pd.to_numeric(telco_data['TotalCharges'],errors='coerce')
telco_data['Churn']=telco_data['Churn'].apply(lambda x: 1 if x == 'Yes' else 0 )

# the duration varaiable column
T = telco_data['tenure']

# the target event(occures/not occured) column
E = telco_data['Churn']

# creating a NelsonAalenFitter object and fitting the duration and event colum data to it
naf = NelsonAalenFitter()
naf.fit(T,event_observed=E)

# printing out the NA Estimations (cummulative hazard rates)
print(naf.cumulative_hazard_.head())
print(naf.cumulative_hazard_.tail())

# utility function to plot the NA Estimator
def plot_estimator():
    naf.plot(figsize=(12,10),label="NA Estimator")
    plt.xlabel('Tenure',size=15)
    plt.ylabel('NA Estimate(Commulative Hazard Function Estimator)',size=13)
    plt.title('Plotting NA Estimate against the churning tenure of a customer',size=15)
    plt.legend(prop={'size': 16})

# utility function to smoothen the curve and compare between the plots
def plot_function(category1,category2,bandwidth,column_name):
    small_ans = (telco_data[column_name] == category1)
    naf.fit(T[small_ans], event_observed=E[small_ans], label= category1)
    ax = naf.plot_hazard(bandwidth=bandwidth,figsize=(10,8))
    naf.fit(T[~small_ans], event_observed=E[~small_ans], label= category2)
    naf.plot_hazard(ax=ax, bandwidth=bandwidth,figsize=(10,8))
    plt.legend(title = column_name,prop={'size': 12})
    plt.title('Curve Smoothening and Comparing({})'.format(column_name),size=12)

# utility function for a plot generation to explain the smoothness and bandwidth factor visually
def smooth_analysis():
    n = 10
    while(n<=100):
        naf.plot_hazard(bandwidth=n,figsize=(15,13),label=n)
        n+=10
    plt.tight_layout()
    plt.legend(title= 'Bandwidth',prop={'size': 12})

# plotting the NA Estimator
plot_estimator()

# getting a visualization of bandwidth and smoothness of the NA Estimator
smooth_analysis()

# smoothing the NA Estimator
naf.plot_hazard(bandwidth=10,figsize=(12,10),title="Smoother NA Estimator",label="NA Estimator")

# smoothing and comparing according to the column's entry
plot_function('Male','Female',3,'gender')
plot_function('Yes','No',3,'PhoneService')
plot_function('Yes','No',3,'Partner')
plot_function('Yes','No',3,'Dependents')
plot_function('Yes','No',3,'PaperlessBilling')
