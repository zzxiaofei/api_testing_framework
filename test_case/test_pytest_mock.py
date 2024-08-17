import pytest
from common.weatherService import WeatherService


def test_get_current_weather(mocker):
    # 设置 mock 对象
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "current": {
            "temp_c": 25,
            "condition": {
                "text": "Sunny"
            }
        }
    }

    # 使用 mocker.patch 来 mock requests.get
    mocker.patch('weather.service.requests.get', return_value=mock_response)

    # 创建 WeatherService 实例
    weather_service = WeatherService("fake_api_key")

    # 调用方法
    result = weather_service.get_current_weather("Sydney")

    # 验证结果
    assert result == {"temperature": 25, "condition": "Sunny"}

    # 验证 requests.get 被正确调用
    weather_service.requests.get.assert_called_once_with(
        "http://api.weatherapi.com/v1/current.json?key=fake_api_key&q=Sydney"
    )


def test_get_current_weather_error(mocker):
    # 设置 mock 对象，模拟错误响应
    mock_response = mocker.Mock()
    mock_response.status_code = 404

    # 使用 mocker.patch 来 mock requests.get
    mocker.patch('weather.service.requests.get', return_value=mock_response)

    # 创建 WeatherService 实例
    weather_service = WeatherService("fake_api_key")

    # 验证异常被正确抛出
    with pytest.raises(Exception, match="Failed to get weather data"):
        weather_service.get_current_weather("NonexistentCity")

    # 验证 requests.get 被正确调用
    weather_service.requests.get.assert_called_once_with(
        "http://api.weatherapi.com/v1/current.json?key=fake_api_key&q=NonexistentCity"
    )

if __name__ == '__main__':
    pytest.main()