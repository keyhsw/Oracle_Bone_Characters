import gradio as gr
from XEdu.hub import Workflow as wf
model = wf(task='MMEdu',checkpoint='Oracle.onnx')
classes = ['人','大'] # 指定中文类别名称

def predict(input_img):  
    result = model.inference(data=input_img) 
    result = model.format_output(lang="zh")
    result_text = "预测结果是：" + classes[result['标签']] # 输出中文推理结果
    return input_img,result_text

demo = gr.Interface(fn=predict,  inputs=gr.Image(shape=(128, 128),source="canvas"), outputs=["image","text"])
demo.launch(share=True)

