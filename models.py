class WifiNetwork:
    def __init__(self, ssid, signal, encryption):
        self.ssid = ssid
        self.signal = signal
        self.encryption = encryption
        self.risk = self.calculate_risk()

    def calculate_risk(self):
        if self.encryption == "OPEN":
            return "HIGH"
        elif self.encryption == "WEP":
            return "HIGH"
        elif self.encryption == "WPA":
            return "MEDIUM"
        elif self.encryption == "WPA2":
            return "LOW"
        elif self.encryption == "WPA3":
            return "VERY LOW"
        else:
            return "UNKNOWN"
