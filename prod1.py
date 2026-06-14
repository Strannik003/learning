# У сообщения есть:
# текст
# автор
# время отправки
# Нужно реализовать метод:
# is_spam()
# Сообщение считается спамом если:
# длина текста больше 200 символов
# или в тексте больше 3 ссылок
# или текст состоит из одинаковых слов


import re 

Spam = False
def is_spam(x):
    x["Spam status"]=False 

    if len(x["Message"]) > 200:
        x["Spam status"] = True
        return x
    if len(re.findall(r"https?://", x["Message"])) >= 3:
        x["Spam status"] = True
        return x
    
    if len(set(x["Message"].split())) == 1:
        x["Spam status"] = True
        return x

    
if __name__ =='__main__':
    
    message = {
        "Author": "Anton",
        "Message": "spam spam spam ",
        "Date": "01.01.2026"

    }
    is_spam(message)
    print(message)
      Remove-Item .git\index.lock