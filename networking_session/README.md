# Short Introduction to networking
Networking is the practice of connecting computers and devices together to share resources and information. Networking enables communication between devices, allowing them to exchange data and access shared resources like files, printers, and internet connections. In this session, we will introduce networking concepts like IP addresses, ports, HTTP, and DNS.

## Networks 
A network is a collection of computers and devices that are connected together to share resources and information. Networks can be classified based on their size and scope:
- **Local Area Network (LAN)**: A LAN is a network that covers a small geographical area like a home, office, or building. LANs are typically used to connect devices within a limited area.
- **Wireless Local Area Network (WLAN)**: A WLAN is a type of LAN that uses wireless technology like Wi-Fi to connect devices.
- **Wide Area Network (WAN)**: A WAN is a network that covers a large geographical area like a city, country, or continent. WANs are used to connect devices over long distances. The internet is an example of a WAN.
<br><br>
*Examples of network devices include routers, switches, modems, and access points. These devices are used to connect devices together and enable communication between them.*
<br><br>

- **Router**: A router is a network device that forwards data packets between computer networks. Routers are used to connect devices within a network and route data between networks.
- **Switch**: A switch is a network device that connects devices within a network. Switches are used to create a network by connecting devices like computers, printers, and servers.
- **Modem**: A modem is a device that modulates and demodulates digital signals to enable communication between devices over a network. Modems are used to connect devices to the internet.
- **Access Point**: An access point is a device that allows wireless devices to connect to a wired network using Wi-Fi. Access points are used to create wireless networks and provide internet access to wireless devices.
<br><br>
*A modern Routers are often a combination of a router, switch, modem, and access point in a single device. These devices are used to connect devices within a network and provide internet access to devices.*
<br><br>
## IP addresses
But how do devices communicate with each other over a network? Devices on a network are identified by IP addresses. An IP address is a unique numerical label assigned to each device on a network. IP addresses are used to identify devices and enable communication between them. There are two types of IP addresses:
- **IPv4**: IPv4 is the fourth version of the Internet Protocol and is the most widely used IP address format. IPv4 addresses are 32-bit numerical addresses written in the form of four octets separated by dots (e.g., 192.1.1.0).
- **IPv6**: IPv6 is the sixth version of the Internet Protocol and is designed to replace IPv4. IPv6 addresses are 128-bit numerical addresses written in hexadecimal format (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
<br><br>
IP addresses are used to route data packets between devices on a network. Devices use IP addresses to send and receive data over the network. IP addresses are assigned to devices dynamically or statically by a network administrator or a DHCP server.

## Ports
In addition to IP addresses, devices communicate with each other using ports. A port is a communication endpoint that allows devices to send and receive data over a network. Ports are identified by numbers ranging from 0 to 65535. Ports are used to differentiate between different types of network traffic. There are three types of ports:
- **Well-known ports**: Well-known ports are reserved for specific services and applications. Well-known ports range from 0 to 1023 and are assigned to common services like HTTP (port 80), HTTPS (port 443), FTP (port 21), and SSH (port 22).
- **Registered ports**: Registered ports are assigned by the Internet Assigned Numbers Authority (IANA) to specific services and applications. Registered ports range from 1024 to 49151 and are used by applications that require specific ports.
- **Dynamic ports**: Dynamic ports are used by client applications to communicate with servers. Dynamic ports range from 49152 to 65535 and are assigned dynamically by the operating system.
<br>
A combination of an IP address and a port number uniquely identifies a communication endpoint on a network. Devices use IP addresses and port numbers to establish connections and exchange data over the network. Different services and applications use different port numbers to run concurrently on a device.

## Firewalls
Firewalls are network security devices that monitor and control incoming and outgoing network traffic. Firewalls are used to protect devices and networks from unauthorized access and cyber threats. Firewalls can be implemented as hardware devices or software applications. Firewalls use rules and policies to filter network traffic and prevent malicious activity. Firewalls can be configured to block or allow specific types of traffic based on predefined rules. Firewalls are an essential component of network security and are used to protect devices and networks from cyber attacks. Firewalls can be configured to block specific IP addresses, ports, and protocols to secure the network. In the future, we will cover more about firewalls and network security in detail. If you are interested in learning more about firewalls and network security, check out the ***UFW - Uncomplicated Firewall***. 

## Standard Protocols
There are many standard protocols used in networking to enable communication between devices. Some of the common protocols include:
- **HTTP (Hypertext Transfer Protocol) Port 80**: HTTP is the protocol used to transfer hypertext documents over the internet. HTTP is the foundation of data communication on the World Wide Web and is used by web browsers to retrieve web pages from web servers.
- **HTTPS (Hypertext Transfer Protocol Secure) Port 443**: HTTPS is the secure version of HTTP that uses encryption to secure data transmitted over the internet. HTTPS is used to protect sensitive information like passwords, credit card numbers, and personal data.
- **DNS (Domain Name System) Port 53**: DNS is the protocol used to translate domain names into IP addresses. DNS is used to resolve domain names like google.com into IP addresses like
- **SSH (Secure Shell) Port 22**: SSH is a secure protocol used to access and manage remote devices over a network. SSH provides encrypted communication between devices and is used to securely transfer files, execute commands, and manage devices remotely.
- **FTP (File Transfer Protocol) Port 21**: FTP is a protocol used to transfer files between devices over a network. FTP is used to upload and download files from a remote server and is commonly used to manage websites and transfer files securely.

>This is an really short introduction to networking. There are many more concepts and technologies in networking that we haven't covered in this session. These basics should be enough to get you started with networking and understand how devices communicate over a network. If you are interested in learning more about networking, there are many online resources and courses available that cover networking in more detail. Check out the ***Hack The Box Academy - Introduction to Networking*** Course for a more in-depth look at networking concepts and technologies.