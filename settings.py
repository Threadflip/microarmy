# Override any keys below by putting them in a local_settings.py. Some
# overrides are required, signaled by a #* on the same line.

import os

### Get these from: http://aws-portal.amazon.com/gp/aws/developer/account/index.html?action=access-key
aws_access_key = None #*
aws_secret_key = None #*

### aws security config
security_groups = None

### key pair name
key_pair_name = 'AppExecutor.east'

### path to ssh private key
### Will resolve ~
ec2_ssh_key = '/Users/jku/.ssh/AppExecutoreast.pem' #*
ec2_ssh_username = 'ubuntu' # ami specific
ec2_ssh_key_password = None # only required if your ssh key is encrypted

### five cannons is a healthy blast
num_cannons = 20

### Availbility zones: http://alestic.com/2009/07/ec2-availability-zones
placement = 'us-east-1a'

### ami key from: http://uec-images.ubuntu.com/releases/11.10/release/
ami_key = 'ami-a7f539ce'
instance_type = 't1.micro'

### enable cloud init, so that a second deploy step is not required
enable_cloud_init = True

### scripts for building environments
env_scripts_dir = os.path.abspath(os.path.dirname('./env_scripts/'))

### Siege config settings
siege_config = {
    'connection': 'close',
    'concurrency': 200,
    'internet': 'true',
    'time': '5M'
}

## Siege urls
siege_urls = []
siege_urls_template = [
    'http://stimpy.stack.aws.threadflip.com/items.json?page=',
    'http://stimpy.stack.aws.threadflip.com/items.json?sort=popularity&page=',
    'http://stimpy.stack.aws.threadflip.com/items.json?sort=score&page=',
    'http://stimpy.stack.aws.threadflip.com/items.json?sort=pricedrop_recency&page='
]

for i in range(1,51):
    for url in siege_urls_template:
        siege_urls.append(url + str(i))

try:
    from local_settings import *
except:
    pass
