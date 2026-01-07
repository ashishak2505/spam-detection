# 1. Use lightweight Python image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements first (for caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy rest of the code
COPY . .

# 6. Expose Streamlit port
EXPOSE 8501

# 7. Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
