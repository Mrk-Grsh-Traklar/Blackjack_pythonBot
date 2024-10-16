import telebot as tb
import random as rnd
from telebot import types

Token = "TOKEN"
print('started')
bot = tb.TeleBot(Token)
@bot.message_handler(commands=['start,play,open_up,help'])
@bot.message_handler(regexp='start')
def send_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    help = types.KeyboardButton('help')
    main = types.KeyboardButton('main')
    markup.add(help, main)
    bot.send_message(message.chat.id, f"Hello! {message.from_user.first_name}\nIf you want to see commands print /help", reply_markup=markup)




@bot.message_handler(regexp='BlackJack')
def send_random_num(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2 = types.KeyboardButton('next')
    markup.add(item2)
    rndNum = rnd.randint(1,12)
    rndNum2 = rnd.randint(1,12)
    rndNum3 = rnd.randint(1,12)

    print(bot.send_message(message.chat.id, f'Your score:{rndNum} \nto take another card print /next', reply_markup= markup))
    @bot.message_handler(regexp='next')
    def send_eshcare(message):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('continue')
        markup.add(item1) 
        userNum = rndNum + rndNum2
        if userNum > 21:
            print(bot.send_message(message.chat.id, f'You lose'))
        elif userNum == 21:
            print(bot.send_message(message.chat.id, f'You win'))
        else:
            print(bot.send_message(message.chat.id, f'Your score:{userNum}(+{rndNum2}) \nto take another card print /continue ', reply_markup= markup))
        
        @bot.message_handler(regexp='continue')
        def send_pisun(message):
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)          
            main = types.KeyboardButton('main')        
            open_up = types.KeyboardButton('open_up')
            markup.add(open_up, main)
            userNum1 = userNum + rndNum3
            if userNum1 == 21:
                print(bot.send_message(message.chat.id, f'You win',reply_markup=markup))
            elif userNum1 > 21:
                print(bot.send_message(message.chat.id, f'You lose',reply_markup=markup))
            else:
                print(bot.send_message(message.chat.id, f'Your score:{userNum1}(+{rndNum3}) \nfind out the result /open_up ', reply_markup=markup))
                @bot.message_handler(regexp='open_up')
                def send_result(message):
                    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                    main = types.KeyboardButton('main')
                    markup.add(main)
                    rndBot = rnd.randint(3,21)
                    if userNum1 > rndBot:
                        print(bot.send_message(message.chat.id, f'You won {userNum1}:{rndBot} ', reply_markup=markup))
                    elif userNum1 < rndBot:
                        print(bot.send_message(message.chat.id, f'You lose {userNum1}:{rndBot}',reply_markup=markup))
                    else:
                        print(bot.send_message(message.chat.id, f'draw{userNum1}:{rndBot}',reply_markup=markup ))

     
@bot.message_handler(regexp='help')
def help(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    BlackJack = types.KeyboardButton('BlackJack')
    rndDice = types.KeyboardButton('guess_the_number')
    games = types.KeyboardButton('games')
    support = types.KeyboardButton('support')
    markup.add(BlackJack, rndDice, games, support)
    print(bot.send_message(message.chat.id,f' /BlackJack-играть в BlackJack \n/guess_the_number-играть в угадай число \n/games-мини игры \n/support-поддержка', reply_markup=markup))

                           
                           
                           
                           




    
@bot.message_handler(regexp='main')
def main_menu(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    BlackJack = types.KeyboardButton('BlackJack')
    rndDice = types.KeyboardButton('guess_the_number')
    help = types.KeyboardButton('help')
    games = types.KeyboardButton('games')
    support = types.KeyboardButton('support')
    markup.add(BlackJack, rndDice, help, games, support)
    bot.send_message(message.chat.id, f'вы в главном меню, {message.from_user.first_name}', reply_markup=markup)

@bot.message_handler(regexp='games')
def mini_games(message):

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    football = types.KeyboardButton('football')
    basketball = types.KeyboardButton('basketball')
    cube = types.KeyboardButton('cube')
    casino = types.KeyboardButton('casino')
    main = types.KeyboardButton('main')
    darts = types.KeyboardButton('darts')
    bowl = types.KeyboardButton('bowl')
    markup.add(football,basketball,cube,casino, bowl, darts, main)
    bot.send_message(message.chat.id, f'кайфуй', reply_markup=markup)
    @bot.message_handler(regexp='football')
    def football(message):
        bot.send_dice(message.chat.id,'⚽')
        bot.send_message(message.chat.id,reply_markup=markup)
    @bot.message_handler(regexp='basketball')
    def basketball(message):
        bot.send_dice(message.chat.id,'🏀')
        bot.send_message(message.chat.id,reply_markup=markup)
    @bot.message_handler(regexp='cube')
    def cube(message):
        bot.send_dice(message.chat.id,'🎲')
        bot.send_message(message.chat.id,reply_markup=markup)
    @bot.message_handler(regexp='casino')
    def casino(message):
        bot.send_dice(message.chat.id,'🎰')
        bot.send_message(message.chat.id,reply_markup=markup)
    @bot.message_handler(regexp='bowl')
    def casino(message):
        bot.send_dice(message.chat.id,'🎳')
        bot.send_message(message.chat.id,reply_markup=markup)
    @bot.message_handler(regexp='darts')        
    def casino(message):
        bot.send_dice(message.chat.id,'🎯')
        bot.send_message(message.chat.id,reply_markup=markup)
   
@bot.message_handler(regexp='support')
def support(message):
    bot.send_message(message.chat.id, f'нам похуй, {message.from_user.first_name} ')
   

bot.infinity_polling()
