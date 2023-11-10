FROM Python3.8
COPY ./ /ernav2/
RUN apt-get -y update && apt-get iputil-ping
RUN pip install -r requirements.txt