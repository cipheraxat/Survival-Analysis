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


def churn_by_subscribe(model, axes):

    model = model  # instantiate the class to create an object for the input model

    # Two Cohorts are compared. 1. Streaming TV Not Subsribed by Users, 2. Streaming TV subscribed by the users.
    groups = data['StreamingTV']
    # group i1 , having the pandas series for the 1st cohort
    i1 = (groups == 'No')
    # group i2 , having the pandas series for the 2nd cohort
    i2 = (groups == 'Yes')

    # fit the model for 1st cohort
    model.fit(T[i1], E[i1], label='Not Subscribed StreamingTV')
    a1 = model.plot(ax=axes)

    # fit the model for 2nd cohort
    model.fit(T[i2], E[i2], label='Subscribed StreamingTV')
    model.plot(ax=axes)


# Churn by subscribe for the lognormal model
churn_by_subscribe(LogNormalFitter(), axes[0][0])
# Churn by subscribe for the weibull model
churn_by_subscribe(WeibullFitter(), axes[0][1])
# Churn by subscribe for the loglogistic model
churn_by_subscribe(LogLogisticFitter(), axes[1][0])
# Churn by subscribe for the Exponential model
churn_by_subscribe(ExponentialFitter(), axes[1][1])


# Function for adding subtitles and labels
plot_details('Subscribed', axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1], fig)
