📋 What is This?
This is a web-based chat app where two users on different virtual machines can send messages to each other in real-time without refreshing the page.
Technologies Used:

Python Flask (Backend)
HTML/CSS/JavaScript (Frontend)
AWS EC2 (Cloud Hosting)
AJAX (Real-time Communication)


🚀 Quick Setup Guide
Prerequisites

AWS Account (Free Tier)
Basic knowledge of Linux terminal
Web browser


📦 Installation
Step 1: Create Two AWS EC2 Instances

Log in to AWS Console → EC2
Click "Launch Instance"
Configure:

Name: ChatVM1 (then repeat for ChatVM2)
AMI: Ubuntu Server 22.04 LTS
Instance Type: t2.micro (Free tier)
Key pair: Proceed without a key pair
Security Group Rules:

SSH (Port 22) - Source: 0.0.0.0/0
HTTP (Port 80) - Source: 0.0.0.0/0
Custom TCP (Port 5000) - Source: 0.0.0.0/0




Launch both instances
Note down both Public IP addresses


Step 2: Connect to EC2 Instances

Select instance → Click "Connect"
Choose "EC2 Instance Connect"
Click "Connect" (opens browser terminal)
Repeat for both VMs (use two browser windows)


Step 3: Install Dependencies (On Both VMs)
bash# Update system
sudo apt update

# Install Flask
sudo apt install python3-flask python3-flask-cors -y

# Verify installation
python3 -c 'import flask; print("Flask installed!")'

Step 4: Download and Setup Files (On Both VMs)
bash# Create directory
mkdir ~/chat-app
cd ~/chat-app

# Download files from GitHub
# Option 1: Clone the repository
git clone https://github.com/dew-13/http-chat-application.git
cd http-chat-application

# Option 2: Create files manually (copy from repository)
# Create app.py and index.html
Or create files manually:
Create app.py:
bashnano app.py
# Copy the app.py content from this repository
# Save: Ctrl+X, then Y, then Enter
Create index.html:
bashnano index.html
# Copy the index.html content from this repository
# Save: Ctrl+X, then Y, then Enter

Step 5: Run the Application (On Both VMs)
bashcd ~/chat-app
python3 app.py
You should see:
 * Running on http://0.0.0.0:5000
⚠️ Keep both terminals open!

🌐 How to Use
Step 1: Open Chat in Browser
Open two browser tabs:

Tab 1: http://<VM1_PUBLIC_IP>:5000
Tab 2: http://<VM2_PUBLIC_IP>:5000

Replace <VM1_PUBLIC_IP> and <VM2_PUBLIC_IP> with your actual EC2 public IP addresses.

Step 2: Configure Chat Settings
In Browser Tab 1 (VM1):

Username: Alice
Remote Server IP:Port: <VM2_PUBLIC_IP>:5000

In Browser Tab 2 (VM2):

Username: Bob
Remote Server IP:Port: <VM1_PUBLIC_IP>:5000


Step 3: Start Chatting!
Type a message and click Send. Messages will appear on both screens in real-time! 🎉
