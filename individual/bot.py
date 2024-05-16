import telebot;
import random
from datetime import datetime

bot = telebot.TeleBot("6422402394:AAGIl16syLNJqAYA8Vj6S8icFDgRlBzVaRM")


print("initiating")
random.seed(datetime.now().timestamp())

def get_random_question():
  print("get random question")
  with open("questions.txt", "r",1, encoding="utf-8") as file:
    lines = file.readlines()
    return random.choice(lines)
  
def get_random_task():
  print("get random task")
  with open("tasks.txt", "r",1, encoding="utf-8") as file:
    lines = file.readlines()
    return random.choice(lines)




score_player1 = 0
score_player2 = 0
truth_count1 = 0
truth_count2 = 0
current_player = 0



def game_logic(context):
  global score_player1
  global score_player2
  global truth_count1
  global truth_count2
  global current_player
  msg = ""
  resultmenu = "\n/done - выполнил✅ \n/aborted - отказался❌"
  againmenu = "\n\n🔄/start заново"
  truthmenu = "\n🩵/truth - правда"
  daremenu = "\n💜/dare - действие"
  
  
  if context == "truth":
    if current_player == 0:
      truth_count1-=1
    if current_player == 1:
      truth_count2-=1
    msg += "Игрок {current_player}: ОЧКИ {score_player}\n".format(current_player=current_player+1,
      score_player = (score_player2 if bool(current_player) else score_player1)                                          
    )
    msg += get_random_question()
    msg += "\n"
    msg += resultmenu + againmenu
    return msg
    
  if context == "done":
    current_player = (current_player+1)%2
    smallmenu = "Игрок {current_player}: ОЧКИ {score_player}\nправда доступно {truth_count1_player}\n".format(
      current_player=current_player+1,
      truth_count1_player=(truth_count2 if bool(current_player) else truth_count1),
      score_player = (score_player2 if bool(current_player) else score_player1)
    )
    msg+=smallmenu
    if current_player == 0:
      if truth_count1 != 0:
        msg += truthmenu
    if current_player == 1:
      if truth_count2 != 0:
        msg += truthmenu
    msg += daremenu
    msg += againmenu
    return msg
  
  if context == "dare":
    if current_player == 0:
      truth_count1 = 2
    if current_player == 1:
      truth_count2 = 2
    
    smallmenu = "Игрок {current_player}: ОЧКИ {score_player}\nправда доступно {truth_count1_player}\n".format(
      current_player=current_player+1,
      truth_count1_player=(truth_count2 if bool(current_player) else truth_count1),
      score_player = (score_player2 if bool(current_player) else score_player1)
    )
    msg += smallmenu
    msg += get_random_task()
    msg += resultmenu
    msg += againmenu
    return msg
  
  if context == "aborted":
    if current_player == 0:
      score_player1-=1
    if current_player ==1:
      score_player2-=1
    if (score_player1 < 0) or (score_player2 < 0):
      msg += "Игрок {current_player} проиграл".format(current_player=current_player+1)
      msg += againmenu
      return msg
    else:
      current_player = (current_player+1)%2
      smallmenu = "Игрок {current_player}: ОЧКИ {score_player}\nправда доступно {truth_count1_player}\n".format(
      current_player=current_player+1,
      truth_count1_player=(truth_count2 if bool(current_player) else truth_count1),
      score_player = (score_player2 if bool(current_player) else score_player1)
      )
      msg+=smallmenu
      if current_player == 0:
        if truth_count1 != 0:
          msg += truthmenu
      if current_player == 1:
        if truth_count2 != 0:
          msg += truthmenu
      msg += daremenu
      msg += againmenu
      return msg
  
  return "error /start"
    
      
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  global score_player1
  global score_player2
  global truth_count1
  global truth_count2
  global current_player


  if message.text == "/start":
    welcome_message = """Привет👋🏻, давай поиграем в правда 💭 ли действие 🗯?
/begin - начать игру
Выбирать правду можно не больше 2ух раз подряд
Потом придется выполнять действие
Сверху указаны очки игроков 
откажешься больше 3-ех раз - проиграл
За каждый отказ вы теряете 1 очко
Веселой игры!
"""
    bot.send_message(message.from_user.id, welcome_message)
    
    
  if message.text == "/begin":
    current_player = 0
    score_player1 = 3
    score_player2 = 3
    truth_count1 = 2
    truth_count2 = 2
    bot.send_message(message.from_user.id, "Игра началась") 
    smallmenu = "Игрок {current_player}: ОЧКИ {score_player}\nправда доступно {truth_count1_player}\n".format(
      current_player=current_player+1,
      truth_count1_player=(truth_count2 if bool(current_player) else truth_count1),
      score_player = (score_player2 if bool(current_player) else score_player1)
    )
    msg = ""
    msg += smallmenu
    msg +="\n🩵/truth - правда\n💜/dare - действие\n\n🔄/start заново"
    print("player:",current_player)
    print("/begin")
    bot.send_message(message.from_user.id, msg)
    
    
  if message.text == "/truth":
    msg = game_logic("truth")
    bot.send_message(message.from_user.id, msg)
  
  if message.text == "/dare":
    msg = game_logic("dare")
    bot.send_message(message.from_user.id, msg)
    
  
  if message.text == "/done":
    msg = game_logic("done")
    bot.send_message(message.from_user.id, msg)
  
  if message.text == "/aborted":
    msg = game_logic("aborted")
    bot.send_message(message.from_user.id, msg)
    
    
    
    
    
    
    
    
bot.polling(non_stop=True,interval=0)

