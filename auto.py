import boto3

def fetch_ips(auto_scaling_group_name):
    # Create a session
    session = boto3.Session()
    
    # Create an autoscaling client
    autoscaling_client = session.client('autoscaling')

    try:
        # Describe the Auto Scaling group
        response = autoscaling_client.describe_auto_scaling_groups(AutoScalingGroupNames=[auto_scaling_group_name])
        
        # Retrieve instances from the response
        instances = response['AutoScalingGroups'][0]['Instances']
        
        # Print the private IP addresses of instances
        for instance in instances:
            print(instance['PrivateIpAddress'])
    except Exception as e:
        print(f"Error fetching IPs: {str(e)}")

# Provide the name of the Auto Scaling group
auto_scaling_group_name = 'my-autoscaling-group'

# Call the function to fetch IPs
fetch_ips(auto_scaling_group_name)
