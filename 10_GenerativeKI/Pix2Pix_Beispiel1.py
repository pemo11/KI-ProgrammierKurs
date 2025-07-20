#! usr/bin/python3
# -*- coding: utf-8 -*-
# filsoe: Pix2Pix_Beispiel1.py

from PIL import Image
import requests
import torch
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler
from os import path
model_id = "timbrooks/instruct-pix2pix"
pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float16, safety_checker=None)
# pipe.to("mps")
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

imgPath = path.join(path.dirname(__file__), "images", "Emden04.jpg")
image = Image.open(imgPath)
# Resize, can try varying sizes also
image = image.resize((768, 768)) 
prompt = "A fireworks to the sky, in the style of a painting by Claude Monet, with vibrant colors and soft brush strokes."
images = pipe(prompt, image=image, num_inference_steps=10, image_guidance_scale=1).images
images[0].show()
pngPath = path.join(path.dirname(__file__), "images", "Emden04_MonetStyle.png")
images[0].save(pngPath, "PNG")