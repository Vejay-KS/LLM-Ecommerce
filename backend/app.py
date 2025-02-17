from flask import Flask, jsonify, send_from_directory
from . import database
from . import llmGemini

app = Flask(__name__, static_folder="../frontend", static_url_path="/")

def get_data_for_plants():
    plants_data = []
    data_db = database.get_data_from_db()
    for row in data_db:
        row_data = {
            'plant_name': row[0],
            'plant_quantity_in_stock': row[1],
            'plant_base_selling_price': row[2],
            'plant_minimum_selling_price': row[3],
            'plant_discounted_selling_price': row[4],
            'plant_discount_percentage': row[5],
            'plant_type_airpurifier': row[6],
            'plant_type_balcony': row[7],
            'plant_type_bonsai': row[8],
            'plant_type_cactus': row[9],
            'plant_type_creeper': row[10],
            'plant_type_succulent': row[11],
            'plant_type_tabletop': row[12],
            'plant_type_medicinal': row[13],
            'plant_type_ornamental': row[14],
            'plant_total_sold': row[15],
        }
        row_data['plant_description'] = llmGemini.get_response_from_llm(row_data)
        plants_data.append(row_data)
    return plants_data

@app.route('/api/datadbllm', methods=['GET'])
def fetch_datadbllm():
    data = get_data_for_plants()
    return jsonify(data)

@app.route('/api/datadb', methods=['GET'])
def fetch_datadb():
    data = database.get_data_from_db()
    return jsonify(data)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)