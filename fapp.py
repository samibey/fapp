import gradio as gr
from fastapi import FastAPI

def greet(text: str) -> str:
    return text

demo = gr.Interface(
    fn=greet,
    inputs=gr.components.Textbox(label='Input'),
    outputs=gr.components.Textbox(label='Output'),
    allow_flagging='never'
)

app = FastAPI()

@app.get('/')
async def root():
    return 'Gradio app is running at /gradio', 200

app = gr.mount_gradio_app(app, demo, path='/gradio')