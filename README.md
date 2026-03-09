🛡️ DroidHunter

DroidHunter is a professional Android APK static analysis framework designed to identify security vulnerabilities, misconfigurations, and potential threats in mobile applications.

The tool performs automated security analysis on Android packages using a modular architecture, making it suitable for:

Security researchers

Penetration testers

Mobile application developers

DevSecOps pipelines

Security audits

🚀 Features
🔍 Comprehensive Static Analysis

The scanner analyzes multiple components of Android applications:

Manifest Analyzer – Detects insecure permissions and misconfigurations

Network Analyzer – Identifies insecure network configurations

Code Analyzer – Searches for insecure coding patterns

Cryptography Analyzer – Detects weak encryption usage

File Analyzer – Finds sensitive files and exposed assets

⚙️ DevSecOps Ready

Built for modern development workflows:

CI/CD pipeline integration

Automated vulnerability detection

Security policy enforcement

🐳 Docker Support

Run scans in isolated environments using Docker containers.

🧩 Modular Architecture

The framework is designed for extensibility. Developers can easily add:

Custom analyzers

Security rules

Additional reporting formats

🎓 Educational Security Scanner

Includes an educational vulnerability scanner to demonstrate Android security analysis techniques.

📦 Installation
Clone the Repository
git clone https://github.com/yourusername/mobile-security-scanner.git
cd mobile-security-scanner
Install Dependencies
pip install -r requirements.txt
Optional: Development Environment
pip install -r requirements-dev.txt
⚙️ Requirements

Before running the scanner ensure the following tools are installed:

python >= 3.8
java >= 8
apktool

Install apktool on Linux:

sudo apt install apktool
▶️ Running the Scanner

Basic scan:

python -m src.scanner app.apk

Example:

python -m src.scanner sample.apk
⚡ Advanced Usage

Run with verbose output:

python -m src.scanner app.apk --verbose

Specify thread count:

python -m src.scanner app.apk --threads 8

Generate report:

python -m src.scanner app.apk --format html
🐳 Running with Docker

Build the Docker image:

docker build -t mobile-security-scanner .

Run scan inside container:

docker run -v $(pwd):/workspace mobile-security-scanner app.apk
🧪 Running Tests

Execute unit tests:

pytest tests/

⚠️ Disclaimer

This tool is intended for authorized security testing and educational purposes only.

Unauthorized scanning of applications or systems without permission may violate laws and regulations.

📄 License

This project is licensed under the MIT License.
