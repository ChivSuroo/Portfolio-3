# Code Institute Portfolio 3 - Hangman Submission

Hangman, custom coded Python game all configured and runs completely on HEROKU.

Users will need to find the selected word and will only have a number of inputs before they're essentially hanged, out the game.

![Responsice Mockup](https://cdn.discordapp.com/attachments/943259257753710684/943269859628830780/unknown.png)

## How to play
When running the game you will be given a random word that has been automatically given you, every time you run the application you will have a new word given out to you. Normally you would play this game with a friend and they would give you a word for luckily with the power of coding this now possible to play the game all by yourself.

When you run the application you will see a number of hashes where your word will showcase depending on the number of guesses you get correct/incorrect for example if the word that you have to guess is CHEESE then it will show as '_ _ _ _ _ _'  6 hashes will show because cheese has a total of 6 characters in its name. 

When you guess the letter wrong you will see for yourself as the board will gradually start to create a person getting hanged, if you fail to guess within 7 turns then the game will stop and say you have lost, obviously if you manage to find the word without the full diagram being created then you will win the game!

# Features
![Responsice Mockup](https://cdn.discordapp.com/attachments/919077234109739008/943243030264180736/unknown.png)

When you run the script, you will be greeted with a simple user-friendly interface. I have made this as simple as possible so when someone new to the game plays they will be able play instantly and see what's going on as everything inputted is logged with all correct guesses and of course the hangman viewer showcase.

![Responsice Mockup](https://cdn.discordapp.com/attachments/919077234109739008/943245808495628389/unknown.png)

When you guess a letter incorrectly it will notify you this and tell you saying "Your guess was incorrect", with this being a feature the player will not be able to input this letter anymore and will not lose a life in-case they forget that they have used the chosen letter.  

![Responsice Mockup](https://cdn.discordapp.com/attachments/919077234109739008/943250007237222510/unknown.png)

When the user loses the game it will notify them saying, "You have lost the game, BETTER LUCK NEXT TIME!. This this being a feature of course we want the player to not have the ability to make another guy so this has been completely disabled for the user forcing them to re-run the script if they wish to play again. 

![Responsice Mockup](https://cdn.discordapp.com/attachments/919077234109739008/943252403736686652/unknown.png)

When the user guesses all the letters without creating the full hangman image then they will be greeted with the "You have won, congratulations!" same as the loss notifier, the user will not be able to input anymore guesses as the game will be over forcing them to re-run the script. 

## Future Features
* The ability to have an Easy/Medium/Hard mode ( adds more words but at a higher level for example if you select easy mode you will get words like "Dog, Cat, Cow" and Hard will be "Handkerchief, Intelligence, Pharaoh". 
* Add a two/four player option - this game can be super fun with multiple people so this option would be one to think about for sure.

## Game Testing
I have manually tested the project by doing the following:
* Passed the code through the PEP8 online checker and everything has now came back with no issues.
* I have tested in my local area within GitPod and also on the deployed website.

## Bugs / Issues / Solved
* When validating my code within the PEP8 there was an issue where I put an extra # without any context to I removed and this fixed the issue
* Another issue which I couldn't really get my head around and tried but quite frankly just didn't have time to complete due to the deadline of this project, I am struggling on how to get the words you have already used to actually showcase where I have placed the "Letters You Have Used" it doesn't showcase the letters next to this, would of loved to tackle this and forsure I will in the future.
* After testing the game for myself I noticed a few spelling mistakes due to me being silly, but they have been fixed and working order.

## Validating Testing 
* I have tested everything and there are no issues. 
![Responsice Mockup](https://cdn.discordapp.com/attachments/943259257753710684/943259402457219072/unknown.png)

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku
# Steps for deployment
* I signed up to Heroku.
* Created a new application
* Linked GitHub and added my project from GitHub
* Added the buildworks // Python and NodeJS making sure they are in the correct order with Python on top
* Click on Deploy
