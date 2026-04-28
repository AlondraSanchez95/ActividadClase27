#Construccion
FROM alpine:latest AS builder
RUN apk add --no-cache curl
WORKDIR /app
COPY ./src .
#Produccion
FROM nginx:alpine
LABEL maintainer="Alondra Sanchez"
LABEL version="1.0"
COPY --from=builder /app /usr/share/nginx/html
EXPOSE 80
