from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./Rivescripts")
bot.sort_replies()

run = True

while run is True:    
    print("User:")
    user_input = input()

    if user_input == "quit":
        run = False
    else:
        reply = bot.reply("user", user_input)
        print("Eliza: \n" + reply)
