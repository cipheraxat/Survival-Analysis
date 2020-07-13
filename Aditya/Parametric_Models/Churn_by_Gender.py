import matplotlib.pyplot as plt
from lifelines import LogNormalFitter, LogLogisticFitter, WeibullFitter, ExponentialFitter
import pandas as pd
from Plotxx import plot_details

# Processing the data as per requirements
data = pd.read_csv('Dataset/telco_customer.csv')
data['tenure'] = pd.to_numeric(data['tenure'])
data = data[data['tenure'] > 0]
data['Churn'] = data['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
T = data['tenure']
E = data['Churn']

fig, axes = plt.subplots(2, 2, figsize=(16, 12))


def churn_by_gender(model, axes):
    model = model  # instantiate the class to create an object for required model

    groups = data['gender']
    # group i1 , having the pandas series for the 1st cohort
    j1 = (groups == 'Male')
    # group i2 , having the pandas series for the 2nd cohort
    j2 = (groups == 'Female')

    # fit the model for 1st cohort
    model.fit(T[j1], E[j1], label='Male')
    a1 = model.plot(ax=axes)

    # fit the model for 2nd cohort
    model.fit(T[j2], E[j2], label='Female')
    model.plot(ax=axes)


# Churn by gender for the lognormal model
churn_by_gender(LogNormalFitter(), axes[0][0])
# Churn by gender for the weibull model
churn_by_gender(WeibullFitter(), axes[0][1])
# Churn by gender for the loglogistic model
churn_by_gender(LogLogisticFitter(), axes[1][0])
# Churn by gender for the Exponential model
churn_by_gender(ExponentialFitter(), axes[1][1])

# Function for adding subtitles and labels
plot_details('Gender', axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1], fig)
