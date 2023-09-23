





    
import json
import requests
import urllib
import random
import os

admin = "J00RJ"

TOKEN = ''
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
USERNAME_BOT = "test_0_1bot"
gplink = "https://t.me/+c80KRM_lZwhmYTQ1"



hom = urllib.parse.quote_plus("""['keyboard' => [[['text'=>"داستان 📑"],['text'=>"🎞️ فیلم"],['text'=>"💾 گیف"],['text'=>"🖼 عکس"]],],'resize_keyboard' => true]""")


tarjome = {"keyboard":[[{"text":"فارسی به انگلیسی"},{"text":"انگلیسی به فارسی"}],[{"text":"عربی به فارسی"},{"text":"فارسی به عربی"}]],"resize_keyboard": True}



key_start = {"inline_keyboard": [
    [{"text":"Use New Number","callback_data":"new-num"},{"text":"Set Message","callback_data":"set-msg"}],
    [{"text": "send message", "callback_data": "send-msg"}],
    [{"text":"Generate Range","callback_data":"set-range"},{"text":"Edit Profile","callback_data":"edit-pro"}],
    [{"text": "Support", "url": "https://t.me/" + admin}]
                                 ]
             }


key_back = {"inline_keyboard":[[{"text":"برگشت 🔙","callback_data":"backstart"}]]}

key_edit_pro = {"inline_keyboard": [
    [{"text":"Edit name","callback_data":"edit-name"},{"text":"Edit Bio","callback_data":"edit-bio"}],
    [{"text": "Edit Usarname", "callback_data": "edit-id"}],
    [{"text":"برگشت 🔙","callback_data":"backstart"}]]}

suptxt = "این گروه متعلق به ربات 𝐖𝐀𝐓𝐈𝐍𝐎𝐑 می‌باشد ! \n پشتیبانی و پاسخ به سوالات برخی از کاربران ربات در این گروه انجام می‌شود . \n \n در گروه پشتیبانی قوانین زیر را رعایت کنید : \n \n ① چت ممنوع و از ارسال سوالات نامرتبط خودداری کنید ! \n ② فحش و فحاشی به اعضای گروه، اکیدا ممنوع می‌باشد و در صورت مشاهده برخورد جدی خواهد شد ! \n ③ ارسال تبلیغات به هر شکل در این گروه ممنوع است از جمله تبلیغات : ربات، کانال، گروه، وب سایت و ... \n ④ در صورت مشاهده از گروه مسدود و در صورت لزوم از تمامی گروه‌های ربات 𝑤𝑎𝑡𝑖𝑛𝑜𝑟 محروم خواهید شد ! \n ⑤ راهنمایی و پاسخ به پرسشها برای عموم آزاد می‌باشد \n \n لطفا به نکات بالا توجه فرمایید تا محیطی \n دوستانه و صمیمی را در کنار یکدیگر داشته باشیم 🌹 \n "+ gplink

helptxt = "🔺 راهنمای بخش های مختلف ربات واتینور \n 🔻 بصورت تفکیک شده به شرح ذیل می‌باشد: \n \n 🔵 توجه کنید که تمامی قابلیت ها و امکانات ربات در این راهنما گنجانده شده است !"


butback = {"keyboard":[[{"text":"برگشت"}]],"resize_keyboard": True}


start_txt = "گزینه ای از منوی زیر انتخاب کنید"


edit_pro_txt = "کدام قسمت را میخواهید ویرایش کنید؟"

new_num_txt = "شماره جدید را بدون 0 و +98 وارد کنید \n مانند : 9141560780"

set_msg_txt = "پیام مورد نظر را ارسال کنید"


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


if(os.path.isfile("./db.json") == False):
    f = open("db.json","w+")
    t = {
        'users': [],
        'user': []
        }
    f.write(json.dumps(t))
    f.close()


def jdb():
    f = open("db.json","r")
    x = json.loads(f.read())
    return x


def sv(data):
    x = json.dumps(data)
    f = open("db.json","w")
    f.write(x)
    f.close()


def new_nums(ranger,count):
    my_nums = []
    for x in range(count - 1):
        num = ranger + ""
        for y in range(6):
            z = random.randint(0, 9)
            num = num + z
            print(y)
        my_nums.append(num)
    return my_nums


def set_number():
    print("")



def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    db = jdb()
    for update in updates["result"]:
        if update.get("callback_query") != None:
            if update.get("callback_query", {}).get("data") != None:
                callback = update["callback_query"]
                data = callback["data"]
                msgid = callback["message"]["message_id"]
                idchat = callback["message"]["chat"]["id"]
                fid = callback["message"]["from"]["id"]
                firstname = callback["from"]["first_name"]

                db = jdb()


                if data == "set-range":
                    o = {"user":{fid:{"step":"set-range2"}}}
                    with open ('db.json','w') as ok:
                        json.dump(o,ok,indent=4)

                    editMessage(idchat,msgid,"رنج مورد نظر را وارد کنید \n مانند : 914")
                    editmsgkey(idchat,msgid,key_back)
                elif data == "backstart":


                    editMessage(idchat,msgid,start_txt)
                    editmsgkey(idchat,msgid,key_start)
                elif data == "new-num":


                    editMessage(idchat,msgid,new_num_txt)
                    editmsgkey(idchat,msgid,key_back)
                elif data == "set-msg":


                    editMessage(idchat,msgid,set_msg_txt)
                    editmsgkey(idchat,msgid,key_back)
                elif data == "edit-pro":
                    editMessage(idchat,msgid,edit_pro_txt)
                    editmsgkey(idchat,msgid,key_edit_pro)
                elif data == "send-msg":
                    send_message(fid,"ارسال پیام آغاز شد")


        # if update.get("message") != None:
        #     if update.get("message", {}).get("photo") != None:
        #         pic = update["message"]["photo"]
        #         chay = update["message"]["chat"]["id"]

        #         db = jdb()

        #     if update.get("message", {}).get("text") != None:
        #         text = update["message"]["text"]
        #         msg = update["message"]["message_id"]
        #         chatid = update["message"]["chat"]["id"]
        #         firt = update["message"]["from"]["first_name"]
        #         fid = update["message"]["from"]["id"]
        #         tp = update["message"]["chat"]["type"]
        #         with open ('db.json',"r") as ton:
        #             z = json.load(ton)
        #             step = z["user"][fid]["step"]

        #         print(text)


                if text == "/start" and tp == "private":
                    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
                    payload = {
                    'chat_id': chatid,
                    'text': start_txt,
                    'reply_markup': key_start
                    }
                    requests.post(url, json=payload)



                    o = {"user":{fid:{"step":"none"}}}
                    with open ('db.json','w') as ok:
                        json.dump(o,ok,indent=4)




                elif text and step == "set-range2":

                    un = new_nums(text,50)
                    o = {"user":{fid:{"step":"none"}}}
                    with open ('db.json','w') as ok:
                        json.dump(o,ok,indent=4)


                    with open ('num.json','w') as pk:
                        json.dump(un,pk,indent=4)

                    send_message(fid,"در حال ساخت شماره")
                    numbers = ""
                    for t in un:
                        numbers = "\n" + un[t]
                    msgtxt = "لیست شماره ها : \n\n" + numbers
                    send_message(fid,msgtxt)

                elif text and step == "set-num2":
                    db["user"][fid]["num"] = text
                    db["user"][fid]["step"] = "none"
                    sv(db)
                    set_number(text)
                    send_message(fid,"شماره تنظیم شد")

                elif text and step == "set-msg2":
                    db["user"][fid]["msg"] = text
                    db["user"][fid]["step"] = "none"
                    sv(db)
                    send_message(fid,"پیام تنظیم شد")


                elif text == "جوک":
                    x = requests.get('http://api.codebazan.ir/jok')
                    send_message(chatid, x.text + "\n 😂 [ @sotiykhande ]••", msg)
                    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
                    payload = {'chat_id': "5386925200",'text': "What is this?",'reply_markup': {"inline_keyboard": [[{"text": "➕ افزودن به گروه ➕", "url": "https://t.me/WATINORBOT?startgroup=add"}],[{"text": "➕ افزودن به گروه ➕", "url": "https://t.me/WATINOR BOT?startgroup=add"}]]}}
                    r = requests.post(url, json=payload)
                    sendmessage(chatid, "جونم🤤", str(msg),tarjome)
                    sendmessage(chatid,"bye <code>0000</code>" + str(msg) + str(update), msg, tarjome)
                elif text == "اسب":
                    send_image("IMG_20220607_175147_018.jpg",chatid)
                    send_document("data.json",chatid)
                elif text == "code":
                    d=get_url("https://www.pythonanywhere.com/user/rezaarrow/shares/7d07ce479cb542698509381c8cf6bcf6/")
                    send_message(chatid,str(d),msg)
                elif text == "من":
                    you = getchat(fid,chatid)
                    send_message(chatid,"your id: " + str(fid) + "\n your name: " + str(firt) + "\n your statuse: " + you,msg)
                elif text == "cbi":
                    sendpm(chatid,"ok frind",msg,"")


def bot(method , datas):
    url = f'https://api.telegram.org/bot{TOKEN}/'  + method
    v = requests.post(url, json=datas)
    return v

def send_message(chat_id, text):
    tot = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(tot, chat_id)
    get_url(url)

def sendmessage(chat_id, text, rep, keys):
    tot = urllib.parse.quote_plus(text)
    gbord = urllib.parse.quote_plus(str(keys))
    url = URL + "sendMessage?text={}&chat_id={}&reply_to_message_id={}&reply_markup={}".format(tot, chat_id, rep, gbord)
    get_url(url)


def sendpm(c,t,m,k):
    bot('sendmessage',{"chat_id": c,"text": t,"reply_to_message_id": m,"reply_markup": k})

def editMessage(idcat,msgid,txt):
    bot('editMessageText',{"chat_id": idcat,"message_id": msgid,"text": txt})

def editmsgkey(idcat,pm,key):
    bot('editmessagereplymarkup',{"chat_id": idcat,"message_id": pm, "reply_markup": key})


def getchat(userid,chatid):
    url = URL + "getChatMember?user_id={}&chat_id={}".format(userid, chatid)
    response = requests.get(url)
    content = response.content.decode("utf8")
    con = json.loads(content)
    s = con["result"]["status"]
    return s


def send_document(doc, chat_id):
    files = {'document': open(doc, 'rb')}
    requests.post(URL + "sendDocument?chat_id={}".format(chat_id), files=files)


def send_image(doc, chat_id):
    files = {'photo': open(doc, 'rb')}
    requests.post(URL + "sendPhoto?chat_id={}".format(chat_id), files=files)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if updates is not None:
            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                echo_all(updates)


if __name__ == '__main__':
    main()
send_message(chat_id, message)