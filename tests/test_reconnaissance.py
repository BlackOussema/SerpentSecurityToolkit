import unittest
from src.modules.reconnaissance import get_cpu_info, get_ram_info, get_os_version, get_disk_usage, get_network_interfaces, get_mac_addresses, get_running_processes

class TestReconnaissance(unittest.TestCase):

    def test_get_cpu_info(self):
        cpu_info = get_cpu_info()
        self.assertIsInstance(cpu_info, dict)
        self.assertIn('model', cpu_info)
        self.assertIn('cores', cpu_info)

    def test_get_ram_info(self):
        ram_info = get_ram_info()
        self.assertIsInstance(ram_info, dict)
        self.assertIn('total', ram_info)
        self.assertIn('available', ram_info)

    def test_get_os_version(self):
        os_version = get_os_version()
        self.assertIsInstance(os_version, str)

    def test_get_disk_usage(self):
        disk_usage = get_disk_usage()
        self.assertIsInstance(disk_usage, dict)
        self.assertIn('total', disk_usage)
        self.assertIn('used', disk_usage)

    def test_get_network_interfaces(self):
        network_interfaces = get_network_interfaces()
        self.assertIsInstance(network_interfaces, list)

    def test_get_mac_addresses(self):
        mac_addresses = get_mac_addresses()
        self.assertIsInstance(mac_addresses, list)

    def test_get_running_processes(self):
        running_processes = get_running_processes()
        self.assertIsInstance(running_processes, list)

if __name__ == '__main__':
    unittest.main()