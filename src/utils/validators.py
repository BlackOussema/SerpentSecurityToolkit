def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_ip(ip):
    import re
    ip_regex = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    return re.match(ip_regex, ip) is not None

def validate_port(port):
    return isinstance(port, int) and 0 <= port <= 65535

def validate_non_empty_string(value):
    return isinstance(value, str) and bool(value.strip())

def validate_positive_integer(value):
    return isinstance(value, int) and value > 0