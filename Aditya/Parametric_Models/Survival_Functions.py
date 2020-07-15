import matplotlib.pyplot as plt
from lifelines import (WeibullFitter, ExponentialFitter,
                       LogNormalFitter, LogLogisticFitter)

import pandas as pd
data = pd.read_csv('Dataset/telco_customer.csv')
data['tenure'] = pd.to_numeric(data['tenure'])
data = data[data['tenure'] > 0]


# Replace yes and No in the Churn column to 1 and 0. 1 for the event and 0 for the censured data.
data['Churn'] = data['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
fig, axes = plt.subplots(2, 2, figsize=(
    16, 12))

T = data['tenure']
E = data['Churn']

wbf = WeibullFitter().fit(T, E, label='WeibullFitter')
ef = ExponentialFitter().fit(T, E, label='ExponentialFitter')
lnf = LogNormalFitter().fit(T, E, label='LogNormalFitter')
llf = LogLogisticFitter().fit(T, E, label='LogLogisticFitter')

wbf.plot_survival_function(ax=axes[0][0])
ef.plot_survival_function(ax=axes[0][1])
lnf.plot_survival_function(ax=axes[1][0])
llf.plot_survival_function(ax=axes[1][1])

plt.suptitle(
    'Implementation of  Paramteric Models to create survival functions on the teleco dataset')

fig.text(0.5, 0.04, 'Timeline', ha='center')
fig.text(0.04, 0.5, 'Probability', va='center', rotation='vertical')
plt.savefig('Images/SurvivalFunctions.jpeg')
plt.show()
