import gradio as gr
import sqlite3
import pandas as pd

def fetch():
    conn = sqlite3.connect('points.db')
    cursor = conn.cursor()
    query = """
        SELECT *
        FROM points;
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    records_df = pd.DataFrame(records,columns=['id','x','y'])
    return records_df

# making interface
iface = gr.Interface(fn = fetch(),inputs=[],outputs=gr.Dataframe(headers=['id','x','y']))

iface.launch()
