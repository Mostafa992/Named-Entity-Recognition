from flask import Flask,render_template,url_for,request
import spacy
from spacy import displacy
from flaskext.markdown import Markdown


nlp = spacy.load('en_core_web_sm')
doc = nlp(u'This is a sentence.')





app=Flask(__name__)
Markdown(app)



@app.route("/")
def index():
  return render_template("index.html")


@app.route("/extract",methods=["GET","POST"])
def extract():
  if request.method=="POST":
    rawtext=request.form['rawtext']
    docx=nlp(rawtext)
    output=displacy.render(docx,style="ent")
  return render_template("result.html",rawtext=rawtext,output=output)



if __name__=="__main__":
  app.run(debug=True)

