FROM python:latest

RUN pip install flask
RUN pip install LiPD

COPY climateModel.py /
COPY static/ /

EXPOSE 80
CMD python /climateModel.py