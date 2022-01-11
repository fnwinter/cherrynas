import os

def get_file_size(path):
  """
  >>> get_file_size()
  """

  size = ''
  try:
    _n_size = os.path.getsize(path)
    if _n_size > 1024 * 1024:
      size = '%.2f MB' % (_n_size / 1048576.0)
    elif _n_size > 1024:
      size = '%d KB' % (_n_size / 1024)
    else:
      size = '%d Bytes' % _n_size

  except os.error:
    size = 'wrong size'
  return size