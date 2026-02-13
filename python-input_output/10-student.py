class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire
        des attributs sélectionnés de l'étudiant.
        
        Args:
            attrs (list, optional): liste
            d'attributs à inclure. Si None,
            retourne tous les attributs.
        """
        obj = self.__dict__.copy()
        if attrs is None:
            return obj

        if type(attrs) is list and all(isinstance(a, str) for a in attrs):
            return {key: obj[key] for key in attrs if key in obj}
        return obj