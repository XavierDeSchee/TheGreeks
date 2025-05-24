from matplotlib import pyplot as plt
import streamlit as st
import numpy as np
from scipy.stats import norm

st.markdown("# Black-Scholes call option price")

def create_charts(x, y_1, y_2):
    fig, ax = plt.subplots()
    ax.plot(x, y_1, label="Intrinsic value", color="lightcoral")
    ax.plot(x, y_2, label="Black-Scholes price", color="darkblue")
    #ax.axvline(x=100, color='lightgrey', linestyle='--', label=f"t = {t}")
    ax.set_xlabel("Stock price")
    #ax.set_ylabel("Value")
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), frameon=False)
    ax.set_xlim([0, 170])
    ax.set_ylim([-10, 100])
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().tick_params(axis='both', which='both', length=0)
    plt.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.7)
    st.pyplot(fig)
# Create two columns: one for the slider and one for the chart

#col1, col2 = st.columns([1, 3]) 

# Black-Scholes formula for a call option
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

# Parameters
K = 100  # Strike price
r = 0.05  # Risk-free rate
#sigma = 0.5  # Volatility

# Generate stock prices
S = np.linspace(0, 200, 500)

# Add volatility input
#with col1:
    #sigma = st.slider("Volatility (σ)", 0.05, 0.9, 0.2, 0.01)
t = st.slider("Time", 0.0, 1.0, 0.2, 0.01)
sigma = st.slider("Volatility (σ)", 0.05, 0.8, 0.2, 0.01)


# Calculate payoff and Black-Scholes price
payoff = np.maximum(S - K, 0)
bs_prices = black_scholes_call(S, K, 1-t, r, sigma)

# Plot the results
#with col2:
    #st.line_chart({"Payoff": payoff, "Black-Scholes Price": bs_prices})

create_charts(S, payoff, bs_prices)