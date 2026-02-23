# Run backup.py every day at 1 AM
0 1 * * * /usr/bin/python3 /path/to/scripts/backup.py >> /path/to/logs/backup.log 2>&1

# Optional: run failover check every hour
0 * * * * /usr/bin/python3 /path/to/scripts/failover.py >> /path/to/logs/failover.log 2>&1
