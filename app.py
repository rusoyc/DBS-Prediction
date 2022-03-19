#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


app = Flask(__name__)


# In[3]:


import joblib

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        rate = request.form.get("rates")
        print(rate)
        model = joblib.load("DBS linear regression")
        #pred = model.predict([[float(rate)]])
        #s = "The predicted DBS share price is " + str(pred)
        return(render_template("index.html",result=rate))
    else:
        return(render_template("index.html",result="DBS predictor"))


# In[ ]:


if __name__=="__main__":
    app.run()

