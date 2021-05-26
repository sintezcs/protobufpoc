import abc
import json
import statistics
import sys

from google.protobuf.json_format import ParseDict

from logger import LoggerMixin
from notification_pb2 import Notification


class EventCompressor(abc.ABC, LoggerMixin):
    def __init__(self):
        super().__init__()
        self.ratios = []

    def print_and_reset_stats(self):
        average_ratio = statistics.mean(self.ratios)
        self.logger.debug(
            f'Average compress ratio for {len(self.ratios)} events is {average_ratio:.2f}%.')

    @abc.abstractmethod
    def _compress(self, data: dict) -> bytes: ...

    @abc.abstractmethod
    def decompress(self, data: bytes) -> dict: ...

    def compress(self, data: dict) -> bytes:
        raw_size = sys.getsizeof(json.dumps(data).encode())
        compressed = self._compress(data)
        compressed_size = sys.getsizeof(compressed)
        ratio = (raw_size - compressed_size) / (raw_size / 100)
        self.ratios.append(ratio)
        self.logger.debug(f'Raw (json string): {raw_size}, Compressed (protobuf): {compressed_size}, Ratio: {ratio:.2f}%')
        return compressed


class ProtobufCompressor(EventCompressor):
    def _compress(self, data: dict) -> bytes:
        notification = Notification()
        notification = ParseDict(data, notification)
        return notification.SerializeToString()

    def decompress(self, data: bytes) -> dict:
        pass
