from flask import jsonify
import nmap

class NetworkScanner:
    def __init__(self):
        self.scanner = nmap.PortScanner()

    def scan_network(self, subnet):
        try:
            self.scanner.scan(hosts=subnet, arguments='-sn')
            return self._parse_scan_results()
        except Exception as e:
            return {'error': str(e)}

    def _parse_scan_results(self):
        devices = []
        for host in self.scanner.all_hosts():
            device_info = {
                'ip': host,
                'state': self.scanner[host].state(),
                'hostname': self.scanner[host].hostname(),
                'protocols': list(self.scanner[host].all_protocols())
            }
            devices.append(device_info)
        return devices

    def port_scan(self, target_ip):
        try:
            self.scanner.scan(target_ip)
            return self._parse_port_scan_results(target_ip)
        except Exception as e:
            return {'error': str(e)}

    def _parse_port_scan_results(self, target_ip):
        ports = []
        if target_ip in self.scanner.all_hosts():
            for proto in self.scanner[target_ip].all_protocols():
                lport = list(self.scanner[target_ip][proto].keys())
                for port in lport:
                    port_info = {
                        'port': port,
                        'state': self.scanner[target_ip][proto][port]['state'],
                        'name': self.scanner[target_ip][proto][port]['name']
                    }
                    ports.append(port_info)
        return ports

# Example usage:
# scanner = NetworkScanner()
# print(scanner.scan_network('192.168.1.0/24'))
# print(scanner.port_scan('192.168.1.1'))