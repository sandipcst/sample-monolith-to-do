FROM registry.access.redhat.com/ubi8/python-39
USER 1001
COPY . ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
CMD ["python", "user_service.py"]
