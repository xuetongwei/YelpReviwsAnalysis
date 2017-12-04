import pandas as pd
import matplotlib.pyplot as plt;
import numpy as np
width = 0.2

if __name__ == "__main__":
    print("LOGISTIC REGRESSION")
    x = -0.3052
    y = 0.2518
    objects = ("Ambience 1", "Ambience 2")
    position = np.arange(len(objects))
    performance = (x,y)
    sample = plt.bar(position,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 1")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    a = -1.6570
    b = -3.8933    
    objects = ("Food 1", "Food 2")
    position = np.arange(len(objects))
    performance = (a,b)
    sample = plt.bar(position+width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 1")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    m = 0.3924
    n = -0.8872
    objects = ("Service 1", "Service 2")
    position = np.arange(len(objects))
    performance = (m,n)
    sample = plt.bar(position+2*width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 1")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
        
    p = 0.1467    
    q = 0.1467
    objects = ("Positive", "Negative")
    position = np.arange(len(objects))
    performance = (p,q)
    sample = plt.bar(position+3*width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Intercept')
    plt.title("Star 1")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom') 
    plt.legend("AFSI")
    plt.show()
    
    x = -0.5274
    y = 0.5064
    objects = ("Ambience 1", "Ambience 2")
    position = np.arange(len(objects))
    performance = (x,y)
    sample = plt.bar(position,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 2")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    a = 0.0761
    b = -1.3146    
    objects = ("Food 1", "Food 2")
    position = np.arange(len(objects))
    performance = (a,b)
    sample = plt.bar(position+width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 2")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    m = -0.0575
    n = -0.5644
    objects = ("Service 1", "Service 2")
    position = np.arange(len(objects))
    performance = (m,n)
    sample = plt.bar(position+2*width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 2")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
        
    p = -1.8080    
    q = -1.8080
    objects = ("Positive", "Negative")
    position = np.arange(len(objects))
    performance = (p,q)
    sample = plt.bar(position+3*width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 2")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom') 
    plt.legend("AFSI")
    plt.show()
    
    x = 0.0605
    y = 0.1051
    objects = ("Ambience 1", "Ambience 2")
    position = np.arange(len(objects))
    performance = (x,y)
    sample = plt.bar(position,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 3")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    a = 1.0976
    b = 0.4187    
    objects = ("Food 1", "Food 2")
    position = np.arange(len(objects))
    performance = (a,b)
    sample = plt.bar(position+width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 3")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    m = -0.5014
    n = -0.2942
    objects = ("Service 1", "Service 2")
    position = np.arange(len(objects))
    performance = (m,n)
    sample = plt.bar(position+2*width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 3")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
        
    p = -2.4350    
    q = -2.4350
    objects = ("Positive", "Negative")
    position = np.arange(len(objects))
    performance = (p,q)
    sample = plt.bar(position+3*width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 3")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom') 
    plt.legend("AFSI")
    plt.show()
    
    x = 0.3794
    y = -0.1577
    objects = ("Ambience 1", "Ambience 2")
    position = np.arange(len(objects))
    performance = (x,y)
    sample = plt.bar(position,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 4")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    a = 0.7476
    b = 1.1716    
    objects = ("Food 1", "Food 2")
    position = np.arange(len(objects))
    performance = (a,b)
    sample = plt.bar(position+width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 4")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    m = -0.1792
    n = -0.1992
    objects = ("Service 1", "Service 2")
    position = np.arange(len(objects))
    performance = (m,n)
    sample = plt.bar(position+2*width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 4")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
        
    p = -1.7907    
    q = -1.7907
    objects = ("Positive", "Negative")
    position = np.arange(len(objects))
    performance = (p,q)
    sample = plt.bar(position+3*width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Sentiment Coefficient')
    plt.title("Star 4")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom') 
    plt.legend("AFSI")
    plt.show()
    
    x = 0.3794
    y = -0.1577
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
    
    a = 0.8299
    b = 2.0784    
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
    
    m = 0.2548
    n = 0.4308
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
        
    p = -2.2218    
    q = -2.2218
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
    