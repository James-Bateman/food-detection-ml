import torch
from PIL import Image
import torchvision.transforms as transforms

import torchvision.models as models

import urllib.request

# Load ImageNet class labels
LABELS_URL = 'https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt'
response = urllib.request.urlopen(LABELS_URL)
IMAGENET_LABELS = [line.strip() for line in response.read().decode('utf-8').split('\n')]

model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

def predict_image(image: Image.Image):
    if isinstance(image, torch.Tensor):
        image = transforms.ToPILImage()(image)
    image = transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        outputs = model(image)
    _, predicted = outputs.max(1)
    return IMAGENET_LABELS[predicted.item()]
