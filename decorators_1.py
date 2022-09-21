# Decorators in classes
# pag-183-.pdf
# Event system, for monitoring the platform. We need to transform data for each event and send it to an external system.
# Each type of Event might have some particularities when selecting how to send its data.
# In particular the Event for a Login might contain sensitive information such as credentials.
# Also timestamp require some transformation to show them in a particular format.

# 1. wrong:
#    - as the number of event grows, also will do the serialization classes (Mapped one to one).
#    - It's not flexible enought. Hard to reuse parts of it.
#    - Boilerplate. serialize() could be an extra class and work as a mixin. It's not a good use of inheritance, so serialize() will have to be present in all event classes.
from dataclasses import dataclass
from datetime import datetime


class LoginEventSerializer:
    def __init__(self, event):
        self.event = event

    def serialize(self) -> dict:
        return {
            "username": self.event.username,
            "password": "**redacted**",
            "ip": self.event.ip,
            "timestamp": self.event.timestamp.strfime("%d-%m-%Y %H:%M"),
        }


@dataclass
class LoginEvent:
    SERIALIZER = LoginEventSerializer

    username: str
    password: str
    ip: str
    timestamp: datetime

    def serialize(self) -> dict:
        return self.SERIALIZER(self).serialize()


# 2. Dynamically construct an object that, given a set of fiters and an event instance, can serialize it by applying the filters to its fields.
# getattr: https://stackoverflow.com/questions/4075190/what-is-getattr-exactly-and-how-do-i-use-it
from dataclasses import dataclass
from package.logger import buildLogger

logger, msg = buildLogger("decorator_1")


def hide_field(field) -> str:
    logger.info(msg.set("Funcion: hide_field"))
    return "**redacted**"


def format_time(field_timestamp: datetime) -> str:
    logger.info(msg.set("Funcion: format_time"))
    return field_timestamp.strftime("%d-%m-%Y %H:%M")


def show_original(event_field):
    logger.info(msg.set("Funcion: show_original"))
    return event_field


class EventSerializer:
    def __init__(self, serialization_fields: dict) -> None:
        logger.info(msg.set("EventSerializer.__init__()"))
        self.serialization_fields = serialization_fields

    def serialize(self, event) -> dict:
        logger.info(msg.set("EventSerializer.serialize()"))
        return {
            field: transformation(getattr(event, field))
            for field, transformation in self.serialization_fields.item()
        }


class Serialization:
    def __init__(self, **transformations):
        logger.info(msg.set("Serialization.__init__()"))
        self.serializer = EventSerializer(transformations)

    def __call__(self, event_class):
        logger.info(msg.set("Serialization.__call__()"))

        def serialize_method(event_instance):
            logger.info(msg.set("Serialization.__call__().serialize_method()"))
            return self.serializer.serialize(event_instance)

        event_class.serialize = serialize_method
        return event_class


@Serialization(
    username=str.lower,
    password=hide_field,
    ip=show_original,
    timestamp=format_time,
)
@dataclass
class LoginEvent:
    logger.info(msg.set("LogginEvent.__init__()"))
    username: str
    password: str
    ip: str
    timestamp: datetime


def main():
    from datetime import datetime as dt
    from pprint import pprint
    from package.explore_object import check_dir, check_vars

    # print (format_time(dt.now()))
    evento_1 = LoginEvent("agustin", "admin123", "4347190283179", dt.now())
    # pprint(dir(evento_1))
    check_vars(evento_1)
    # check_dir(evento_1)
    # print (evento_1)


if __name__ == "__main__":
    main()
