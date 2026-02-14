from models import WifiNetwork

def analyze_networks(raw_data):
    analyzed = []

    for item in raw_data:
        network = WifiNetwork(
            ssid=item["ssid"],
            signal=item["signal"],
            encryption=item["encryption"]
        )
        analyzed.append(network)

    return analyzed

