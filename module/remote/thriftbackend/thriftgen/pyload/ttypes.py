#
# Autogenerated by Thrift Compiler (0.7.0-dev)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:slots,dynamic
#

from thrift.Thrift import TType, TMessageType

from thrift.protocol.TBase import TBase, TExceptionBase


class DownloadStatus(TBase):
  Finished = 0
  Offline = 1
  Online = 2
  Queued = 3
  Skipped = 4
  Waiting = 5
  TempOffline = 6
  Starting = 7
  Failed = 8
  Aborted = 9
  Decrypting = 10
  Custom = 11
  Downloading = 12
  Processing = 13
  Unknown = 14

  _VALUES_TO_NAMES = {
    0: "Finished",
    1: "Offline",
    2: "Online",
    3: "Queued",
    4: "Skipped",
    5: "Waiting",
    6: "TempOffline",
    7: "Starting",
    8: "Failed",
    9: "Aborted",
    10: "Decrypting",
    11: "Custom",
    12: "Downloading",
    13: "Processing",
    14: "Unknown",
  }

  _NAMES_TO_VALUES = {
    "Finished": 0,
    "Offline": 1,
    "Online": 2,
    "Queued": 3,
    "Skipped": 4,
    "Waiting": 5,
    "TempOffline": 6,
    "Starting": 7,
    "Failed": 8,
    "Aborted": 9,
    "Decrypting": 10,
    "Custom": 11,
    "Downloading": 12,
    "Processing": 13,
    "Unknown": 14,
  }

class Destination(TBase):
  Collector = 0
  Queue = 1

  _VALUES_TO_NAMES = {
    0: "Collector",
    1: "Queue",
  }

  _NAMES_TO_VALUES = {
    "Collector": 0,
    "Queue": 1,
  }

class ElementType(TBase):
  Package = 0
  File = 1

  _VALUES_TO_NAMES = {
    0: "Package",
    1: "File",
  }

  _NAMES_TO_VALUES = {
    "Package": 0,
    "File": 1,
  }


class DownloadInfo(TBase):
  """
  Attributes:
   - fid
   - name
   - speed
   - eta
   - format_eta
   - bleft
   - size
   - format_size
   - percent
   - status
   - statusmsg
   - format_wait
   - wait_until
   - packageID
   - packageName
   - plugin
  """

  __slots__ = [ 
    'fid',
    'name',
    'speed',
    'eta',
    'format_eta',
    'bleft',
    'size',
    'format_size',
    'percent',
    'status',
    'statusmsg',
    'format_wait',
    'wait_until',
    'packageID',
    'packageName',
    'plugin',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'fid', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.I64, 'speed', None, None, ), # 3
    (4, TType.I32, 'eta', None, None, ), # 4
    (5, TType.STRING, 'format_eta', None, None, ), # 5
    (6, TType.I64, 'bleft', None, None, ), # 6
    (7, TType.I64, 'size', None, None, ), # 7
    (8, TType.STRING, 'format_size', None, None, ), # 8
    (9, TType.BYTE, 'percent', None, None, ), # 9
    (10, TType.I32, 'status', None, None, ), # 10
    (11, TType.STRING, 'statusmsg', None, None, ), # 11
    (12, TType.STRING, 'format_wait', None, None, ), # 12
    (13, TType.I64, 'wait_until', None, None, ), # 13
    (14, TType.I32, 'packageID', None, None, ), # 14
    (15, TType.STRING, 'packageName', None, None, ), # 15
    (16, TType.STRING, 'plugin', None, None, ), # 16
  )

  def __init__(self, fid=None, name=None, speed=None, eta=None, format_eta=None, bleft=None, size=None, format_size=None, percent=None, status=None, statusmsg=None, format_wait=None, wait_until=None, packageID=None, packageName=None, plugin=None,):
    self.fid = fid
    self.name = name
    self.speed = speed
    self.eta = eta
    self.format_eta = format_eta
    self.bleft = bleft
    self.size = size
    self.format_size = format_size
    self.percent = percent
    self.status = status
    self.statusmsg = statusmsg
    self.format_wait = format_wait
    self.wait_until = wait_until
    self.packageID = packageID
    self.packageName = packageName
    self.plugin = plugin


class ServerStatus(TBase):
  """
  Attributes:
   - pause
   - active
   - queue
   - total
   - speed
   - download
   - reconnect
  """

  __slots__ = [ 
    'pause',
    'active',
    'queue',
    'total',
    'speed',
    'download',
    'reconnect',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'pause', None, None, ), # 1
    (2, TType.I16, 'active', None, None, ), # 2
    (3, TType.I16, 'queue', None, None, ), # 3
    (4, TType.I16, 'total', None, None, ), # 4
    (5, TType.I64, 'speed', None, None, ), # 5
    (6, TType.BOOL, 'download', None, None, ), # 6
    (7, TType.BOOL, 'reconnect', None, None, ), # 7
  )

  def __init__(self, pause=None, active=None, queue=None, total=None, speed=None, download=None, reconnect=None,):
    self.pause = pause
    self.active = active
    self.queue = queue
    self.total = total
    self.speed = speed
    self.download = download
    self.reconnect = reconnect


class ConfigItem(TBase):
  """
  Attributes:
   - name
   - description
   - value
   - type
  """

  __slots__ = [ 
    'name',
    'description',
    'value',
    'type',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'description', None, None, ), # 2
    (3, TType.STRING, 'value', None, None, ), # 3
    (4, TType.STRING, 'type', None, None, ), # 4
  )

  def __init__(self, name=None, description=None, value=None, type=None,):
    self.name = name
    self.description = description
    self.value = value
    self.type = type


class ConfigSection(TBase):
  """
  Attributes:
   - name
   - description
   - items
   - outline
  """

  __slots__ = [ 
    'name',
    'description',
    'items',
    'outline',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'description', None, None, ), # 2
    (3, TType.LIST, 'items', (TType.STRUCT,(ConfigItem, ConfigItem.thrift_spec)), None, ), # 3
    (4, TType.STRING, 'outline', None, None, ), # 4
  )

  def __init__(self, name=None, description=None, items=None, outline=None,):
    self.name = name
    self.description = description
    self.items = items
    self.outline = outline


class FileData(TBase):
  """
  Attributes:
   - fid
   - url
   - name
   - plugin
   - size
   - format_size
   - status
   - statusmsg
   - packageID
   - error
   - order
   - progress
  """

  __slots__ = [ 
    'fid',
    'url',
    'name',
    'plugin',
    'size',
    'format_size',
    'status',
    'statusmsg',
    'packageID',
    'error',
    'order',
    'progress',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'fid', None, None, ), # 1
    (2, TType.STRING, 'url', None, None, ), # 2
    (3, TType.STRING, 'name', None, None, ), # 3
    (4, TType.STRING, 'plugin', None, None, ), # 4
    (5, TType.I64, 'size', None, None, ), # 5
    (6, TType.STRING, 'format_size', None, None, ), # 6
    (7, TType.I32, 'status', None, None, ), # 7
    (8, TType.STRING, 'statusmsg', None, None, ), # 8
    (9, TType.I32, 'packageID', None, None, ), # 9
    (10, TType.STRING, 'error', None, None, ), # 10
    (11, TType.I16, 'order', None, None, ), # 11
    (12, TType.BYTE, 'progress', None, None, ), # 12
  )

  def __init__(self, fid=None, url=None, name=None, plugin=None, size=None, format_size=None, status=None, statusmsg=None, packageID=None, error=None, order=None, progress=None,):
    self.fid = fid
    self.url = url
    self.name = name
    self.plugin = plugin
    self.size = size
    self.format_size = format_size
    self.status = status
    self.statusmsg = statusmsg
    self.packageID = packageID
    self.error = error
    self.order = order
    self.progress = progress


class PackageData(TBase):
  """
  Attributes:
   - pid
   - name
   - folder
   - site
   - password
   - dest
   - order
   - priority
   - fids
   - links
  """

  __slots__ = [ 
    'pid',
    'name',
    'folder',
    'site',
    'password',
    'dest',
    'order',
    'priority',
    'fids',
    'links',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'pid', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.STRING, 'folder', None, None, ), # 3
    (4, TType.STRING, 'site', None, None, ), # 4
    (5, TType.STRING, 'password', None, None, ), # 5
    (6, TType.I32, 'dest', None, None, ), # 6
    (7, TType.I16, 'order', None, None, ), # 7
    (8, TType.BYTE, 'priority', None, None, ), # 8
    (9, TType.LIST, 'fids', (TType.I32,None), None, ), # 9
    (10, TType.LIST, 'links', (TType.STRUCT,(FileData, FileData.thrift_spec)), None, ), # 10
  )

  def __init__(self, pid=None, name=None, folder=None, site=None, password=None, dest=None, order=None, priority=None, fids=None, links=None,):
    self.pid = pid
    self.name = name
    self.folder = folder
    self.site = site
    self.password = password
    self.dest = dest
    self.order = order
    self.priority = priority
    self.fids = fids
    self.links = links


class CaptchaTask(TBase):
  """
  Attributes:
   - tid
   - data
   - type
   - resultType
  """

  __slots__ = [ 
    'tid',
    'data',
    'type',
    'resultType',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I16, 'tid', None, None, ), # 1
    (2, TType.STRING, 'data', None, None, ), # 2
    (3, TType.STRING, 'type', None, None, ), # 3
    (4, TType.STRING, 'resultType', None, None, ), # 4
  )

  def __init__(self, tid=None, data=None, type=None, resultType=None,):
    self.tid = tid
    self.data = data
    self.type = type
    self.resultType = resultType


class Event(TBase):
  """
  Attributes:
   - event
   - id
   - type
   - destination
  """

  __slots__ = [ 
    'event',
    'id',
    'type',
    'destination',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'event', None, None, ), # 1
    (2, TType.I32, 'id', None, None, ), # 2
    (3, TType.I32, 'type', None, None, ), # 3
    (4, TType.I32, 'destination', None, None, ), # 4
  )

  def __init__(self, event=None, id=None, type=None, destination=None,):
    self.event = event
    self.id = id
    self.type = type
    self.destination = destination


class UserData(TBase):
  """
  Attributes:
   - name
   - email
   - role
   - permission
   - template
  """

  __slots__ = [ 
    'name',
    'email',
    'role',
    'permission',
    'template',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'email', None, None, ), # 2
    (3, TType.I32, 'role', None, None, ), # 3
    (4, TType.I32, 'permission', None, None, ), # 4
    (5, TType.STRING, 'template', None, None, ), # 5
  )

  def __init__(self, name=None, email=None, role=None, permission=None, template=None,):
    self.name = name
    self.email = email
    self.role = role
    self.permission = permission
    self.template = template


class AccountInfo(TBase):
  """
  Attributes:
   - validuntil
   - login
   - options
   - valid
   - trafficleft
   - maxtraffic
   - premium
   - type
  """

  __slots__ = [ 
    'validuntil',
    'login',
    'options',
    'valid',
    'trafficleft',
    'maxtraffic',
    'premium',
    'type',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'validuntil', None, None, ), # 1
    (2, TType.STRING, 'login', None, None, ), # 2
    (3, TType.MAP, 'options', (TType.STRING,None,TType.STRING,None), None, ), # 3
    (4, TType.BOOL, 'valid', None, None, ), # 4
    (5, TType.I64, 'trafficleft', None, None, ), # 5
    (6, TType.I64, 'maxtraffic', None, None, ), # 6
    (7, TType.BOOL, 'premium', None, None, ), # 7
    (8, TType.STRING, 'type', None, None, ), # 8
  )

  def __init__(self, validuntil=None, login=None, options=None, valid=None, trafficleft=None, maxtraffic=None, premium=None, type=None,):
    self.validuntil = validuntil
    self.login = login
    self.options = options
    self.valid = valid
    self.trafficleft = trafficleft
    self.maxtraffic = maxtraffic
    self.premium = premium
    self.type = type


class AccountData(TBase):
  """
  Attributes:
   - type
   - login
   - password
   - options
  """

  __slots__ = [ 
    'type',
    'login',
    'password',
    'options',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'type', None, None, ), # 1
    (2, TType.STRING, 'login', None, None, ), # 2
    (3, TType.STRING, 'password', None, None, ), # 3
    (4, TType.MAP, 'options', (TType.STRING,None,TType.STRING,None), None, ), # 4
  )

  def __init__(self, type=None, login=None, password=None, options=None,):
    self.type = type
    self.login = login
    self.password = password
    self.options = options


class ServiceCall(TBase):
  """
  Attributes:
   - plugin
   - func
   - arguments
   - parseArguments
  """

  __slots__ = [ 
    'plugin',
    'func',
    'arguments',
    'parseArguments',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'plugin', None, None, ), # 1
    (2, TType.STRING, 'func', None, None, ), # 2
    (3, TType.LIST, 'arguments', (TType.STRING,None), None, ), # 3
    (4, TType.BOOL, 'parseArguments', None, None, ), # 4
  )

  def __init__(self, plugin=None, func=None, arguments=None, parseArguments=None,):
    self.plugin = plugin
    self.func = func
    self.arguments = arguments
    self.parseArguments = parseArguments


class OnlineStatus(TBase):
  """
  Attributes:
   - name
   - plugin
   - status
   - size
  """

  __slots__ = [ 
    'name',
    'plugin',
    'status',
    'size',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'plugin', None, None, ), # 2
    (3, TType.I32, 'status', None, None, ), # 3
    (4, TType.I64, 'size', None, None, ), # 4
  )

  def __init__(self, name=None, plugin=None, status=None, size=None,):
    self.name = name
    self.plugin = plugin
    self.status = status
    self.size = size


class PackageDoesNotExists(TExceptionBase):
  """
  Attributes:
   - pid
  """

  __slots__ = [ 
    'pid',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'pid', None, None, ), # 1
  )

  def __init__(self, pid=None,):
    self.pid = pid

  def __str__(self):
    return repr(self)


class FileDoesNotExists(TExceptionBase):
  """
  Attributes:
   - fid
  """

  __slots__ = [ 
    'fid',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'fid', None, None, ), # 1
  )

  def __init__(self, fid=None,):
    self.fid = fid

  def __str__(self):
    return repr(self)


class ServiceDoesNotExists(TExceptionBase):
  """
  Attributes:
   - plugin
   - func
  """

  __slots__ = [ 
    'plugin',
    'func',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'plugin', None, None, ), # 1
    (2, TType.STRING, 'func', None, None, ), # 2
  )

  def __init__(self, plugin=None, func=None,):
    self.plugin = plugin
    self.func = func

  def __str__(self):
    return repr(self)


class ServiceException(TExceptionBase):
  """
  Attributes:
   - msg
  """

  __slots__ = [ 
    'msg',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'msg', None, None, ), # 1
  )

  def __init__(self, msg=None,):
    self.msg = msg

  def __str__(self):
    return repr(self)

