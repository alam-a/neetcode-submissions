class Singleton:
    _instance, _initialized = None, None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not self._initialized:
            self._initialized = True
            self.value = None

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value