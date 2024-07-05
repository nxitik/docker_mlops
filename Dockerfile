FROM python:3.12.4-slim
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python model_deploy_to_flask/flask_02.py