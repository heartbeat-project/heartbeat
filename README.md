# Heartbeat
- **Original Authors** : Patricia Raftery, Keith Eckert and Jay Adams
- **Open Source Project Lead** Keith Eckert
- **Version**: 0.1.1

### Contact Us
- **email**: [heartbeat.opensource@gmail.com]


[![Coverage Status](https://coveralls.io/repos/github/lwb-connect/lwb_heartbeat/badge.svg?branch=development)](https://coveralls.io/github/lwb-connect/lwb_heartbeat?branch=development)



[![Build Status](https://travis-ci.org/lwb-connect/lwb_heartbeat.svg?branch=development)](https://travis-ci.org/lwb-connect/lwb_heartbeat.svg?branch=development)


## Overview
Heartbeat is a logistics and data managment web application being built for an international charity that provides hope and healing to orphaned and vulnerable children, and their underserved communities, through its education, nutrition, medical, and foster care programs.  

Heartbeat's goals:

* Automate and streamline data input from users across the world.

* Make data useful and meaningful to help them fulfull their primary mission.

* Provide tracking and reporting for people, children and programs in their care.

* Allow staff access only to data within their work scope.

* Always keep this data safe and secure.



![Current Heartbeat Front Page](/assets/heartbeatfrontpage.png)


![Current Database Model](/assets/ERD_entity_relationship_diagram.png)


## Contributing
---------------

* We welcome and encourage contributions to Heartbeat.  Together we can make this world a little better!

* First, please read and agree to our [Code of Conduct](/code-of-conduct.md).

### How to Contribute

* A great place to start is with the Issues tab in this repository.  

* Take a look at labels ```enhancement, bug, testing, future``` and check to see if an issue has been assigned before starting.  

* Always make sure you are using the current deployment code in the master branch.  

* For a contribution (pull request) to be considered, please document and test all code.


## Getting Started
---------------
 Create an LWB_heartbeat clone for organizing and viewing and managing the childrens information.  This app is designed to be deployed on AWS EC2 via ansible and utilizes an AWS RDS postgreSql database.   More features to come later....
*  Project-specific env variables
* `export SECRET_KEY='secret key'`
* `export DEBUG=True`
* `export DB_NAME=''`
* `export DB_USER=''` set these two if need for linux
* `export DB_PASSWORD=''`
* `export DB_HOST='localhost'` 

### initalize and run server

* `dropdb $DB_NAME`
* `createdb $DB_NAME`
* `./manage.py makemigrations`
* `./manage.py migrate`
* `./manage.py compilescss`
* `./manage.py collectstatic`
* `./manage.py check`
* `./manage.py test`
* `./manage.py runserver`


## Assets


## Architechture
Python 3.6
Django
venv
AWS EC2
AWS RDS
Ansible
Ansible playbook

## API
None at this time

## Change log
| pull | comment|
| --------- |:--------------------------------------------:|
| 18950bb | (HEAD -> jay-tues-child)  fix readme.md |
| d4578bc | (origin/development, origin/HEAD) Merge pull request #17 from lwb-connect/jay-tues-child |
| 9c514b8 | (origin/jay-tues-child) clean up doc strings |
| b864d88 | models edited, added relationships, remamed user app to staff, edit urls, added pillow |
| 08c593b | models edited, added relationships, remamed user app to staff, edit urls, added pillow |
| 6dc1191 | models edited, added relationships, remamed user app to staff, edit urls, added pillow |
| 7fd00d4 | Merge pull request #15 from lwb-connect/jay-tues-child |
| bed55c4 | clean up docs in users. |
| 0629e0d | Merge pull request #14 from lwb-connect/mon-images |
| bcfb8de | started testing, changed models, views, html |
| a2caba6 | (jay-mon-child-two, development) Merge pull request #13 from lwb-connect/keith-monday |
| 5712cc0 | model relationhips working |
| 8a100b2 | Merge branch 'development' of https://github.com/lwb-connect/lwb_heartbeat into keith-monday |
| 7d9c4b3 | settings import to urls |
| 79da762 | Merge pull request #12 from lwb-connect/mon-images |
| d2ef513 | Merge pull request #11 from lwb-connect/jay-mon-child |
| a40cf51 | (origin/jay-mon-child, jay-mon-child) create child app |
| 3a6b8a3 | started form for adding photo, started view for adding and viewing photos, wrote urls |
| 27599b8 | Merge pull request #10 from lwb-connect/mon-images |
| e347217 | fixing ansible |
| e3e5dd0 | Merge pull request #9 from lwb-connect/jay-05-21-travis |
| 78d05d2 | Open Source Prepertions |