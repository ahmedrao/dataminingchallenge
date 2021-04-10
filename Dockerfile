FROM python:3
WORKDIR /code
COPY zalora_scraping.py ./code
RUN pip install requests
CMD ["python3","./code/zalora_scraping.py"]