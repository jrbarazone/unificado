import openai

def generate_seo_description(image_url):
    # Ejemplo de implementación ficticia utilizando OpenAI API
    openai.api_key = 'your-api-key'
    
    response = openai.Image.create_description(image_url=image_url)
    description = response['description']
    title = response['title']
    return description, title
