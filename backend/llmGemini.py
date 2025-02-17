from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def get_response_from_llm(plant_details):
    prompt = f"""  
    Write a compelling e-commerce product description for INDOOR plants with:  

    **Name:** {plant_details['plant_name']}
    **Quantity in Stock:** {plant_details['plant_quantity_in_stock']}
    **Base Selling Price:** {plant_details['plant_base_selling_price']}
    **Minimum Selling Price:** {plant_details['plant_minimum_selling_price']}
    **Discounted Selling Price:** {plant_details['plant_discounted_selling_price']}
    **Discount Percentage:** {plant_details['plant_discount_percentage']}
    **Is the plant type airpurifier?:** {plant_details['plant_type_airpurifier']}
    **Is the plant type balcony:** {plant_details['plant_type_balcony']}
    **Is the plant type bonsai:** {plant_details['plant_type_bonsai']}
    **Is the plant type cactus:** {plant_details['plant_type_cactus']}
    **Is the plant type creeper:** {plant_details['plant_type_creeper']}
    **Is the plant type succulent:** {plant_details['plant_type_succulent']}
    **Is the plant type tabletop:** {plant_details['plant_type_tabletop']}
    **Is the plant type medicinal:** {plant_details['plant_type_medicinal']}
    **Is the plant type ornamental:** {plant_details['plant_type_ornamental']}
    **Total plants sold:** {plant_details['plant_total_sold']}

    Make it engaging, persuasive, and SEO-friendly but between 280 and 300 words. 
    """  

    client = genai.Client(api_key=os.environ.get('APIKEY_LLM_GEMINI'))
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.candidates[0].content.parts[0].text
