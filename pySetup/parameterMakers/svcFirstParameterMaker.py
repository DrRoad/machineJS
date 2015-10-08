import math

def makeParams(X, y, globalArgs, dev):

    # at some point in the future when we have figured out whether we have a probability or a classifiaction problem, we can set 'probability' equal to True only when we have a probability problem. that property just enables us to invoke predict_proba, but it slows down training time noticeably
    # an easy way to split this out would be to have one svm that is shrinking, and one that is not
    parameters_to_try = {
        # 'shrinking': False,
        # 'C': [1, 10, 100, 1000], 
        'gamma': [0.001, 0.0001], 
        'kernel': ['rbf']
    }

    # if dev:
    #     parameters_to_try.pop('C', None)
    #     parameters_to_try.pop('kernel', None)
    #     parameters_to_try.pop('max_features', None)
        
    return parameters_to_try
