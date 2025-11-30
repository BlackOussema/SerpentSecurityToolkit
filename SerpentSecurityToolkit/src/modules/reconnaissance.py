# reconnaissance.py

import platform
import psutil
import socket

def get_system_info():
    """Retrieve system information including CPU, RAM, OS version, and disk usage."""
    cpu_info = psutil.cpu_percent(interval=1)
    ram_info = psutil.virtual_memory()
    os_version = platform.platform()
    disk_usage = psutil.disk_usage('/')

    return {
        'cpu_percent': cpu_info,
        'ram_total': ram_info.total,
        'ram_used': ram_info.used,
        'ram_free': ram_info.free,
        'os_version': os_version,
        'disk_total': disk_usage.total,
        'disk_used': disk_usage.used,
        'disk_free': disk_usage.free,
    }

def get_network_info():
    """Retrieve network interface information including IP and MAC addresses."""
    interfaces = psutil.net_if_addrs()
    network_info = {}

    for interface_name, interface_addresses in interfaces.items():
        for address in interface_addresses:
            if address.family == socket.AF_INET:  # IPv4
                network_info[interface_name] = {
                    'ip_address': address.address,
                    'mac_address': None
                }
            elif address.family == socket.AF_LINK:  # MAC
                if interface_name in network_info:
                    network_info[interface_name]['mac_address'] = address.address

    return network_info

def get_running_processes():
    """Retrieve a list of currently running processes."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        processes.append(proc.info)
    return processes

def perform_reconnaissance():
    """Perform system reconnaissance and return all gathered information."""
    system_info = get_system_info()
    network_info = get_network_info()
    running_processes = get_running_processes()

    return {
        'system_info': system_info,
        'network_info': network_info,
        'running_processes': running_processes,
    }