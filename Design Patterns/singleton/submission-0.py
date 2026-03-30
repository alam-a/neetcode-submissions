class Singleton:
    _instance = None
    _initialized = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if not self._initialized:
            self.value = None
            self._initialized = True

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value