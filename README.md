# 📈 Stock Price Forecasting App with ARIMA

This is an interactive Streamlit web app that allows users to view historical stock prices and forecast future values using the ARIMA model. The data is fetched live from Yahoo Finance.

---

## 👨‍💻 Creator

**John Christopher**  
🗓️ July 2025  
📍 Built as my first data science portfolio project using Streamlit.

---

## 🚀 Features

- 📅 Choose your own start and end dates  
- 💼 Works with any stock ticker (e.g., AAPL, TSLA, INFY)  
- 📉 Visualize stock closing price charts  
- 📊 See the full historical data table  
- ⚠️ Displays error messages for invalid symbols  
- 🔮 Forecast future stock prices using ARIMA  
- 📷 Includes screenshots of the full app workflow  

---

## 🧠 Technologies Used

- **Python**  
- **Streamlit**  
- **YFinance**  
- **Pandas**  
- **Matplotlib**  
- **Statsmodels** (for ARIMA forecasting)  

---

## 🖼️ App Screenshots

| #  | Description                      | Click to View                      |
|:--:|----------------------------------|------------------------------------|
| 1  | Homepage with title & sidebar    | [![1](screenshots/1_home_with_name_and_sidebar.png)](screenshots/1_home_with_name_and_sidebar.png) |
| 2  | Chart view after entering AAPL   | [![2](screenshots/2_chart_view.png)](screenshots/2_chart_view.png) |
| 3  | Table view of stock data         | [![3](screenshots/3_table_view.png)](screenshots/3_table_view.png) |
| 4  | Error message for wrong symbol   | [![4](screenshots/4_error_message_handling.png)](screenshots/4_error_message_handling.png) |
| 5  | ARIMA input UI                   | [![5](screenshots/5_arima_input_ui.png)](screenshots/5_arima_input_ui.png) |
| 6  | ARIMA forecast days selection    | [![6](screenshots/6_arima_days_selection.png)](screenshots/6_arima_days_selection.png) |
| 7  | ARIMA original data chart        | [![7](screenshots/7_arima_original_chart.png)](screenshots/7_arima_original_chart.png) |
| 8  | ARIMA original data table        | [![8](screenshots/8_arima_original_table.png)](screenshots/8_arima_original_table.png) |
| 9  | ARIMA forecast chart             | [![9](screenshots/9_arima_forecast_chart.png)](screenshots/9_arima_forecast_chart.png) |
| 10 | ARIMA forecasted data table      | [![10](screenshots/10_arima_forecast_table.png)](screenshots/10_arima_forecast_table.png) |

🖼️ All images are located in the `screenshots/` folder.

---

## 🏁 How to Run This App Locally

### 📂 1. Clone the repository (or download the ZIP)

```bash
git clone https://github.com/yourusername/stock-price-forecasting-arima.git
cd stock-price-forecasting-arima
```

### 🐍 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
# source venv/bin/activate  # On Mac/Linux
```

### 📦 3. Install the required packages

```bash
pip install -r requirements.txt
```

### ▶️ 4. Run the Streamlit app

```bash
streamlit run app.py
```

After running the above command, open your browser and visit:  
🔗 [http://localhost:8501](http://localhost:8501)  
This will open the interactive stock forecasting app on your local machine.

---

🌟 Thanks for checking out my project! Feel free to use, or star it 💫
