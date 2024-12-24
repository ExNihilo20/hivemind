from datetime import datetime

class Hive:
    id = 0
    def __init__(self, id:int, health_level:str, type:str = "Langstroth", last_inspected:datetime = datetime(1900,1,1)):
        self._id += 1
        self._name = f"Hive {self._id}"
        self._type = type
        self._health_level = health_level
        self._last_inspected = last_inspected
        self._has_queen = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self.name = name
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, new_type):
        self._type = new_type

    @property
    def health_level(self):
        return self._health_level
    
    @health_level.setter
    def health_level(self, new_level):
        valid_health_levels = ["Healthy", "Moderate", "Unhealthy"]
        if new_level not in valid_health_levels:
            raise ValueError("Health Level must be 'Healthy', 'Moderate', or 'Unhealthy'")
    
    @property
    def last_inspected(self):
        return self._last_inspected

    @last_inspected.setter
    def last_inspected(self, new_inspection_date:datetime):
        if new_inspection_date < self._last_inspected:
            raise ValueError("New inspection date must be in the future")
        

    def __str__(self):
        return f"{self._name}, last inspected: {self._last_inspected}, health level {self._health_level}"
