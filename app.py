import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from pmdarima.arima import auto_arima
from datetime import datetime

# App config
st.set_page_config(page_title="Stock Price Predictor", layout="wide", initial_sidebar_state="expanded")

# App title and author info
st.title("📈 Stock Price Viewer + ARIMA Forecast - By John Christopher")
st.markdown("👤 Created by **John Christopher** | 📅 July 2025")
st.sidebar.markdown("👤 **Made by John Christopher**")

# User inputs
ticker = st.text_input("Enter stock symbol (e.g., AAPL, TSLA, INFY):", value="AAPL")
start_date = st.date_input("Start date", pd.to_datetime("2022-01-01"))
end_date = st.date_input("End date", pd.to_datetime("today"))
forecast_period = st.slider("Select days to forecast into future", 7, 60, step=1)

# Get Data button
if st.button("Get Data"):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)

        if data.empty:
            st.warning("⚠️ No data found. Try a different stock symbol or date range.")
        else:
            st.success(f"✅ Showing data for {ticker.upper()}")

            # Plot closing prices
            st.subheader("📉 Closing Price Chart")
            st.line_chart(data['Close'])

            # Show preview table
            st.subheader("📊 Data Preview")
            st.dataframe(data.tail())

            # ARIMA Forecasting
            st.subheader("🔮 ARIMA Forecast")

            close_prices = data['Close'].dropna()
            model = auto_arima(close_prices, seasonal=False, suppress_warnings=True)
            forecast = model.predict(n_periods=forecast_period)

            last_date = data.index[-1]
            future_dates = [last_date + timedelta(days=i+1) for i in range(forecast_period)]
            forecast_df = pd.DataFrame({'Date': future_dates, 'Forecasted Close': forecast})
            forecast_df.set_index('Date', inplace=True)

            # Plot both actual and forecast
            fig, ax = plt.subplots(figsize=(10, 4))
            close_prices.plot(ax=ax, label="Historical")
            forecast_df['Forecasted Close'].plot(ax=ax, label="Forecast", linestyle="--")
            ax.set_title(f"{ticker.upper()} Stock Price Forecast ({forecast_period} days)")
            ax.legend()
            st.pyplot(fig)

            # Show forecast table
            st.subheader("📄 Forecasted Values")
            st.dataframe(forecast_df)

    except Exception as e:
        st.error(f"❌ Something went wrong: {e}")
