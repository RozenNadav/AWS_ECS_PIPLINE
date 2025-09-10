FROM python:3.11-slim

WORKDIR /app

# העתקת requirements והתקנת dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת שאר הקוד
COPY app/ .

EXPOSE 80

CMD ["python", "app.py"]