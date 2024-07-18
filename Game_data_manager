import yaml
from game_data_receiver import GameDataReceiverUDP, GameDataReceiverSharedMemory
from game_data_sender import GameDataSender

class GameDataManager:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)
        self.general_config = self.config["general"]
        self.receivers = []
        self.senders = []
        self.init_receivers_and_senders()

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)

    def init_receivers_and_senders(self):
        for game in self.config["games"]:
            protocol = game["protocol"]
            buffer_size = game.get("buffer_size", 1024)
            receive_frequency = self.general_config.get("receive_frequency", 10)
            send_frequency = self.general_config.get("send_frequency", 20)
            if protocol == "udp":
                receiver = GameDataReceiverUDP(game["ip"], game["port"], game["telemetry_format"], game["data_mapping"], buffer_size, receive_frequency)
            elif protocol == "shared_memory":
                receiver = GameDataReceiverSharedMemory(game["shared_memory_name"], game["telemetry_format"], game["data_mapping"])
            else:
                raise ValueError(f"Unsupported protocol {protocol} for game {game['name']}")

            sender = GameDataSender(self.config["devices"], send_frequency)
            self.receivers.append(receiver)
            self.senders.append(sender)

    def start_receiving_and_sending(self):
        for receiver, sender in zip(self.receivers, self.senders):
            receiver.start_receiving()
            sender.start_sending()
