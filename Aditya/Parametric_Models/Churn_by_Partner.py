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


def churn_by_partner(model, axes):
    model = model  # instantiate the class to create an object of required model

    groups = data['Partner']
    # group i1 , having the pandas series for the 1st cohort
    k1 = (groups == 'No')
    # group i2 , having the pandas series for the 2nd cohort
    k2 = (groups == 'Yes')

    # fit the model for 1st cohort
    model.fit(T[k1], E[k1], label='Do not have a partner')
    a1 = model.plot(ax=axes)

    # fit the model for 2nd cohort
    model.fit(T[k2], E[k2], label='Have a partner')
    model.plot(ax=axes)


# Churn by partner for the lognormal model
churn_by_partner(LogNormalFitter(), axes[0][0])
# Churn by partner for the weibull model
churn_by_partner(WeibullFitter(), axes[0][1])
# Churn by partner for the loglogistic model
churn_by_partner(LogLogisticFitter(), axes[1][0])
# Churn by partner for the Exponential model
churn_by_partner(ExponentialFitter(), axes[1][1])

# Function for adding subtitles and labels
plot_details('Partner', axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1], fig)
