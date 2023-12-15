FROM node

WORKDIR /client

COPY package.json .

RUN npm ci

COPY . .

CMD ["npm", "run", "dev"]
