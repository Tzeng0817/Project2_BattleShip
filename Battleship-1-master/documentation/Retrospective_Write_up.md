# Meeting notes:

**Meeting 1:**

Date: Fri 9/6/19

Location: Eaton 2

Members: Karen Setiawan, Rikki Augustine, Antonette Gichohu, Alfonso Martello, Grant Gollier

Topics:
-	What language will we use?
    - Not JavaScript
    - Most likely Python3
-	Team Meetings in lab W 9-10 & MF 2-3 pm

**Meeting 2:**

Date: Mon 9/9

Location: Eaton 2

Members: Karen Setiawan, Rikki Augustine, Antonette Gichohu, Alfonso Martello, Grant Gollier

Topics:
- Research implementation of product
- Discussed languages and display of project
  - Chose to code our project in Python
- Next meeting at 4 today
- Need to break the game battleship into parts to code

**Meeting 3:**

Date: Mon 9/9

Location: Eaton 2

Members: Karen Setiawan, Rikki Augustine, Antonette Gichohu, Alfonso Martello, Grant Gollier

Topics:
- How to make an 8x8 board
- Plan for Classes/Implementation
  - Game (AKA executive)
    - Gui
    - switchPlayer()
    - Handle display functions
  - Board
    - Where shots have been fired
    - Hit & miss
    - Stores position of ships
    - isSunk()
    - isHit()
  - Player
    - They get a board
    - setUp()
      - rotate
    - attack()
  - Ship
    - Size of ship (wrapper)
    - Object contains
      - Origin
      - Direction
      - Length
- Progression
    - Game
      - Handle UI
      - Set Up
      - Run
      - Player1
        - Attack
      - Player 2
        - Attack
      - EndGame
  - Player
    - Current Player
    - Create own board
      - Make n ships
      - Handle rotating, shipts
    - BeAttacked
    - HasLost
  - Board
    - 8x8 list
    - constructor(places ships)
    - isHit()
    - isSunk() 
    - In list either empty, hit, or miss
    - attacked( returns boolean T=hit F=miss) updates list
  - Ship
  - Divide code
    - Antonette -> Ship, Player
    - Karen -> Game
    - Grant -> Board
    - Rikki -> Player
    - Alfonso -> Game

**Meeting 4:**

Date: Wed 9/11 (9-11)

Location: Engineering

Members: Karen Setiawan, Rikki Augustine, Antonette Gichohu, Alfonso Martello, Grant Gollier

Topics:
- General getting started with coding the project while together
- Want to have a basic first iteration done by next Monday 9/16

**Meeting 5:**

Date: Wed 9/13

Location: Engineering

Members: Karen Setiawan, Rikki Augustine, Antonette Gichohu, Alfonso Martello, Grant Gollier

Topics:
- Created our own branches to start adding our code to GitHub
- Considering what GUI library we will use for our game (possibly PyQt5 or Python Arcade)

**Meeting 6:**

Members: Antonette Gichohu, Alfonso Martello, Grant Gollier

Topics:
- Started working on documentation 
- Chose to use PyQt5 as our GUI library
- Work on UI will be done by everyone as Game cannot handle all UI in its own class
- Grant will be absent for the next two days
- Documenting will be done using PyDoc format (look at board.py)

Questions:

- What do we have left to do:
  - Pretty much everything
- What can we do to fix that:
  - Work for next few days
  - We have basic logic, so we just need to work on making it pretty
- Schedule for getting work done:
  - Pseudo meeting sometime today
  - Wednesday lab time
  - EVERYONE BE FINISHED BY FRIDAY
  - Saturday is test, documentation, evaluation, everything 
- What needs to be done on game and who needs to do what:
  - Main menu - basic info
  - Game itself

**Meeting 7:**

Date: Wed 9/18

Location: Engineering

Members: Karen Setiawan, Rikki Augustine, Antonette Gichohu, Alfonso Martello

What we need to do:
- Make main menu and get user name and num of ships from game
- Player one and two place their ships
- Players turn: they see their board and opponents board and can attack
- End game 
- Need to merge am and ks branches to master

To do:
- Main menu - Alfonso
- Info gathered menu - Alfonso
- Place ships player 1 – Grant, Alfonso, Karen
- Place ships player 2 - Grant, Alfonso, Karen
- Player 1 turn – Antonette, Karen
- Player 2 turn - Antonette, Karen
- Endgame screen - Alfonso
- Rotate ship - Antonette 
- Show and place ship - Rikki
- Switch tab button - Karen

**Meeting 8:**

Date: Thurs 9/19

Location: Engineering

Members: Karen Setiawan, Antonette Gichohu, Alfonso Martello, Grant Gollier

Topics:
- How to work with the UI and where to go from here?
- Decided to change the GUI library to Python Arcade. This was fully approved by all team members.

**Meeting 9:**

Date: Friday 9/20

Location: Engineering

Members: Karen Setiawan, Rikki Augustine, Antonette Gichohu, Alfonso Martello, Grant Gollier

Topics:
- Updated player version in master
- Updated game class

**Meeting 10:**

Date: Saturday 9/21 10:00am - 6:30 PM

Location: Lawrence Public Library

Members: Karen Setiawan, Rikki Augustine, Antonette Gichohu, Alfonso Martello, Grant Gollier

Topics:
- “It’s hacky but it works”
- “The goal is not to cry”
- Discussed and implemented how to place and rotate ships
- Integrated game class to repo
- Added a button class
- Got rid of all PyQT5
- Learned that the essential functionality of displaying multiple arcade windows at once doesn’t work with Windows. The game can still be run on Mac (and possibly Linux). 

**Meeting 11:**

Date: Sunday 9/22 8:00am

Location: Engineering

Members: Karen Setiawan, Rikki Augustine, Antonette Gichohu, Alfonso Martello, Grant Gollier

Topics:
- Need to finalize project today
- All documentation needs to be finished
- Need to get it tested and working
- Found errors in ship placement to work around
- Integrating pieces together 
- Compensated for lack of ability to display window for switching sides to sound 
- Complicated game flow will now be given as instructions

# Team Division of Labor:
- Original Plan:
  - Game - Alfonso
  - Board - Grant
  - Button - Karen
  - Player - Rikki
  - Ship - Antonette
  - GUI (All)
- Final Split of Work:
  - Main / Menu – Alfonso
  - Selecting how many ships to play with – Karen
  - Transitioning between game states – Alfonso and Karen
  - Placing ships – Rikki
  - Managing the board and flow of actual gameplay – Grant
  - Documentation and helping with all areas – Antonette
  
# Challenges:
- The GUI: No one in the group had worked with UI before. There was a steep learning curve and we did a lot of guess and check to figure out what would work and what doesn’t. We originally planned to use the PyQt5 library, but due to how complicated and redundant PyQt5 was, we switched to using Python Arcade library only a few days before the deadline. Python Arcade was much more understandable and programmer friendly.
- Displaying Windows: We originally planned to have each GUI class open its own window, but the window class in Arcade caused problems into the code, so we converted the existing code base at the time into using the View Arcade class (which is integrated with the Arcade windows class but did not cause as many bugs). 
- Could not use our own event loop: When we started programming, we created the game logic before working on the GUI. Originally, we had our own event loop managing all aspects of the game states, but the arcade.run function is its own event loop (and that function must be called for the Arcade library to work). Therefore, our game logic did not work. We solved this by integrating the game logic with the GUI and by allowing the GUI to manage the transferring the game to the next state.
- Issue with deleting ships during ship placement: We had a function that could delete a ship after it was placed, allowing users to change their mind after placing a ship. However, this function also introduced a series of game breaking bugs, so we decided to exclude that feature. 

# Features not in the Demo:
- Deleting ships during ship placement (thus allowing users to change their mind on where they placed their ships).
- Displaying a message during the game telling players to switch so each player knows when it is their turn.
- Allowing players to enter their names (Arcade did not have text boxes for user input).
- Displaying ship icons where the ships are instead of just denoting the ships with x’s.

# Retrospective
- We would have started coding earlier and worked harder at the beginning of the two-week period instead of having to do most of the project over a few days. We would have started by learning the GUI we had chosen library and we would have started implementing the GUI and game logic at the same time instead of first doing the game logic and then the GUI (because this approach did not work as discussed in the challenges section). If we could redo the project, we might have decided to make it web-based and would have coded it in JavaScript instead because the GUI would be easier to integrate with the code. As a team we worked well and had plenty of productive meetings and efficiently divided the work between us.
