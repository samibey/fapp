import gradio as gr
from fastapi import FastAPI

def echo(text: str) -> str:
    return text

iface = gr.Interface(
    fn=echo,
    inputs=gr.components.Textbox(label='Input'),
    outputs=gr.components.Textbox(label='Output'),
    allow_flagging='never'
)

app = FastAPI()

@app.get('/')
async def root():
    return 'Gradio app is running at /gradio', 200

app = gr.mount_gradio_app(app, iface, path='/gradio')