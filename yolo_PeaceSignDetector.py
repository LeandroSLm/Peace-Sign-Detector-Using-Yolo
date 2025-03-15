from ultralytics import YOLO
import os
dirname = os.path.dirname(__file__)
config = os.path.join(dirname, 'config.yaml')
# Load a model
# model = YOLO("yolo11n.pt") Modelo Padrão do yolo
model = YOLO("C:\\Users\leand\OneDrive\Área de Trabalho\\15_03_2025\\Peace-Sign-Detector-Using-Yolo\\runs\\detect\\train\\weights\\best.pt")  # Modelo Treinado com o Peace-Sign
# Train the model
'''
train_results = model.train(
    data="config.yaml",  # path to dataset YAML
    epochs=200,  # number of training epochs
    imgsz=640,  # training image size
    device="cpu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)
'''
#Eval
#results = model.val(data=config)
