# Chilexpress bot
Bot de telegram que te avisa cuando hay un nuevo evento relacionado con tu envio.

### Dependencias
````sh
pip3 install telebot,time,os,sys,sqlite3,requests,json
````


### Pasos:

Ve a `/libs/secret/` , renombra `example_tokenlib.py` y edita el archivo con tus datos.

	tokenlib.py ~
	
	    TELEGRAM_TOKEN = '' # 
		 ↳  Es  el token que te da BotFather

	    TELEGRAM_CHAT_ID = ''

		↳  El chat id de algun grupo/canal que tengas. El bot no está pensado para chat personal.

	    CHILEXPRESS_TOKEN = '' 

		↳  Es el OTP o numero de seguimiento que te da Chilexpress.


Vuelves a la carpeta principal  y ejecutas bot.py

```sh
python3 bot.py
````
Listo!, si quieres dejar corriendo en un vps te recomiendo TMUX, creas una sesion nueva, la abres, corres el bot y desatachas y te vas.
