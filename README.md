#  Smartwatch Application Installer (Terminal CLI)

A lightweight, cross-platform terminal-based installer simulator for smartwatch applications. Perfect for demos, testing installation flows, or adding a CLI tool to your wearable app project.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)

##  Features

-  Simulates complete smartwatch app installation process
-  Real-time progress indicators with step-by-step feedback
-  Permission checks (HR, GPS, Notifications)
-  Storage validation
-  Battery optimization simulation
-  Optional uninstall flow
-  Colorful terminal output (auto-detects support)
-  Easy to extend for real watchOS/Wear OS deployment

##  Quick Start

### Prerequisites
- Python 3.7 or higher
- Terminal with UTF-8 support (for emoji icons)

### Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/smartwatch-installer.git
cd smartwatch-installer
```

Make the script executable (Linux/macOS):
```bash
chmod +x watch_installer.py
```

### Usage

Run with app name as argument:
```bash
python3 watch_installer.py "FitnessPro"
```

Or run interactively:
```bash
python3 watch_installer.py
```

##  Examples

### Basic Installation
```bash
$ python3 watch_installer.py "HeartMonitor"

 Smartwatch App Installer
 Target watch: 192.168.1.100
 App: HeartMonitor

 Connecting to smartwatch... ✓
 Authenticating device... ✓
 Checking storage space... ✓
 Uploading app bundle... ✓
 Installing dependencies... ✓
 Setting permissions (HR, GPS, Notifications)... ✓
 Optimizing for battery life... ✓
 Finalizing installation... ✓

 Installation complete!
 HeartMonitor is now ready on your smartwatch.
```

### Custom Watch IP
Edit the `watch_installer.py` file to change the target IP:
```python
terminal_installer("MyApp", watch_ip="10.0.0.5")
```

##  Configuration

You can modify the installation steps in the script:

| Step | Description | Default Duration |
|------|-------------|------------------|
| Connecting | Network handshake | 1.0 sec |
| Authenticating | Device verification | 1.0 sec |
| Storage check | Available space | 0.8 sec |
| Upload bundle | Transfer files | 1.5 sec |
| Dependencies | Install libs | 1.2 sec |
| Permissions | Grant access | 1.0 sec |
| Battery opt | Power tuning | 0.7 sec |
| Finalize | Complete setup | 0.5 sec |

##  Real-World Adaptation

This simulator can be easily adapted for actual smartwatch deployments:

### For Wear OS (Android)
Replace simulation with ADB commands:
```python
import subprocess
subprocess.run(["adb", "connect", watch_ip])
subprocess.run(["adb", "install", "app.apk"])
```

### For watchOS
Use `xcrun` with Apple devices:
```python
subprocess.run(["xcrun", "simctl", "install", "watch", "app.app"])
```

##  Project Structure

```
smartwatch-installer/
├── watch_installer.py      # Main installer script
├── README.md               # This file
├── LICENSE                 # MIT License
└── examples/
    └── custom_installer.py # Extended example
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for improvement
- Add support for multiple watch connections
- Include configuration file for custom steps
- Add logging to file
- Create GUI wrapper (Tkinter/PyQt)
- Support for OTA (Over-the-Air) updates simulation

##  License

Distributed under the MIT License. See `LICENSE` for more information.

##  Acknowledgments

- Inspired by real wearable device installation flows
- Terminal emoji support from [emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet)

##  Contact

Om Gedam

GitHub: [https://github.com/itsomg134](https://github.com/itsomg134)

Email: [omgedam123098@gmail.com](mailto:omgedam123098@gmail.com)

Twitter (X): [https://twitter.com/omgedam](https://twitter.com/omgedam)

LinkedIn: [https://linkedin.com/in/omgedam](https://linkedin.com/in/omgedam)

Portfolio: [https://ogworks.lovable.app](https://ogworks.lovable.app)
