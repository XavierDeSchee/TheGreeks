import streamlit as st
import numpy as np
import matplotlib.pyplot as plt



def create_chart(t, i, w):
    fig, ax = plt.subplots()
    ax.plot(np.linspace(0, t, i), w, label="Brownian Motion")
    ax.axvline(x=t, color='grey', linestyle='--', label=f"t = {t}")
    ax.fill_between(np.linspace(0, t, i), w, color='lightblue', alpha=0.5)
    ax.set_xlim([0, 1])
    ax.set_ylim([-3, 3])
    ax.set_xlabel("Time")
    ax.set_ylabel("W(t)")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().tick_params(axis='both', which='both', length=0)
    plt.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.7)
    #plt.style.use('dark_background')
    st.pyplot(fig)