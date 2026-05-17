import pytest
from converter.factory import ConverterFactory
from converter.strategies import ImageConverter, CsvToJsonConverter

def test_factory_returns_image_converter():
    # Arrange
    input_ext = '.png'
    output_ext = '.jpg'

    # Act
    converter = ConverterFactory.get_converter(input_ext, output_ext)

    # Assert
    assert isinstance(converter, ImageConverter)

def test_factory_returns_csv_converter():
    # Arrange
    input_ext = '.csv'
    output_ext = '.json'

    # Act
    converter = ConverterFactory.get_converter(input_ext, output_ext)

    # Assert
    assert isinstance(converter, CsvToJsonConverter)

def test_factory_unsupported_format_raises_error(): # Негативный сценарий
    # Arrange
    input_ext = '.pdf'
    output_ext = '.docx'

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        ConverterFactory.get_converter(input_ext, output_ext)
    assert "не поддерживается" in str(exc_info.value)