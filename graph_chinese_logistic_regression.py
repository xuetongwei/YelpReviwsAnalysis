import pandas as pd
import matplotlib.pyplot as plt;
import numpy as np
width = 0.2

if __name__ == "__main__":
    print("CHINESE FOOD LOGISTIC REGRESSION")
    x = -0.0932
    y = 1.2278
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
    
    a = -1.9539
    b = -4.1982    
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
    
    m = 0.2799
    n = 1.4642
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
        
    p = 0.5450    
    q = 0.5450
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
    
    x = -0.4439
    y = 0.8445
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
    
    a = -0.3598
    b = -1.4100    
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
    
    m = -0.2488
    n = -0.6352
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
        
    p = -1.3277    
    q = -1.3277
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
    
    x = 0.2787
    y = 0.5273
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
    
    a = 14.5504
    b = 13.9628   
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
    
    m = -0.4976
    n = -0.1766
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
        
    p = -15.7727    
    q = -15.7727
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
    
    x = 0.0690
    y = 0.0763
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
    
    a = 1.5642
    b = 2.1078    
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
    
    m = 0.0494
    n = -0.3108
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
        
    p = -2.6684    
    q = -2.6684
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
    
    x = 0.0387
    y = -0.7208
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
    
    a = 0.8646
    b = 2.0651    
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
    
    m = 0.3059
    n = 0.5772
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
        
    p = -2.4427    
    q = -2.4427
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