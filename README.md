# Automated-Cloud-Disaster-Recovery-System
Automated Cross-Region Disaster Recovery Architecture | AWS, Python, Bash, Linux  Designed and implemented a highly available AWS disaster recovery solution across multiple regions.
# Automated Multi-Region Cloud Disaster Recovery & Failover System

## Overview
This project simulates a multi-region AWS disaster recovery system with automation, monitoring, and failover.

## Technologies
- AWS (EC2, IAM, VPC, S3, CloudWatch)
- Python, Bash
- Linux (Ubuntu)
- Route53 (DNS failover)

## Features
- Multi-region EC2 disaster recovery
- Automated snapshot backups using Python & Bash
- DNS failover for minimal downtime
- IAM least-privilege policies for secure access
- CloudWatch monitoring for system reliability
- Simulated high availability and DR workflows

## How to Run
1. Configure AWS credentials or attach IAM role
2. Launch EC2 instances in primary & DR regions
3. Run scripts/backup.py for automated snapshots
4. Run scripts/failover.py to simulate DR
5. Monitor CloudWatch metrics

## Architecture
![Architecture Diagram](docs/architecture_diagram.png)

## Results
- Snapshots stored in S3
- Automated failover tested
- Minimal downtime achieved in simulated outages
