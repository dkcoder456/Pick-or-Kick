
import random

def pick_or_kick():
    players = []
    score = 0
    
    print("Welcome to Pick or Kick Challenge!")
    
    # Get number of players
    num_players = int(input("Enter number of players (2-6): "))
    
    # Get player names
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        players.append({"name": name, "score": 0})
    
    # Game rounds
    rounds = 5
    for round_num in range(rounds):
        print(f"\nRound {round_num + 1}")
        
        for player in players:
            print(f"\n{player['name']}'s turn!")
            
            # Generate random challenge
            challenges = [
                "Do 10 jumping jacks",
                "Tell a joke",
                "Sing a short song",
                "Do your best dance move",
                "Make animal sounds",
                "Tell a funny story"
            ]
            
            challenge = random.choice(challenges)
            print(f"Challenge: {challenge}")
            
            # Player chooses to pick or kick
            choice = input("Will you PICK (do the challenge) or KICK (skip)? ").lower()
            
            if choice == "pick":
                print("You chose to do the challenge!")
                completed = input("Did you complete the challenge? (yes/no): ").lower()
                if completed == "yes":
                    player["score"] += 2
                    print("Great job! +2 points!")
            else:
                print("You kicked the challenge!")
                player["score"] -= 1
                print("-1 point for skipping!")
                
            print(f"Current score: {player['score']}")
    
    # Find winner
    winner = max(players, key=lambda x: x["score"])
    print("\n=== Game Over ===")
    print(f"The winner is {winner['name']} with {winner['score']} points!")
    
    # Display all scores
    print("\nFinal Scores:")
    for player in players:
        print(f"{player['name']}: {player['score']} points")

if __name__ == "__main__":
    pick_or_kick()
