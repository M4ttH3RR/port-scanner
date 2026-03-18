import socket

def scan_target(target):
    print(f"\nScanning target: {target}")
    print("Open ports:\n")

    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            print(f"Port {port} is open ({service})")

        s.close()

if __name__ == "__main__":
    target = input("Enter IP address to scan: ")
    scan_target(target)