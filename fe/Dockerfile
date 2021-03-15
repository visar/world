FROM node:15.11 as builder
ENV REACT_APP_API_URL="http://localhost:8080/"
WORKDIR /app
ADD . /app
RUN npm install
RUN npm run build

FROM node:15.11-slim
COPY --from=builder /app/build /app/build
WORKDIR /app
RUN npm install -g serve
EXPOSE 5000
ENTRYPOINT ["serve", "-s", "build"]
