# Firewall Rule Generator

A simple Python tool that creates firewall rules for iptables, ufw (Ubuntu), and AWS Security Groups based on user input. Great for scripting practice and understanding how common firewall configurations work.

---

## 🔧 What It Does

- Takes in an IP address, port number, protocol, and action (allow/deny)
- Outputs:
  - An `iptables` rule
  - A `ufw` rule
  - A properly structured AWS Security Group rule in JSON

---

## 🚀 How to Use

1. **Install Python 3**
2. Run the script:

   ```bash
   python rule_generator.py
3. Enter details when prompted
	IP address: 192.168.1.100
	Port: 22
	Protocol: tcp
	Action: allow

Example Output

css
Copy
Edit
[iptables]
iptables -A INPUT -p tcp --dport 22 -s 192.168.1.100 -j ALLOW

[ufw]
ufw allow from 192.168.1.100 to any port 22 proto tcp

[AWS Security Group]
{
    "IpProtocol": "tcp",
    "FromPort": 22,
    "ToPort": 22,
    "IpRanges": [{"CidrIp": "192.168.1.100/32"}]
}
