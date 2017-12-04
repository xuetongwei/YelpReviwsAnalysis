import matplotlib.pyplot as plt;
import numpy as np
width = 0.2

if __name__ == "__main__":    
    print("LINEAR REGRESSION")
    
    x = 0.3155
    y = -0.0733
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
    
    a = 1.0548
    b = 2.0916    
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
    
    m = -0.0705
    n = 0.2214
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
    
    p = 2.0944   
    q = 2.0944
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
