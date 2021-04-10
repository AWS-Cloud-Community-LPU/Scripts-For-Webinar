# Script for Installing Wordpress and enabling it
# in AWS EC2.

import os


os.system("yum install mysql")
os.system("amazon-linux-extras install php7.2")
os.system("yum install httpd")
os.system("wget https://wordpress.org/latest.tar.gz")
os.system("tar -xzf latest.tar.gz")
# open the httpd.conf file and change the overide from none to all
os.system("systemctl start httpd")
# os.system("mysql -h RDS_ENDPOINT -u admin -p")