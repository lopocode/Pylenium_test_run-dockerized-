from selenium.webdriver.common.keys import Keys


def test_google_search(py):
    py.visit('http://google.com')
    py.get('[name="q"]').type('puppies', Keys.ENTER)
    assert py.should().contain_title('puppies')
