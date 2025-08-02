import seaborn as sns
import matplotlib.pyplot as plt

def plot_trend(df, column, state_name, label, show_plot=False):
    fig, ax = plt.subplots(figsize=(10, 4))
    
    if column not in df.columns:
        print(f"❌ Column '{column}' not found in DataFrame for {state_name}. Available columns: {df.columns.tolist()}")
        return None

    sns.lineplot(data=df, x="date", y=column, ax=ax)
    ax.set_title(f"{label} Trend in {state_name}")
    ax.set_xlabel("Date")
    ax.set_ylabel(label)
    ax.grid(True)
    plt.tight_layout()
    
    if show_plot:  # for main.py use
        plt.show()

    return fig  # for app.py (Streamlit)
