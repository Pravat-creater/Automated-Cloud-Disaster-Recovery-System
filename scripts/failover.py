import boto3

# Connect to AWS EC2 in DR region
ec2_dr = boto3.client('ec2', region_name='us-west-2')

# Launch a backup instance in DR region
response = ec2_dr.run_instances(
    ImageId='ami-xxxxxxxx',  # Use your backup AMI
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='your-keypair',
    SecurityGroupIds=['sg-xxxxxx']
)
instance_id = response['Instances'][0]['InstanceId']
print(f"DR instance launched: {instance_id}")

# Optional: Update Route53 DNS to point to DR instance
