from game_logic import play_game


def main():
    while True:
        play_game()
        # Ask if the player wants to play again
        replay = input("🔄 Play again? (y/n): ").lower()
        if replay == "n":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
