import json

with open(r"lab4\sample-data.json", "r") as file:
    data = json.load(file)

information = data["imdata"] #We take all infom which contain under key "imdata"
print("Interface Status")
print("="*90)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<6}")
print("-"*90)
for item in information:
    attribute = item["l1PhysIf"]["attributes"]
    dn = attribute["dn"]
    description = attribute["descr"] if attribute["descr"] else ""
    speed = attribute["speed"]
    mtu = attribute["mtu"]
    print(f"{dn:<47} {description:<23} {speed:<10} {mtu:<10}")