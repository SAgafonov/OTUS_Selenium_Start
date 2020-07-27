FROM python:3.6

WORKDIR /home/app

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD ["pytest", "--url=http://192.168.0.105/", "--remote_type=selenoid", "tests/admin_part/test_admin_auth_zone.py::TestAuthorization"]