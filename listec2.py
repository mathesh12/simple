import boto3

client = boto3.client('ec2',
		region_name = 'ap-south-1',
		aws_access_key_id = 'AKIA57VDLY3OAZWZHLEV',
		aws_secret_access_key = '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')
		
myec2 = client.describe_instances()
for printins in myec2['Reservations']:
	for printout in printins['Instances']:
		for printname in printout['Tags']:
			print(printout['InstanceId'])
			print(printout['InstanceType'])
			print(printout['LaunchTime'])
			print(printout['State']['Name'])
			print(printname['Value'])
		


print(myec2['Reservations'])
