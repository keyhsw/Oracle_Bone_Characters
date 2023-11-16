import gradio as gr
from XEdu.hub import Workflow as wf
model = wf(task='MMEdu',checkpoint='model/Oracle.onnx')

def predict(input_img):
    # result = model.inference(data=input_img) 
    # result = model.format_output(lang="zh")
    return input_img,result

demo = gr.Interface(fn=predict,  inputs=gr.Image(shape=(128, 128),source="canvas"), outputs=["image","text"])
demo.launch(share=True)
