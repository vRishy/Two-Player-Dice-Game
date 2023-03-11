# Two-Player-Dice-Game

This project involves developing a two-player dice game called Drop Dead using Python programming and MySQL integration. The game consists of five rounds, and each player rolls two 6-sided dice in each round. The players must be registered to ensure that they are authorized players.

The game scoring system involves adding the points rolled on each player's dice to their score. If the total points are an even number, an additional 10 points are added to their score. If the total points are an odd number, 5 points are subtracted from their score. If a player rolls a double, they get to roll one extra die and add the points rolled to their score.

In the event of a tie, where both players have the same score at the end of the game, each player rolls one die, and whoever gets the highest score wins. This process repeats until one player emerges as the winner.

The program outputs the name of the player who has won and stores their score and name in an external file. In addition, the program stores the leaderboard scores in a MySQL database. To achieve this, the program connects to the MySQL database using Python's MySQL connector library, which must be installed using pip. The program then creates a new table in the database to store the leaderboard scores. Each row in the table represents a player, and the columns store the player's name and their score.

The use of MySQL integration ensures data storage and retrieval is seamless and reliable, adding a layer of data security and scalability to the project. The program utilizes problem decomposition, modular and structural programming techniques, and declarative programming to ensure a well-organized, efficient, and effective code.


## Requirements

The task requires to create a two-player dice game. The players need to be registered to play the game to ensure that they are authorised players. The game involves 5 rounds and each player rolls two 6-sided dice in each round. The points rolled on each player’s dice is added to their score. If the total points is an even number then an additional 10 points are added to their score or if the total points are an odd number 5 points are subtracted from their score. If the player rolls a double, they get to roll one extra die and get the points rolled added to their score. Each player gets to roll 1 die if both players have the same score at the end, whoever gets the highest score wins. This repeats until any one of the player wins. The program then outputs the player’s name who has won and store their score and their name in an external file. 

## Success criteria 

	Each player should roll two 6-sided dice
	The points rolled on each player’s dice are added to their score
	The score should be incremented by 10 if the total is an even number
	The score should be subtracted by five if the total is an odd number
	The player should get an extra die if they roll a double,  the points rolled adds to their score
	The score should never be 0 at any point
	Both the players should get one extra die if their scores are equal. The program should repeat until one of the player gets higher points rolled than the other player. 
	The name and score of the player who won should be outputted
	The winning players name and score should be stored in an external file and the score and player name of the top 5 winning scores should be outputted from the external file. 

## Problem Decomposition


	Allow the user to input their details that are authenticated to ensure they are authorised players by using a function 
	The user details are stored in an external file
	Allow each player to roll two 6-sided dice by generating two random number between 1 and 6
	Calculate the points for each round for each player’s total score. 
	Calculate if the player’s total score is an odd or even number and add or subtract based on the program rules
	Use a function to allow the user to play 5 rounds.
	The program then should output the winning player’s score and name. The player’s name and score is then stored in an external file.

## Conclusion 

In conclusion, the code meets all the success criteria and user requirements. This has been made easier through problem decomposition that significantly highlighted the requirements for each stage in the development. The Testing of each stage ensured that the program met all the success criteria. It was planned to be efficient and less memory intensive through declaring functions for each stage of development. This centralised the code as more organized through less lines of codes as calling function reduced repeating the same code again and again. Every stage of the project was done through setting timelines that helped deliver the project on time and skip the stages that had unresolved issues. The document contains table of contents that illustrates the project as more organized and accessible for a user to go through the document. Each stage of the code is well annotated through comments in the code and other annotations and the tested to convey the program is running successfully and as expected by the user.  A table containing the success criteria of the project and how they are met are demonstrated with evidence of testing to convey proof that the code has met all the success criteria. Issues that were unresolved while developing the code are highlighted and clearly demonstrated by the way they are resolved through testing. Majority of the project has been delivered as initially planned with few limitations of unresolved issues with the player login which is later resolved and well-tested to prevent any logical and syntax error in the code. The code was further developed my modifying the Leaderboard section by integrating it with a database using MySQl to store the player details and scores which also made it easier to display and sort the leaderboaard. 
