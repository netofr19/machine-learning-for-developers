import matplotlib.pyplot as plt

def lin_regplot(X, y, model):

    plt.scatter(X, y, c='steelblue', edgecolor='white', s=70)
    plt.plot(X, model.predict(X), color='black', lw=2)
    
