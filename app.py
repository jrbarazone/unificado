from flask import Flask, request, render_template
import scripts.data_storage as ds
import scripts.image_processing as ip
import scripts.seo_optimization as seo
import scripts.marketplace_integration as mi
import scripts.inventory_management as im

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.form
    file = request.files['file']
    file_path = f'static/uploads/{file.filename}'
    file.save(file_path)

    barcode = data['barcode']
    quantity = data['quantity']

    # Procesar la imagen
    processed_image_path = ip.remove_background(file_path)
    
    # Subir la imagen a la nube (implementación ficticia)
    image_url = mi.upload_to_cloud(processed_image_path)
    
    # Generar descripción y título SEO
    description, title = seo.generate_seo_description(image_url)
    
    # Guardar los datos en la hoja de cálculo
    ds.save_to_sheet(barcode, image_url, quantity, description, title)
    
    # Publicar en marketplaces
    mi.publish_product(barcode, image_url, quantity, description, title)
    
    return 'Producto subido y procesado con éxito'

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
