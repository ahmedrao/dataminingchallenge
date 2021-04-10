FROM python:3
WORKDIR /code
COPY zalora_scraping.py ./
RUN pip install requests
CMD ["python3","./zalora_scraping.py"]