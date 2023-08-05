## Problem Statement

### Requirements
Design class diagram for snake and ladders multiplayer game. One of the players creates a room and shares the roomCode with up to 3 of his friends. These friends join the room with the roomCode provided and once all the players are ready, the room creator can start the game. 
	Each of the players have 1 token each. And they start at position 1 on the board and the first one to reach position 100 will win the game. Players will roll an unbiased dice one by one in a predetermined order, the token of the player will be moved ahead by the number with the dice outcome. If the token stops on the start of the ladder then the token moves up to the end of the ladder. Similarly, if the player lands at the face of the snake, then the token moves down to the position where the end of the snake tail lies. First one who reaches the position 100 wins the game.

#### Other points to consider:
1. The board is set up with the snake and ladders using several of the predefined configurations of snakes and ladders.
1. There will be different types of snakes, ladders which appear differently on the board.


#### Future scope
These points are optional points to be considered during the design, these ideas may or may not be implemented by the product in future. 
There can be multiple game modes introduced in future which can have different configurations like
1. Multiple dice to be rolled by player at once as opposed to single dice.
1. Multiple dice to be owned by each player and first one to reach all his/her tokens to 100 wins.
1.  Special type of snake (If you land on it, you will not only go to the end of tail but also lose next turn) and ladder (If you land on it, you will go to the top of the ladder and get an extra turn) can be introduced.
1. Shape of the board can change in new modes but the numbering will continue to be 1 to 100.

#### Expected from candidate
1. Well designed and extensible class diagram of the game with clear indication of fields, functions (their return type, params, access specifiers) and relationship between classes.
1. A write up or a sequence diagram for the important flows of the game.


## Class Diagram

```mermaid


classDiagram
    class Game {
        - String roomCode
        - Player[] players 
        - GameStatus status
        - Player winner 
        - Board board 
        - Dice dice
        - GameMode[] modes
        - Player roomAdmin 
        + addPlayer(Player player)
        + removePlayer(Player player)
        + startGame()
        + isGameComplete(): bool
        + handlePlayerTurn(Player player, Dice dice)
    }

   class Player {
        - String playerId
        - String playerName
        - Square playerPosition
        - Dice[] ownedDice
        - int turnBalance
        + rollDice(Dice[]: dice = [dice]): int
        + getPlayerPosition()
        + getTurnBalance()
        + increaseTurnBalance()
        + decreaseTurnBalance()
    }

    class Board {
        - Square[] squares
        - Snake[] snakes
        - Ladder[] ladders
        - BoardShape shape
    }

    class Square {
        - squareNumber
    }

    class Snake {
        - Square startSquare
        - Square endSquare
        - SnakeTypes snakeType
        - bool eatsTurn
        + bool isTurnEater()
    }

    class Ladder {
        - Square startSquare
        - Square endSquare
        - LadderTypes ladderType
        - bool freeTurn 
        + bool givesFreeTurn()
    }

    class GameStatus{
       <<enumeration>>
       READY_TO_PLAY
       IN_PROGRESS
       COMPLETE
    }
    class GameMode{
       <<enumeration>>
       STANDARD
       FREETURN_LADDERS
       TURN_EATER_SNAKES
       MULTI_DIE_PLAYERS
    }
    class SnakeTypes{
       <<enumeration>>
       SNAKE1
       SNAKE2
       SNAKE3
    }

    class LadderTypes{
       <<enumeration>>
       LADDER1
       LADDER2
       LADDER3
    }

    class BoardShape{
       <<enumeration>>
        SHAPE1
        SHAPE2
        SHAPE3
    }

    class Dice {
        - int[] sides 
        + roll()> int
    }

    Game o-- Player
    Game *-- Board
    Game *-- Dice
    Board *-- Square
    Board *-- Snake
    Board *-- Ladder
    Player -- Dice




```

## Sequence Diagram

```mermaid
sequenceDiagram
    participant P1 as Player1 (game admin)
    participant P2 as Player2
    participant P3 as Player3
    participant P4 as Player4
    participant G as Game

    P1->>G: Create room and share roomCode
    P2->>G: Join with roomCode
    P3->>G: Join with roomCode
    P4->>G: Join with roomCode

    alt All players ready
        P1->>G: Start the game
        loop Until game complete
            G->>P1: HandlePlayerTurn()
            activate P1
            P1->>G: rollDice()
            G->>Board: Determine new position
            Board->>G: New position
            G ->> Board: check snake-ladder at this position?
            G ->>P1: Update position
            G->>P1: Check for win condition
            deactivate P1

            G->>P2: HandlePlayerTurn()
            activate P2
            P2->>G: rollDice()
            G->>Board: Determine new position
            Board->>G: New position
            G ->> Board: check snake-ladder at this position?
            G->>P2: Update position
            G->>P2: Check for win condition
            deactivate P2

            G->>P3: HandlePlayerTurn()
            activate P3
            P3->>G: rollDice()
            G->>Board: Determine new position
            Board->>G: New position
            G ->> Board: check snake-ladder at this position?
            G->>P3: Update position
            G->>P3: Check for win condition
            deactivate P3

            G->>P4: HandlePlayerTurn()
            activate P4
            P4->>G: rollDice()
            G->>Board: Determine new position
            Board->>G: New position
            G ->> Board: check snake-ladder at this position?
            G->>P4: Update position
            G->>P4: Check for win condition
            deactivate P4
        end
    else Some players not ready
        G-->>P1: Cannot start, players not ready
    end
    G-->>P1 : Game complete, announce winner
    G-->>P2 : Game complete, announce winner
    G-->>P3 : Game complete, announce winner
    G-->>P4 : Game complete, announce winner



```




