import socket
import struct
import mmap
import time
from telemetry_common import TelemetryData

class GameDataReceiverUDP:
    def __init__(self, ip, port, telemetry_format, data_mapping, buffer_size, receive_frequency):
        self.ip = ip
        self.port = port
        self.telemetry_format = telemetry_format
        self.data_mapping = data_mapping
        self.buffer_size = buffer_size
        self.receive_frequency = receive_frequency
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.ip, self.port))
        self.telemetry_data = None

    def start_receiving(self):
        while True:
            data, addr = self.sock.recvfrom(self.buffer_size)
            unpacked_data = struct.unpack(self.telemetry_format, data)
            self.telemetry_data = TelemetryData(
                [unpacked_data[i] for i in self.data_mapping["vehicle_pos"]],
                [unpacked_data[i] for i in self.data_mapping["vehicle_speed"]],
                [unpacked_data[i] for i in self.data_mapping["vehicle_accel"]],
                [unpacked_data[i] for i in self.data_mapping["vehicle_ang_euler"]],
                [unpacked_data[i] for i in self.data_mapping["vehicle_ang_speed"]],
                [unpacked_data[i] for i in self.data_mapping["vehicle_ang_accel"]],
                unpacked_data[self.data_mapping["engine_rpm"]],
                [unpacked_data[i] for i in self.data_mapping["susp_deflect"]]
            )
            time.sleep(1 / self.receive_frequency)

class GameDataReceiverSharedMemory:
    def __init__(self, shared_memory_name, telemetry_format, data_mapping):
        self.shared_memory_name = shared_memory_name
        self.telemetry_format = telemetry_format
        self.data_mapping = data_mapping
        self.telemetry_data = None

    def start_receiving(self):
        while True:
            with mmap.mmap(-1, 4096, self.shared_memory_name) as mem:
                data = mem.read()
            unpacked_data = struct.unpack(self.telemetry_format, data)
            self.telemetry_data = TelemetryData(
                [unpacked_data[i] for i in self.data_mapping["vehicle_pos"]],
                [unpacked_data[i] for i in self.data_mapping["vehicle_speed"]],
                [unpacked_data[i] for i in self.data_mapping["vehicle_accel"]],
                [unpacked_data[i] for i in self.data_mapping["vehicle_ang_euler"]],
                [unpacked_data[i] for i in self.data_mapping["vehicle_ang_speed"]],
                [unpacked_data[i] for i in self.data_mapping["vehicle_ang_accel"]],
                unpacked_data[self.data_mapping["engine_rpm"]],
                [unpacked_data[i] for i in self.data_mapping["susp_deflect"]]
            )
            time.sleep(1 / self.receive_frequency)
