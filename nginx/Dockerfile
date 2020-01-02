# production stage
FROM nginx:stable-alpine as production-stage

WORKDIR /usr/share/nginx/html

COPY ./vuejs/ .
COPY ./static/ ./static/

WORKDIR /etc/nginx/conf.d/

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf default.conf
#COPY backend.conf backend.conf

# EXPOSE 8000
EXPOSE 8080
EXPOSE 8877
CMD ["nginx", "-g", "daemon off;"]