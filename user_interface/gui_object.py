class GUIObject:
    all_uis = []
    def __init__(self, **kwargs):
        self.surface = None

        # keyword arguments
        for kw in kwargs:
            if hasattr(self, kw):
                setattr(self, kw, kwargs[kw])

        # inserting into list
        GUIObject.all_uis.append(self)

    def render_ui(self):
        pass