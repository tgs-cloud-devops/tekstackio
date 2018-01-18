FROM node:5.11.0-slim

WORKDIR /app

RUN npm install -g nodemon
RUN npm install applicationinsights --save
ADD package.json /app/package.json
RUN npm config set registry http://registry.npmjs.org

RUN cd $(npm root -g)/npm && npm install fs-extra && sed -i -e s/graceful-fs/fs-extra/ -e s/fs.rename/fs.move/ ./lib/utils/rename.js

RUN npm install && npm ls
RUN mv /app/node_modules /node_modules

ADD . /app

ENV PORT 80
EXPOSE 80

CMD ["node", "server.js"]
