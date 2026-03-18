import socket
import threading
import tkinter as tk
from tkinter import scrolledtext


def start_scan():
    
    threading.Thread(target=scan_ports, daemon=True).start()


def scan_ports():
    target = entry.get()

    output.delete('1.0', tk.END)

    if not target:
        output.insert(tk.END, "Please enter an IP address.\n")
        return

    output.insert(tk.END, f"Scanning {target}...\n\n")

    for port in range(1, 1025):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            result = s.connect_ex((target, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"

                
                root.after(0, lambda p=port, svc=service:
                output.insert(tk.END, f"Port {p} open ({svc})\n"))

            s.close()

            
            if port % 100 == 0:
                root.after(0, lambda p=port:
                output.insert(tk.END, f"Scanned up to port {p}...\n"))

        except:
            pass

    root.after(0, lambda: output.insert(tk.END, "\nScan complete.\n"))



root = tk.Tk()
root.title("Port Scanner")

tk.Label(root, text="Enter IP Address:").pack()

entry = tk.Entry(root, width=30)
entry.pack()

tk.Button(root, text="Scan", command=start_scan).pack()

output = scrolledtext.ScrolledText(root, width=60, height=20)
output.pack()

root.mainloop()
