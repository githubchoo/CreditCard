#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/",methods=["GET", "POST"])
def index():
    if request.method=="POST":
        Income = float(request.form.get("income"))
        Age = float(request.form.get("age"))
        Loan = float(request.form.get("loan"))
        print(Income,Age,Loan)
        model = joblib.load("RandomForest")
        pred = model.predict([[Income, Age, Loan]])
        print(pred)
        s = "The probability of default is: " + str(pred)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="2"))


# In[4]:


if __name__ == "__main__":
    app.run()


# In[ ]:




