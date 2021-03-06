from .. import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship


class IPAddress(BaseModel):
    __tablename__ = 'ipaddress'
    __repr_attrs__ = ['ip_address']
    id = Column(Integer, primary_key=True)
    ip_address = Column(String, unique=True)
    cidr_id = Column(Integer, ForeignKey('cidr.id'))
    OS = Column(String)
    whois = Column(String)
    ports = relationship('Port', backref='ip_address')
