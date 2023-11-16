import gradio as gr

def predict(input_img):
    # result = model.inference(data=input_img) 
    # result = model.format_output(lang="zh")
    return input_img,None

demo = gr.Interface(fn=predict,  inputs=gr.Image(shape=(128, 128),source="canvas"), outputs=["image","text"])
if __name__ == "__main__":
    demo.launch()
