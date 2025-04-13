from PIL import Image
import torch
import torch.nn.functional as F
from torchvision import transforms

# 🔁 Same transform used during training
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

# 🏷️ Class labels (match your training order!)
class_names = ["Real", "Altered-Easy", "Altered-Medium", "Altered-Hard"]

def predict_jpg_image(image_path):
    image = Image.open(image_path).convert("L")
    image = transform(image).unsqueeze(0).to(DEVICE)

    model.eval()
    with torch.no_grad():
        output = model(image)
        probs = F.softmax(output, dim=1)
        pred_idx = torch.argmax(probs, dim=1).item()
        predicted_class = class_names[pred_idx]

        print(f"\n🖼️ Image: {image_path}")
        print(f"🔍 Probabilities: {probs.cpu().numpy()}")
        print(f"✅ Predicted Class: {predicted_class}")
