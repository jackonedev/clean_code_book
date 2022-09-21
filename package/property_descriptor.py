"""
Do not implement a descriptor unless there is actual evidence of
the repetition we are trying to solve, and the complexity is proven
to have paid off.
"""

class HistoryTracedAttribute:
    def __init__(self, trace_attribute_name: str) -> None:
        self.trace_attribute_name = trace_attribute_name
        self._name = None

    def __set_name__(self, objtype, name):
        self._name = name

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return obj.__dict__[self._name]

    def __set__(self, obj, value):
        self._track_change_in_value_for_instance(obj, value)
        obj.__dict__[self._name] = value

    def _track_change_in_value_for_instance(self, obj, value):
        self._set_default(obj)
        if self._needs_to_track_change(obj, value):
            obj.__dict__[self.trace_attribute_name].append(value)

    def _needs_to_track_change(self, obj, value) -> bool:
        try:
            current_value = obj.__dict__[self._name]
        except KeyError:
            return True
        return value != current_value

    def _set_default(self, obj):
        obj.__dict__.setdefault(self.trace_attribute_name, [])
