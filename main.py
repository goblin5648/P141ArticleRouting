from flask import Flask, jsonify
import pandas as pd
from demographic_filtering import output
from content_filtering import get_recommendations

articles_data = pd.read_csv('C:\Users\elven\Downloads\C141\C141\P141\data.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_articles=articles_data[["original_title","poster_link","release_date","runtime","weighted_rating"]]

# variables to store data
liked_articles=[]
unliked_articles=[]

# method to fetch data from database
def assign_val():
  a_data={
    "original_title":all_articles.iloc[0,0],
    "poster_link": all_articles.iloc[0,1],
    "release_date": all_articles.iloc[0,2] or "N/A",
    "duration": all_articles.iloc[0,3],
    "rating":all_articles.iloc[0,4]/2
  }
  return a_data

# /movies api
@app.route("/article")
def get_article():
  articles_data=assign_val()
  return jsonify({
    "data":articles_data,
    "status":"success"
  })

# /like api
@app.route("/like")
def get_like():
  global all_articles
  articles_data=assign_val()
  liked_articles.append(articles_data)
  all_articles.drop([0],inplace=True)
  all_articles=all_articles.reset_index(drop=True)
  return jsonify({
    "data":liked_articles,
    "status":"success"
  })

# /dislike api
@app.route("/dislike")
def get_unliked():
  global all_articles
  articles_data=assign_val()
  unliked_articles.append(articles_data)
  all_articles.drop([0],inplace=True)
  all_articles=all_articles.reset_index(drop=True)
  return jsonify({
    "data":unliked_articles,
    "status":"success"
  })

if __name__ == "__main__":
  app.run(debug=True)