def generate_iptables_rule(ip, port, protocol, action):
    return f"iptables -A INPUT -p {protocol} --dport {port} -s {ip} -j {action.upper()}"

def generate_ufw_rule(ip, port, protocol, action):
    return f"ufw {action.lower()} from {ip} to any port {port} proto {protocol}"

def generate_aws_sg_rule(ip, port, protocol):
    return {
        "IpProtocol": protocol,
        "FromPort": int(port),
        "ToPort": int(port),
        "IpRanges": [{"CidrIp": f"{ip}/32"}]
    }

def main():
    print("🔥 Firewall Rule Generator 🔥\n")

    ip = input("Enter the IP address (e.g. 192.168.1.10): ").strip()
    port = input("Enter the port number (e.g. 22): ").strip()
    protocol = input("Enter the protocol (tcp/udp): ").strip().lower()
    action = input("Allow or Deny (used for iptables/ufw): ").strip().lower()

    print("\n📄 Generated Rules:\n")

    print("[iptables]")
    print(generate_iptables_rule(ip, port, protocol, action))

    print("\n[ufw]")
    print(generate_ufw_rule(ip, port, protocol, action))

    print("\n[AWS Security Group]")
    import json
    print(json.dumps(generate_aws_sg_rule(ip, port, protocol), indent=4))

if __name__ == "__main__":
    main()
