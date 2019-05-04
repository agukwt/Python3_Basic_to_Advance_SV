def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')