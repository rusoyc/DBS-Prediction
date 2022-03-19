#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


app=Flask(__name__)


# In[3]:


import joblib

@app.route("/", methods=["GET","POST"])
def i():
    if request.method == "POST":
        rate = request.form.get("rates")
        print(rate)
        model = joblib.load("DBS_Reg")
        pred = model.predict([[float(rate)]])
        s = "The predicted DBS share price is " + str(pred)
        print(s)
        
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="2"))


# In[ ]:


if __name__=="__main__":
    app.run()

