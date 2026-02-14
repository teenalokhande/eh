import json
from analyzer import analyze_networks

def load_data():
    with open("wifi_data.json", "r") as file:
        return json.load(file)

def generate_report(networks):
    with open("report.txt", "w") as report:
        report.write("WIFI SECURITY ANALYSIS REPORT\n")
        report.write("============================\n\n")

        for net in networks:
            report.write(f"SSID       : {net.ssid}\n")
            report.write(f"Signal     : {net.signal} dBm\n")
            report.write(f"Encryption : {net.encryption}\n")
            report.write(f"Risk Level : {net.risk}\n")
            report.write("-----------------------------\n")

def main():
    print("starting wifi security analysis...\n")

    raw_data = load_data()
    networks = analyze_networks(raw_data)
    generate_report(networks)

    for net in networks:
        print(f"{net.ssid} | {net.encryption} | Risk: {net.risk}")

    print("\nanalysis completed. report generated.")

if __name__ == "__main__":
    main()
