import abc
import datetime
from src.domain.enums.situation_enum import SITUATION
from src.helpers.errors.domain_errors import EntityError

class Selfie(abc.ABC):
  ra: str
  dtUpload: datetime.datetime
  url: str
  situation: SITUATION

  def __init__(self, ra: str, dtUpload: datetime.datetime, url: str, situation: SITUATION):
    if (ra == None or len(ra) != 8):
      raise EntityError('ra')
    self.ra = ra
        
    if (dtUpload == None):
      raise EntityError('dtUpload')
    self.dtUpload = dtUpload

    if (url == None or ' ' in url or "." not in url):
      raise EntityError('url')
    self.url = url

    if (situation == None):
      raise EntityError('situation')
    self.situation = situation
      





