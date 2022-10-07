import libs.chilexpress as ce
import libs.secret.tokenlib as se
import libs.sqldriver as fl
import telebot
import time,os,sys
import sqlite3 as sql

bot = telebot.TeleBot(se.TELEGRAM_TOKEN)

def restart():
    bot.send_message(se.TELEGRAM_CHAT_ID, 'Restarting...', parse_mode='Markdown')
    os.execv(sys.executable, ['python3'] + sys.argv)
    

def compare():
    with sql.connect('tracker.db') as conn:
        c = conn.cursor()
        SQLite_select_query = """SELECT * from tracking_lugar ORDER BY tiempo DESC LIMIT 2"""
        fl.itemIns('tracker.db', 'tracking_lugar', ce.dondeEsta(), time.strftime("%d/%m/%Y"))
        mensajes_list = []
        for row in c.execute(SQLite_select_query):
            mensajes_list.append(row)
        print(mensajes_list)
        if mensajes_list[0] == mensajes_list[1]:
            #bot.send_message(se.TELEGRAM_CHAT_ID, ce.dondeEsta(), parse_mode='Markdown')
            fl.itemIns('tracker.db', 'tracking_lugar', ce.dondeEsta(), time.strftime("%d/%m/%Y"))
            print(".")
        else:
            fl.itemIns('tracker.db', 'tracking_lugar', ce.dondeEsta(), time.strftime("%d/%m/%Y"))
            bot.send_message(se.TELEGRAM_CHAT_ID, ce.dondeEsta(), parse_mode='Markdown')
    c.close()
    

if __name__ == '__main__':
    try:
        count = 0
        while count < 300:
            if not os.path.isfile('tracker.db'): fl.createDB('tracker.db', 'tracking_lugar', 'lugar', 'tiempo')
            compare()
            time.sleep(60)
            count += 1
        bot.infinity_polling(timeout=20, long_polling_timeout = 5)
    except KeyboardInterrupt:
        print('Bye!')
        
        