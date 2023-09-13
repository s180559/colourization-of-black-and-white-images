import os
os.system("hub install deoldify==1.0.1")
import gradio as gr
import paddlehub as hub
from pathlib import Path
from datetime import datetime

model = hub.Module(name='deoldify')
# NOTE:  Max is 45 with 11GB video cards. 35 is a good default
render_factor=35


def colorize_image(image):
    # now = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    if not os.path.exists("./output"):
        os.makedirs("./output")
    # if image is not None:
    #     image.save(f"./output/{now}-input.jpg")    
    model.predict(image.name)
    return './output/DeOldify/'+Path(image.name).stem+".png"


def create_interface():
    with gr.Blocks() as enhancer:
        gr.Markdown("Colorize old black & white photos")
        with gr.Column(scale=1, label = "Colorize photo", visible=True) as colorize_column:
            colorize_input = gr.Image(type="file")
            colorize_button = gr.Button("Colorize!")
            colorize_output = gr.Image(type="file")
            download_colorize_button = gr.outputs.File(label="Download colorized image!")
            colorize_button.click(colorize_image, inputs=colorize_input, outputs=colorize_output)
    enhancer.launch()

def run_code():
    create_interface()

# The main function
run_code()