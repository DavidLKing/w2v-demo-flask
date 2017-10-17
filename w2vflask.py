from flask import Flask
from flask import request
from flask import render_template
import gensim
import os

app = Flask(__name__)

print("wording wordvectors")
wordvecs = gensim.models.KeyedVectors.load_word2vec_format('./vectors.bin', binary=True) 

def results2html(results):
    print("results", results)
    outstring = ""
    for result in results:
        outstring += result[0] + ": " + str(result[1]) + "<br>"
    return outstring


@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', method=['POST'])
def my_form_post():
    word1 = request.form('word1')
    word2 = request.form('word2')
    word3 = request.form('word3')
    sim = results2html(wordvecs.most_similar([w1, w2], [], topn=10))

    return sim

if __name__ == '__main__':
    app.run()
