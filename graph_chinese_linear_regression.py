import matplotlib.pyplot as plt;
import numpy as np
width = 0.2

if __name__ == "__main__":    
    print("CHINESE FOOD LINEAR REGRESSION")
    
    x = 0.1022
    y = -0.4219
    objects = ("Ambience 1", "Ambience 2")
    position = np.arange(len(objects))
    performance = (x,y)
    sample = plt.bar(position,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 5")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    a = 1.3179
    b = 2.3376    
    objects = ("Food 1", "Food 2")
    position = np.arange(len(objects))
    performance = (a,b)
    sample = plt.bar(position+width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 5")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    m = 0.0376
    n = 0.2916
    objects = ("Service 1", "Service 2")
    position = np.arange(len(objects))
    performance = (m,n)
    sample = plt.bar(position+2*width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 5")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    p = 1.7249   
    q = 1.7249
    objects = ("Positive", "Negative")
    position = np.arange(len(objects))
    performance = (p,q)
    sample = plt.bar(position+3*width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient') 
    plt.title("Star 5")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom') 
    plt.legend("AFSI")
    plt.show()
