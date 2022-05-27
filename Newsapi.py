#AKbar padhke sunaoo

import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.speak(str)




if __name__ == '__main__':
    speak("News for today")
    # speak("Subho novoborsho sobai k ,       sobai k amar pronam")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=b29dbda187b8472f887990b60c9b8150"
    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news..Listen Carefully")
        # a = input("Enter")
        # if a == "stop":
        #     break


