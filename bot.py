import telebot as tb
import random as rnd


Token = "6514145919:AAGJY5oqN6qpBv90RidrwU9Ts5w26TyFjXE"
print('started')
bot = tb.TeleBot(Token)
@bot.message_handler(commands=['start,play,open_up,help'])
@bot.message_handler(regexp='start')
def send_message(message):
    bot.send_message(message.chat.id, f"Hello! {message.from_user.first_name}\nIf you want to see commands print /help")



@bot.message_handler(regexp='play')
def send_random_num(message):
    rndNum = rnd.randint(1,12)
    rndNum2 = rnd.randint(1,12)
    rndNum3 = rnd.randint(1,12)

    print(bot.send_message(message.chat.id, f'Your score:{rndNum} \nto take another card print /next'))
    @bot.message_handler(regexp='next')
    def send_eshcare(message):
        userNum = rndNum + rndNum2
        if userNum > 21:
            print(bot.send_message(message.chat.id, f'You lose'))
        elif userNum == 21:
            print(bot.send_message(message.chat.id, f'You win'))
        else:
            print(bot.send_message(message.chat.id, f'Your score:{userNum}(+{rndNum2}) \nto take another card print /continue '))
        
        @bot.message_handler(regexp='continue')
        def send_pisun(message):
            userNum1 = userNum + rndNum3
            if userNum1 == 21:
                print(bot.send_message(message.chat.id, f'You win'))
            elif userNum1 > 21:
                print(bot.send_message(message.chat.id, f'You lose'))
            else:
                print(bot.send_message(message.chat.id, f'Your score:{userNum1}(+{rndNum3}) \nfind out the result /open_up '))
                @bot.message_handler(regexp='open_up')
                def send_result(message):
                    rndBot = rnd.randint(1,21)
                    if userNum1 > rndBot:
                        print(bot.send_message(message.chat.id, f'You won {userNum1}:{rndBot} '))
                    elif userNum1 < rndBot:
                        print(bot.send_message(message.chat.id, f'You lose {userNum1}:{rndBot}'))
                    else:
                        print(bot.send_message(message.chat.id, f'draw{userNum1}:{rndBot}' ))


         
@bot.message_handler(regexp='help')
def help(message):
    print(bot.send_message(message.chat.id, f'/play-начало игры'))






           


bot.infinity_polling()

