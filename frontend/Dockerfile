FROM node:18-alpine

WORKDIR /app

ENV NODE_ENV=development

COPY package*.json ./
RUN npm ci

COPY . .

RUN npm run build || true

EXPOSE 3000

CMD ["npm", "run", "dev"]
