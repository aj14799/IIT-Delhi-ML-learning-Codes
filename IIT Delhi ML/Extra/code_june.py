


import pandas
import numpy

df = pandas.read_csv(r"E:\MLIoT\ML\dataset\spam.csv",encoding="latin-1")

# drop the unnecessary columns
df = df[["v1","v2"]]

# separate the features and laels
x = df["v2"]
y = df["v1"]

import re
for i in range(len(x)):
    x[i] = re.sub("[\d]+[0-9a-zA-Z]","",x[i])

######################################################
d="my mobile number is 98989898989 and what is your number"
re.sub("[\d]+[0-9a-zA-Z]","",d)
##############################
#count vecorization
from sklearn.feature_extraction.text import CountVectorizer
cvec = CountVectorizer(stop_words="english",lowercase=True)

# apply count vectorization on x to convert it into vectors
xnew = cvec.fit_transform(x).toarray()

print(xnew.shape)
print(cvec.get_feature_names())

#####################################################
#####################################################
from sklearn.model_selection import train_test_split
xtr,xts,ytr,yts = train_test_split(xnew,y,test_size=0.2)

#######################################################
# trian the model to identify spam emails
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# train the model
model.fit(xtr,ytr)

# check the accuracy of the model
ypred = model.predict(xts)
from sklearn.metrics import accuracy_score
accuracy_score(yts,ypred)
########################################
####################################

email = ["""Hi yash, you have won $10000 if you just answer
         one question, and your question is  - what is 
         capital of India? you can claim your price by
          calling us at 08989897897 and deposit $2000."""]

email = cvec.transform(email)
model.predict(email)

## export the model
from sklearn.externals import joblib
joblib.dump(model,"spam_model.pkl")
joblib.dump(cvec,"cvec.pkl")


