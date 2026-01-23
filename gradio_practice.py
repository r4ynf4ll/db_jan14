import gradio as gr


def f(x):
    return x**2

# making interface
iface = gr.Interface(fn = f,inputs="number",outputs="number")

iface.launch()
