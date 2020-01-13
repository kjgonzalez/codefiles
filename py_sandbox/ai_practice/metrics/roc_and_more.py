'''
want to demonstrate a bit of info about ROC curve, AUROC, and PR curves as
    metrics. will use scikit-learn for items

'''

import numpy as np
import sklearn.metrics as skm
import matplotlib.pyplot as plt
np.random.seed(0)
# generate some fake data
ndat = 30
k=0.30 # factor for how much prediction deviates from ytrue. k:[0.0-0.5]
ytrue = np.random.randint(2,size=ndat)
ypred = ((ytrue*k+(1-k)*np.random.rand(ndat))).round(0).astype(int)
yconf = np.random.rand(ndat)/2.1+ypred*0.5

print('data')
print('ytrue:',ytrue)
print('ypred:',ypred)
print('yconf:',yconf.round(2))
CM = skm.confusion_matrix(ytrue,ypred)
print('CM:\n',CM,sep='')

ROC = skm.roc_curve(ytrue,yconf)
AUROC = skm.roc_auc_score(ytrue,yconf)
print('AUROC:',AUROC)

PR = skm.precision_recall_curve(ytrue,yconf)
AP = skm.average_precision_score(ytrue,yconf)
print('AP:',AP)

f,p=plt.subplots(1,2)
p[0].plot(ROC[0],ROC[1],'r.-')
p[0].set_title('ROC')
p[0].set_xlim([0,1])
p[0].set_ylim([0,1])
p[0].set_xlabel('FPR')
p[0].set_ylabel('TPR')
p[0].grid()
p[0].set_aspect('equal')

p[1].plot(PR[1],PR[0],'r.-')
p[1].set_title('PR')
p[1].set_xlim([0,1])
p[1].set_ylim([0,1])
p[1].set_xlabel('recall')
p[1].set_ylabel('precision')
p[1].grid()
p[1].set_aspect('equal')



plt.show()

# import ipdb; ipdb.set_trace()
# eof
