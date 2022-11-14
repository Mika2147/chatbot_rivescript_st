package com.chatbot;
import java.util.Scanner;

import com.rivescript.Config;
import com.rivescript.RiveScript;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        RiveScript bot = new RiveScript();
        bot.loadFile("./eliza.rive");
        bot.sortReplies();

        while(true){
            Scanner scanner = new Scanner(System.in);
            System.out.println("User:");
            String userInput = scanner.nextLine();

            if(userInput.equals("quit")){
                scanner.close();
                return;
            }

            String reply = bot.reply("user", userInput);
            System.out.println("Eliza: \n" + reply);
        }
        
    }
}
