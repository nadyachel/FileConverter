import os
import json
from PIL import Image
from converter.strategies import ImageConverter, CsvToJsonConverter

def test_image_converter(tmp_path):
    # Arrange (используем встроенную фикстуру tmp_path для временных файлов)
    converter = ImageConverter()
    input_image_path = tmp_path / "test.png"
    output_image_path = tmp_path / "test.jpg"
    
    # Создаем тестовую картинку 10x10 пикселей
    img = Image.new('RGB', (10, 10), color = 'red')
    img.save(input_image_path)

    # Act
    converter.convert(str(input_image_path), str(output_image_path), quality=80)

    # Assert
    assert os.path.exists(output_image_path)
    with Image.open(output_image_path) as result_img:
        assert result_img.format == 'JPEG'

def test_csv_to_json_converter(tmp_path):
    # Arrange
    converter = CsvToJsonConverter()
    input_csv = tmp_path / "data.csv"
    output_json = tmp_path / "data.json"
    
    input_csv.write_text("name,age\nAlice,20\nBob,25", encoding="utf-8")

    # Act
    converter.convert(str(input_csv), str(output_json))

    # Assert
    assert os.path.exists(output_json)
    with open(output_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) == 2
        assert data[0]['name'] == 'Alice'