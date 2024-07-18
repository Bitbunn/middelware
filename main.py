from game_data_manager import GameDataManager

def main():
    manager = GameDataManager("config.yaml")
    manager.start_receiving_and_sending()

if __name__ == "__main__":
    main()
