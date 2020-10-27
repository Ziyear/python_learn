import socket

# tcp
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

# udp
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket Created")