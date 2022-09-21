# Descriptors - after decorators_1.py
# pag-247-248.pdf

from dataclasses import dataclass
from datetime import datetime
from functools import partial
from package.logger import buildLogger
from package.transformer_descriptor import BaseFieldTransformation
from package.explore_object import check_vars

ShowOriginal = partial(BaseFieldTransformation, transformation=lambda x: x)
HideField = partial(BaseFieldTransformation, transformation=lambda x: "**redacted**")
FormatTime = partial(BaseFieldTransformation, transformation=lambda ft: ft.strftime("%d-%m-%Y %H:%M"))

@dataclass
class LoginEvent:
    username: str = ShowOriginal()
    password: str = HideField()
    ip: str = ShowOriginal()
    timestamp: datetime = FormatTime()

    def serialize(self) -> dict:
        return {
            "username": self.username,
            "password": self.password,
            "ip": self.ip,
            "timestamp": self.timestamp,
        }

def main():
    event_1 = LoginEvent("john", "secreto passwordo", "1.1.1.1", datetime.utcnow())
    check_vars(event_1)
    
    check_vars(event_1.serialize())

if __name__ == '__main__':
    main()