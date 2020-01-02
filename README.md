# thunes_test
* This branch is for the docker-compose files, you can download these files to start up the docker-compose cluster.
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
  if you do not want to configure the proxy, you can comment or delete these two parameter setting and please do not forget to delete the   "\" behind the setence "ENV workdir=/opt/Thunes/"
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
