# thunes_test
* This branch is for the docker-compose files, you can download these files to start up the docker-compose cluster.
* here is the file struct for this folder:
```
.
├── docker-compose.yml -> (docker-compose defined yaml file)
├── nginx
│   ├── backend.conf 
│   ├── default.conf -> (the nginx config file and its proxy setting for backend)
│   ├── Dockerfile -> (the docker file to build the nginx image)
│   ├── nginx.conf
│   ├── static -> (the static file for backend css)
│   ├── tmp_log -> (the volume to bind with the tmp folder for nginx container)
│   ├── var_log -> (the volume to bind with the var folder for nginx container)
│   └── vuejs -> -> (the file for built vuejs code)
│       ├── index.html
│       └── static
├── postgres (the volume to bind with the postgres container)
│   ├── backup
│   └── data
├── README.md
├── .env -> (the env para file to define env for multi container)
└── thunes_test 
    ├── APISecret.ini -> (the file to define the api secret and key as well as base url)
    ├── Dockerfile (the docker file to build the django image)
    ├── requirements.txt (the file to install required python package when building)
    ├── run_supervisord.sh (the entrypoint script for django container)
    └── supervisord.conf (the supervisord config file)
```
### The step to run this docker-compose cluster ###
1. check your machine has installed the docker-compose by typing this below command:
  ```
  docker-compose -version
  docker-compose version 1.24.0, build 0aa59064
  ```
  this output will notify you the docker-compose has been successfully installed in your VM.

2. please go to this folder and make some changes for it.
* create a file named **APISecret.ini** in the **thunes_test** folder and configure the api secret and key as well as the baseurl in this file like this format
  ```
  [Global]
  API_BASE_URL = https://xxx.xx.xx.xxx.com/
  API_KEY = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  API_SECRET = xxxxxxxxxxxxxxxxxxxxxxxxxxxx
  ```
 * edit the http_proxy and https_proxy in the **Dockerfile** in this **thunes_test** folder like this format
  ```
  # Configure the Proxy for this image.
  # Please change it based on your own Host Env.
  ENV workdir=/opt/Thunes/ \
         http_proxy=http://xxx.xx.xxx:xxxx \
         https_proxy=http://xxx.xx.xxx:xxxx
  ```
  if you do not want to configure the proxy, you can comment or delete these two parameter setting and please do not forget to delete the anti-slash " \ " behind the setence "ENV workdir=/opt/Thunes/"
  * please make sure these ports in your vm has not been occupied by other applications.
  - 8080:8080
  - 5433:5432
  - 8000:8000
  - 8001:8001
  - 9001:9001
  if you would like to expose other ports, please change these ports configurations in the docker-compose.yml

  3. after these changes have been done. you can run these below commands to start up the application
  ```
  docker-compose up -d
  docker-compose ps
  ```
  the first command is to start up the docker-compose cluster in the back-end.
  the second command is to check all docker containers running status and its port expose status.
  
  4. the index page is opened at the port 8080 with default and you can see below page when you access the webpage:
  ![home page](image/home.jpg)
  
  5. and please open the /api/docs path to review all apis exposed in the backend:
  ![api docs page](image/apidocs.jpg)
  
  (PS: somehow, this api cannot be interconnect with as I review every request will miss the port para when sending to backend. currently, I have no idea with issue why this para will be lost when running in the container)
