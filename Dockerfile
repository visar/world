FROM python:3.7 AS builder
WORKDIR /app
COPY . /app
RUN python setup.py bdist_wheel

FROM python:3.7-slim
ENV VERSION 0.0.3
WORKDIR /app
COPY --from=builder /app/dist/app-${VERSION}-py3-none-any.whl .
RUN pip install app-${VERSION}-py3-none-any.whl
RUN pip install gunicorn
EXPOSE 8000
CMD ["/usr/local/bin/gunicorn", "app:create_app()", "-b", "0.0.0.0:8000"]
