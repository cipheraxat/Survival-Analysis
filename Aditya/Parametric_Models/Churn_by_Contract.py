import matplotlib.pyplot as plt
from lifelines import LogNormalFitter, LogLogisticFitter, WeibullFitter, ExponentialFitter
import pandas as pd
from Plotxx import plot_details

# Processing the data as per the requirements
data = pd.read_csv('Dataset/telco_customer.csv')
data['tenure'] = pd.to_numeric(data['tenure'])
data = data[data['tenure'] > 0]
data['Churn'] = data['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
T = data['tenure']
E = data['Churn']


fig, axes = plt.subplots(2, 2, figsize=(16, 12))


def churn_by_contract(model, axes):

    model = model  # instantiate the class to create an object for choosen model

    # Three cohorts are compared on the basis of the contract
    groups = data['Contract']
    x1 = (groups == 'Month-to-month')
    x2 = (groups == 'Two year')
    x3 = (groups == 'One year')

    model.fit(T[x1], E[x1], label='Month-to-month')
    ax = model.plot(ax=axes)

    model.fit(T[x2], E[x2], label='Two year')
    ax1 = model.plot(ax=axes)
    ac1 = model.plot

    model.fit(T[x3], E[x3], label='One year')
    model.plot(ax=axes)


# Churn by contract for the lognormal model
churn_by_contract(LogNormalFitter(), axes[0][0])
# Churn by contract for the weibull model
churn_by_contract(WeibullFitter(), axes[0][1])
# Churn by contract for the loglogistic model
churn_by_contract(LogLogisticFitter(), axes[1][0])
# Churn by contract for the Exponential model
churn_by_contract(ExponentialFitter(), axes[1][1])

# Function for adding subtitles and labels
plot_details('Contract', axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1], fig)
