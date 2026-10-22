# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Leting Liu")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 3 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "* Fun Tab"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

# Tab 4: A Circle
with tabs[3]:
    st.subheader(f"Somethhing New")
    import turtle

    # Set up the screen and turtle object
    screen = turtle.Screen()
    pen = turtle.Turtle()

    # Optional: Customize the appearance
    pen.color("blue")
    pen.pensize(3)

    # Draw a circle with a radius of 100 pixels
    pen.circle(100)

    # Keep the window open until you click on it
    screen.exitonclick()

