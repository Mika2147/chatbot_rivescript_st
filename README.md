# Chatbot - Russian-Ukrainian war

A chatbot which provides current casualty statistics on the Russian-Ukrainian war.

## Description

As part of a project for Semantic Technologies in the first master's semester of computer science at the HKA, a chatbot is to be implemented that provides current casualty figures for the Russian-Ukrainian war. This is done with [Rivescript](https://www.rivescript.com/), which is the basis of the chatbot.
The bot gets the data from Wikipedia and pays attention to the semantic phrasing of the user. Depending on the bias, pro-Ukrainian, pro-Russian or U.S. estimates are provided.

## Getting Started

### Dependencies

Just execute the following line in the root directory of this repository:
```bash
pip install -r chatbot_sematic_technologies/requirements.txt
```
This will install the required packages for the python script to work:
* RiveScript
* lxml
* beautifulsoup4
* pandas
* requests
* re

### Installing

Just clone or download this repository as zip file. No installation needed.

### Executing program

* How to run the program
* Open console in ./chatbot_sematic_technologies/
* Execute the following command
```
python app.py
```
* Ask the bot anything

## Help

If you have no clue what to ask the bot. Try one of the following:
* How many civilians have died in the russia ukraine conflict
* How many russian/ukrainian soldiers have died in the war/conflict/special military operation

To exit the application just type
```bash
quit
```

## Authors

[Mika Auer](https://github.com/Mika2147)

[Tim Hänlein](https://github.com/THaenlein)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
