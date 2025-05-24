from matplotlib import pyplot as plt
import streamlit as st
import numpy as np
from scipy.stats import norm

st.markdown("# Call option Greeks")

def create_chart(x, y_1, name,min_y, max_y):
    fig, ax = plt.subplots()
    ax.plot(x, y_1, label=name, color="darkblue")
    ax.axvline(x=100, color='grey', linestyle='--')
    ax.set_xlabel("Stock price")
    #ax.set_ylabel("Value")
    #ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), frameon=False)
    ax.set_xlim([0, 170])
    ax.set_ylim([min_y, max_y])
    ax.title.set_text(name)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().tick_params(axis='both', which='both', length=0)
    plt.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.7)
    st.pyplot(fig)

def create_charts(x, y_1, y_2):
    fig, ax = plt.subplots()
    ax.plot(x, y_1, label="Intrinsic value", color="lightcoral")
    ax.plot(x, y_2, label="Black-Scholes price", color="darkblue")
    ax.axvline(x=100, color='grey', linestyle='--')
    ax.set_xlabel("Stock price")
    #ax.set_ylabel("Value")
    #ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), frameon=False)
    ax.title.set_text("Black-Scholes price")
    ax.set_xlim([0, 170])
    ax.set_ylim([-10, 100])
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().tick_params(axis='both', which='both', length=0)
    plt.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.7)
    st.pyplot(fig)


# Black-Scholes formula for a call option
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

def delta(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    nd1 = norm.cdf(d1)
    return nd1

def gamma(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    gamma_value = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    return gamma_value

def theta(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    theta_value = -(1/2) * sigma * S * norm.pdf(d1) / np.sqrt(T) - r * K * np.exp(-r * T) * norm.cdf(d2)
    return theta_value

def vega(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    vega_value = S * sigma * np.sqrt(T) * norm.pdf(d1)
    return vega_value

# Parameters
K = 100  # Strike price
r = 0.05  # Risk-free rate
#sigma = 0.5  # Volatility

# Generate stock prices
S = np.linspace(0, 200, 500)

# Add volatility input
#with col1:
    #sigma = st.slider("Volatility (σ)", 0.05, 0.9, 0.2, 0.01)
sigma = st.slider("Volatility (σ)", 0.05, 0.8, 0.2, 0.01)
t = st.slider("Time", 0.0, 1.0, 0.2, 0.01)

# Calculate Greeks
payoff = np.maximum(S - K, 0)
bs_prices = black_scholes_call(S, K, 1-t, r, sigma)
delta_values = delta(S, K, 1-t, r, sigma)
gamma_values = gamma(S, K, 1-t, r, sigma)
theta_values = theta(S, K, 1-t, r, sigma)
vega_values = vega(S, K, 1-t, r, sigma)

# Create two columns
col1, col2, col3 = st.columns([1, 1, 1]) 

# Plot the results
with col1:
    create_charts(S, payoff, bs_prices)
    create_chart(S, theta_values, "Theta", -80, 10)
with col2:
    create_chart(S, delta_values, "Delta", 0, 1)
    create_chart(S, vega_values, "Vega", 0, 20)
with col3:
    create_chart(S, gamma_values, "Gamma", 0, 0.125)
