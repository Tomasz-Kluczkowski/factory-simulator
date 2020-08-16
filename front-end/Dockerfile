FROM node:12.18.3-alpine AS builder
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build --prod

FROM nginx:1.17.1-alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /usr/src/app/dist/front-end/ /usr/share/nginx/html
