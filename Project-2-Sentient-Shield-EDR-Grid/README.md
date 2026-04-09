# 🛡️ Project 2 – Sentient Shield EDR Grid

## 📌 Overview
Sentient Shield is an enterprise-style Endpoint Detection and Response (EDR) and Security Information and Event Management (SIEM) home lab built using **Wazuh**.

The objective of this project is to design and deploy a **centralized threat monitoring and detection environment** capable of collecting logs, detecting suspicious behavior, and automatically responding to potential security incidents.

The lab simulates a **Security Operations Center (SOC)** environment where endpoints are monitored for malicious activity and alerts are generated for security analysts.

---

# 🏗️ Lab Architecture

                 ┌─────────────────────────┐
                 │     Kali Linux VM       │
                 │       (Attacker)        │
                 │  Hydra / Recon / Tests  │
                 └─────────────┬───────────┘
                               │
                               │ Attack Simulation
                               ▼
┌─────────────────────────────────────────────────┐
│                Windows Endpoint                 │
│                                                 │
│ • Wazuh Agent                                   │
│ • Sysmon                                        │
│ • Windows Security Event Logs                   │
│                                                 │
└───────────────┬─────────────────────────────────┘
                │
                │ Log Collection
                ▼
        ┌─────────────────────────────┐
        │        Ubuntu Server        │
        │                             │
        │  🧠 Wazuh Manager           │
        │  🗄️ Wazuh Indexer (Logs DB) │
        │  📊 Wazuh Dashboard         │
        │                             │
        │  Threat Detection           │
        │  Alert Correlation          │
        │  Security Monitoring        │
        └─────────────────────────────┘


---

# 📅 Week-1-Infrastructure-and-Agent-Deployment

## Objective
Deploy the SIEM infrastructure and connect monitored endpoints.

## Tasks Completed
- Installed Wazuh Manager on Ubuntu server
- Configured Wazuh Dashboard
- Installed Wazuh Indexer
- Deployed Wazuh Agent on Windows endpoint
- Installed Sysmon for enhanced Windows logging
- Connected Windows endpoint to the Wazuh server
- Verified agent communication and log ingestion

## Outcome
A functional SIEM infrastructure was deployed and endpoint logs were successfully collected by the Wazuh server.

---

# 📅 Week-2-Detection-Rules

## Objective
Configure detection mechanisms to monitor suspicious system activity.

## Tasks Completed
- Enabled File Integrity Monitoring (FIM)
- Monitored sensitive directories for file changes
- Enabled Vulnerability Detection module
- Verified Windows security event collection
- Tested detection by modifying monitored files
- Observed alerts generated in the Wazuh dashboard

## Outcome
The SIEM system successfully detected file changes and generated security alerts in real time.

---

# 📅 Week-3-Active-Response

## Objective
Implement automated response actions for detected threats.

## Tasks Completed
- Configured Active Response rules in Wazuh
- Implemented firewall-based response actions
- Simulated multiple authentication failures
- Triggered brute-force detection alerts
- Monitored automated response activity through system logs

## Outcome
Wazuh successfully detected suspicious login attempts and initiated automated response actions based on configured rules.

---

# 📅 Week-4-Threat-Simulation

## Objective
Simulate attacker behavior and validate detection capabilities.

## Threat Simulations Performed

PowerShell Execution
powershell -ExecutionPolicy Bypass -Command "whoami"

Account Discovery
net user

System Information Discovery
systeminfo

Suspicious File Creation
echo malware > C:\Users\Public\malware.exe

---

# 🚨 Alerts Observed
The Wazuh SIEM detected multiple suspicious activities including:

- PowerShell execution events
- Account discovery commands
- Suspicious file creation
- Authentication failures

Alerts were visualized through the **Wazuh Security Events dashboard** with varying severity levels.

---

# 🔍 Security Monitoring Capabilities Demonstrated

- Endpoint log collection
- Security event correlation
- Suspicious process detection
- Brute-force login detection
- File integrity monitoring
- Automated threat response
- Security alert visualization
- Threat simulation and analysis

---

# 🧰 Technologies Used

| Tool | Purpose |
|-----|--------|
| Wazuh | SIEM and threat detection platform |
| Ubuntu Server | Wazuh Manager host |
| Windows 10 | Monitored endpoint |
| Sysmon | Advanced Windows event logging |
| Kali Linux | Attack simulation machine |
| VMware Workstation | Virtual lab environment |

---

# 📊 Conclusion
This project successfully implemented a functional SIEM monitoring environment using Wazuh.

The system was able to collect logs, detect suspicious activities, generate alerts, and simulate attack scenarios.

The final setup demonstrates how SIEM solutions help security teams monitor endpoints, identify potential threats, and respond to suspicious activity in real time.

---

# 🚀 Future Improvements

- Integration with threat intelligence feeds
- Advanced detection rule customization
- Automated incident response playbooks
- Log monitoring across multiple endpoints
