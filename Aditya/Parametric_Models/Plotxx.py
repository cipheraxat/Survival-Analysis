import matplotlib.pyplot as plt


def plot_details(category, positon1, positon2, positon3, positon4, figure):

    positon1.set_title("LogNatural")
    positon2.set_title("Weibull")
    positon3.set_title("LogLogistic")
    positon4.set_title("Exponential")

    plt.suptitle(
        'Using different parametric models to see the churn probability on the basis of User '+category)

    figure.text(0.5, 0.04, 'Timeline', ha='center')
    figure.text(0.04, 0.5, 'Probability', va='center', rotation='vertical')
    plt.savefig('Images/Churn_by_'+category+'.jpeg')
    plt.show()
