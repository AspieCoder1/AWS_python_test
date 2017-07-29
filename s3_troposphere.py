from troposphere import Template
import troposphere.ec2 as ec2

t = Template()
instance = ec2.Instance("Server1")
instance.ImageId = "ami-951945d0"
instance.InstanceType = "t1.micro"
t.add_resource(instance)
f = open('./test.json', 'w')
f.write(str(t.to_json()))
