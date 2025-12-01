import unittest
from src.modules.network_scanner import NetworkScanner

class TestNetworkScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = NetworkScanner()

    def test_device_discovery(self):
        devices = self.scanner.discover_devices()
        self.assertIsInstance(devices, list)
        self.assertGreater(len(devices), 0)

    def test_port_scanning(self):
        open_ports = self.scanner.scan_ports('127.0.0.1')
        self.assertIsInstance(open_ports, list)

    def test_service_detection(self):
        services = self.scanner.detect_services('127.0.0.1', [80, 443])
        self.assertIsInstance(services, dict)

if __name__ == '__main__':
    unittest.main()