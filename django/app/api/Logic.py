import sys
import os
from .Models import UserInfo, CustomerInfo, Sample

def CreateSampleModelObject(data):
  Insert_List = []
  for item in data:
    Insert_List.append(
      Sample(
        title = item['title'],
        description = item['description']
      ))

  return Insert_List