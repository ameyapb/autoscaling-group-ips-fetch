This project provides a Python script that fetches the IP addresses of live servers in an Auto Scaling group using the AWS SDK (boto3). The script is designed to retrieve the private IP addresses of instances within the specified Auto Scaling group.

Before running the script, ensure that you have the necessary prerequisites in place. First, create an AWS account if you don't have one already. You can sign up for an AWS Free Tier account, which provides limited usage for free. Next, install the AWS CLI (Command Line Interface) on your system and configure it with your AWS credentials. This will allow the script to authenticate and interact with AWS services. Additionally, make sure Python 3 is installed on your system along with the required dependencies, including `boto3`, which can be installed using pip.

To use the script, start by cloning this repository to your local machine or server. Install the required dependencies using pip. Then, configure your AWS credentials by running `aws configure` in the command line and providing your Access Key ID, Secret Access Key, default region, and output format. Next, open the `fetch_ips.py` file in a text editor and replace `'my-autoscaling-group'` with the actual name of your Auto Scaling group. Save the file and close the text editor. Finally, run the script by executing `python fetch_ips.py` in the command line.

Upon execution, the script will use the AWS SDK (boto3) to communicate with AWS services. It will retrieve the IP addresses of the live servers within the specified Auto Scaling group and display them on the console. Note that the script assumes the instances in the Auto Scaling group have private IP addresses. If you need to fetch public IP addresses, modify the script accordingly.
