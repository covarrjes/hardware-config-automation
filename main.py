# Cisco Device Configs
import telnetlib
import switch

# Constant Variables = Frequently used commands
ENABLE = "enable\n"
CONFIG_T = "configure terminal\n"
NO_SHUT = "no shutdown\n"


def router_config():
    print("router config")


def switch_config():
    naming_convention = input("Choose naming convention: ")
    switch_count = int(input("How many switches would you like to configure?: "))
    vlan_count = int(input("How many vlans would you like to initialize?: "))
    message = input("Set your banner message: ")
    switch_list = []
    for i in range(switch_count):
        host_name = (naming_convention + str(i))
        host_address = input("Enter Host Address for " + host_name + ": ")
        sw = switch.Switch(host_name, host_address)
        for j in range(vlan_count):
            sub_vlan = (int(j) + 1) * 10
            host = "192.168." + str(sub_vlan) + ".0"

            sw.set_banner(message)
            name = input("Set vlan " + str(sub_vlan) + " name: ")
            # port_range = input("Set vlan " + sub_vlan + " port range: ")
            sw.set_vlan(sub_vlan, name, host)
            switch_list.append(sw)
        run_switch(sw)
    print("switch config")


def run_switch(sw):
    HOST = sw.get_host_address()
    tn = telnetlib.Telnet(HOST)
    tn.write(ENABLE)
    tn.write(CONFIG_T)
    tn.write(sw.get_name)
    tn.write(sw.get_banner)
    tn.write(sw.set_telnet(sw.set_pass(2)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(__name__)
    choice = input("R or S config: ")

    if choice == "s" or choice == "S":
        switch_config()
    else:
        router_config()