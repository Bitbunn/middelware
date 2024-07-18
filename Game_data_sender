import socket
import time
from telemetry_common import TelemetryData

class GameDataSender:
    def __init__(self, devices_config, send_frequency):
        self.devices_config = devices_config
        self.send_frequency = send_frequency
        self.sockets = {}
        for device, config in devices_config.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sockets[device] = (sock, (config["ip"], config["port"]))
        self.telemetry_data = None

    def update_telemetry_data(self, telemetry_data):
        self.telemetry_data = telemetry_data

    def start_sending(self):
        while True:
            if self.telemetry_data:
                data = self.telemetry_data.serialize()  # Assurez-vous que TelemetryData a une méthode serialize
                for device, (sock, addr) in self.sockets.items():
                    sock.sendto(data, addr)
            time.sleep(1 / self.send_frequency)
