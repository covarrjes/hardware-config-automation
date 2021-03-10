import getpass
# Switch configuration


class Switch:

    def __init__(self, name, address):
        self.name = name
        self.host = address
        self.subnet = "255.255.255.0"
        self.banner = ""
        self.interfaces = {}
        self.vlan = {}
        self.telnet_pass = ""
        self.enable_pass = ""

    # set password, for enable (1) or telnet (2)
    def set_pass(self, option):
        if option == 1:
            # p = getpass.getpass(prompt="Enter enable password: ")
            p = input("Enter the enable password: ")
            self.enable_pass = p
        if option == 2:
            p = input("Enter the telnet password: ")
            self.telnet_pass = p
            # p = getpass.getpass(prompt="Enter telnet password: ")
        return p

    @staticmethod
    def set_telnet(password):
        return "line vty 0 15\n" + "password " + password + "\n" + "login\n" + "exit\n"

    def get_host_address(self):
        return self.host

    # return hostname string to telnet
    def get_name(self):
        return "hostname " + self.name + "\n"

    # set switch banner attribute
    def set_banner(self, message):
        self.banner = message

    # return banner string to telnet
    def get_banner(self):
        return "banner motd " + self.banner + "\n"

    # take interface # and assign it to a host within an interfaces dictionary
    def set_interface(self, interface, to_host):
        self.interfaces[interface] = to_host

    # return interface config with desired host number
    def get_interface(self, interface):
        return "interface " + interface + " " + self.interfaces[interface] + "\n"

    # take vlan_id and assign to a host range within interface / address table
    def set_vlan(self, vlan_id, name, network):
        self.vlan[vlan_id] = {'port': "ports", 'name': name, 'network': network}

    # return vlan name at index to telnet
    def get_vlan_name(self, vlan_id):
        return self.vlan[vlan_id]['name']

# vlan is a 2d array
