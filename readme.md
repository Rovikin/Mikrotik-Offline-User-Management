# Mikrotik Offline User Management

This project allows you to store user vouchers imported from Mikhmon in a CSV format into a database using Python. It can be run offline on Termux or Linux.

## Features
- Import user vouchers from a CSV file.
- Store voucher data into a local database.
- Run the application offline in Termux or Linux.

## Getting Started

### Prerequisites
- Python 3.x
- Termux (for Android) or a Linux environment

### Installation and Usage

#### Termux Installation

1. **Install Termux from the Play Store or F-Droid.**
2. **Update packages:**
   ```bash
   pkg update && pkg upgrade

#### Install Python and Git:**
   '''bash
   pkg install python git

#### Clone the repository:
   '''bash
   git clone https://github.com/Rovikin/Mikrotik-Offline-User-Management.git

#### Navigate to the project directory:
   '''bash
   cd ~/path/to/your/directory/Mikrotik-Offline-User-Management

#### Install required Python packages:
   '''bash
   pip install -r requirements.txt
#### Import your CSV file into the data/ directory. The CSV format should be:
   '''bash
   id,username,password
#### Run the application:
   '''bash
   python app.py

### Linux Installation

#### Install Python and Git:
   '''bash
   sudo apt update
   sudo apt install python3 git

#### Clone the repository:
   '''bash
   git clone https://github.com/Rovikin/Mikrotik-Offline-User-Management.git

#### Navigate to the project directory:
   '''bash
   cd /path/to/your/directory/Mikrotik-Offline-User-Management

#### Install required Python packages:
   '''bash
   pip3 install -r requirements.txt

#### Import your CSV file into the data/ directory. The CSV format should be:
   '''bash
   id,username,password

#### Run the application:
   '''bash
   python3 app.py
