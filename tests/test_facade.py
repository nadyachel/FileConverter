import os
from converter.facade import BatchConverterFacade

def test_batch_converter_success(tmp_path):
    # Arrange
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    
    # Создаем 2 тестовых CSV файла
    (input_dir / "file1.csv").write_text("id,val\n1,A", encoding="utf-8")
    (input_dir / "file2.csv").write_text("id,val\n2,B", encoding="utf-8")
    # Создаем один неподдерживаемый файл (негативный кейс внутри пакета)
    (input_dir / "file3.txt").write_text("hello", encoding="utf-8")

    facade = BatchConverterFacade(str(input_dir), str(output_dir))

    # Act
    facade.convert_batch('.json')

    # Assert
    assert os.path.exists(output_dir)
    # Должно сконвертироваться только 2 файла
    converted_files = os.listdir(output_dir)
    assert len(converted_files) == 2
    assert "file1.json" in converted_files
    assert "file2.json" in converted_files