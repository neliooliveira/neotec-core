FROM node:18-alpine

WORKDIR /app

ENV NODE_ENV=development

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build 2>/dev/null || true

EXPOSE 3000

CMD ["npm", "run", "dev"]
