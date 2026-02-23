import boto3

# Connect to AWS EC2 in primary region
ec2 = boto3.client('ec2', region_name='us-east-1')

# Describe all instances
instances = ec2.describe_instances()
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        # Create snapshot for each instance
        snapshot = ec2.create_snapshot(
            InstanceId=instance_id,
            Description='Automated backup'
        )
        print(f"Snapshot created for {instance_id}: {snapshot['SnapshotId']}")
