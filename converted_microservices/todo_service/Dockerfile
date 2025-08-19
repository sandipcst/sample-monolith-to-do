FROM registry.access.redhat.com/ubi8/python-39
USER 1001
COPY . ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
ENV FLASK_APP=todo_service.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
