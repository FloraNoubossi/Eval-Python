# Utiliser une image de base NGINX
FROM nginx:alpine

# Copier le fichier de configuration NGINX
COPY nginx.conf /etc/nginx/nginx.conf

# Copier les certificats SSL
COPY ssl/nginx.crt /etc/nginx/ssl/nginx.crt
COPY ssl/nginx.key /etc/nginx/ssl/nginx.key

# Exposer le port 443
EXPOSE 443

