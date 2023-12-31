import constants
from openai import OpenAI
import os
import utilities

client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY') 

def chat(prompt, system_prompt):
    response = client.chat.completions.create(
        model=constants.GPT_MODEL,
        messages=
        [
            {
                "role" : "system", 
                "content": system_prompt
            },
            {
                "role" : "user", 
                "content" : prompt
            }
        ]
    )

    return response.choices[0].message.content

def look(prompt, image_path):
    image_response = client.chat.completions.create(
    model=constants.GPT_VISION_MODEL,
    messages = 
    [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", "text": prompt
                },
                {
                    "type": "image", "image_url": 
                                    {
                                        "url": f"data:image/jpeg;base64,{utilities.encode_image(image_path)}"
                                    }
                }
            ]
        }
    ],
    max_tokens=500
    )
    return image_response.choices[0].message.content